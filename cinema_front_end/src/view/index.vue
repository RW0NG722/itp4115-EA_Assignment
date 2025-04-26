<template>
  <nav style="position: fixed; top: 0; left: 0; width: 100%; background-color: #333; color: white; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center; z-index: 1000;">
    <div class="logo" style="font-size: 1.5em; font-weight: bold;"><a href="#/index">Cinema</a></div>
    <ul style="list-style: none; display: flex; margin: 0; padding: 0;">
      <li style="margin: 0 15px;"><a href="#/login" class="nav-tabs">登入</a></li>
      <li style="margin: 0 15px;">|</li>
      <li style="margin: 0 15px;"><a href="#/register" class="nav-tabs">成为会员</a></li>
      <li style="margin: 0 15px;"><a href="#" class="nav-tabs"></a></li>
      <li style="margin: 0 15px;"><a href="#" class="nav-tabs">FaceBook</a></li>
    </ul>
  </nav>
  <br><br>
  <Row>
    <a-col :span="24" align="center" >
      <Space>
        <div>logo</div>
        <div>banner</div>
      </Space>
    </a-col>
    <a-col :span="24" style="padding: 20px; text-align: center;">
      carousel
    </a-col>
    <a-col :span="24" style="padding: 20px; text-align: center;">
      <Space :size="50">
        <Tabs class=" border w-200 h-100" :centered="true">
          <TabPane key="1" tab="即日/预售">
            <Now />
          </TabPane>
          <TabPane key="2" tab="即将上映">
            <Upcoming />
          </TabPane>
          <TabPane key="3" tab="特备节目">
            <Special />
          </TabPane>
          <TabPane key="4" tab="戏院">
            <Cinemas />
          </TabPane>
          <TabPane key="5" tab="礼品卡区">
            <GiftCardShop />
          </TabPane>
          </Tabs>
          <div class=" border w-60 h-100">
            戏院
          </div>
      </Space>
    </a-col>
  </Row>

</template>
<script lang="ts" setup>
import { Row, Space, TabPane, Tabs } from 'ant-design-vue';
import Now from './tabs/Now.vue';
import Upcoming from './tabs/Upcoming.vue';
import Special from './tabs/Special.vue';
import Cinemas from './tabs/Cinemas.vue';
import GiftCardShop from './tabs/GiftCardShop.vue';


</script>
<style scoped>
.nav-tabs {
  color: white; text-decoration: none;
}
</style>
