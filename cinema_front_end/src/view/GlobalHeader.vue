<template>
  <div>
    <nav class="navbar">
      <div class="logo" style="font-size: 1.5em; font-weight: bold">
        <a href="#/">Cinema</a>
      </div>
      <a href="https://cinema.com.hk/" class="text-blue-600" target="_blank">
        reference
      </a>
      <ul
        style="list-style: none; display: flex; margin: 0; padding: 0"
        v-if="!userName"
      >
        <li style="margin: 0 15px">
          <a href="#/login" class="nav-tabs">登入</a>
        </li>
        <li style="margin: 0 15px">|</li>
        <li style="margin: 0 15px">
          <a href="#/register" class="nav-tabs">成为会员</a>
        </li>
        <li style="margin: 0 15px"><a href="#" class="nav-tabs"></a></li>
        <li style="margin: 0 15px">
          <a href="#" class="nav-tabs">FaceBook</a>
        </li>
      </ul>
      <div v-else class="mr-8">
        <UserOutlined class="mr-3" />
        <u>
          <Dropdown placement="bottom">
            <a href="#/profile">{{ userName }}</a>
            <template #overlay>
              <a-menu>
                <a-menu-item>
                  <a href="javascript:;">订票记录</a>
                </a-menu-item>
                <a-menu-item>
                  <a href="#/profile">用户资料</a>
                </a-menu-item>
                <a-menu-item>
                  <a href="javascript:;">我的钱包</a>
                </a-menu-item>
                <a-menu-item>
                  <a href="javascript:;">登出</a>
                </a-menu-item>
              </a-menu>
            </template>
          </Dropdown>
        </u>
        , 你好
      </div>
    </nav>
  </div>
  <br />
  <br />
</template>
<script setup lang="ts">
  import { useUserStore } from '@/modules/store/user'
  import { ref } from 'vue'
  import { UserOutlined } from '@ant-design/icons-vue'
  import { Dropdown } from 'ant-design-vue'

  const user = useUserStore()
  const userName = ref(user.userName)
</script>
<style>
  .nav-tabs {
    color: white;
    text-decoration: none;
  }
  .navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #333;
    color: white;
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 1000;
  }
</style>
