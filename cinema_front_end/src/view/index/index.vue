<template>
  <GlobalHeader />
  <Row>
    <a-col :span="24" align="center">
      <Space>
        <div class="w-[210px] h-[110px]">
          <img src="/src/assets/index_logo.png" />
        </div>
        <div class="w-[610px] h-[90px] border">广告位招租</div>
      </Space>
    </a-col>
    <a-col :xl="18" :xxl="15" class="border mr-auto ml-auto">
      <IndexCarousel />
    </a-col>
    <a-col :span="24" style="padding: 20px; text-align: center">
      <Space :size="50">
        <Tabs class="border w-[750px] h-[870px]" :centered="true">
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
        <div class="border w-60 h-[870px]">
          <div align="left" class="text-2xl ml-3 mt-2">戏院</div>
          <a-row class="mt-3">
            <a-col :span="8" class="cinemas_region"> 九龙 </a-col>
            <a-col :span="16">
              <div
                class="mb-2"
                align="left"
                v-for="cinema in jiulong"
                :key="cinema"
              >
                {{ cinema }}
              </div>
            </a-col>
          </a-row>
          <a-row class="mt-3">
            <a-col :span="8" class="cinemas_region"> 香港 </a-col>
            <a-col :span="16">
              <div
                class="mb-2"
                align="left"
                v-for="cinema in hongkong"
                :key="cinema"
              >
                {{ cinema }}
              </div></a-col
            >
          </a-row>
          <a-row class="mt-3">
            <a-col :span="8" class="cinemas_region"> 新界 </a-col>
            <a-col :span="16">
              <div
                class="mb-2"
                align="left"
                v-for="cinema in newTerritories"
                :key="cinema"
              >
                {{ cinema }}
              </div></a-col
            >
          </a-row>
        </div>
      </Space>
    </a-col>
  </Row>
</template>
<script lang="ts" setup>
  import { Row, Space, TabPane, Tabs } from 'ant-design-vue'
  import Now from './tabs/Now.vue'
  import Upcoming from './tabs/Upcoming.vue'
  import Special from './tabs/Special.vue'
  import Cinemas from './tabs/Cinemas.vue'
  import GiftCardShop from './tabs/GiftCardShop.vue'
  import IndexCarousel from './IndexCarousel.vue'
  import GlobalHeader from '../GlobalHeader.vue'

  const jiulong = [
    'GALA CINEMA (朗豪坊)',
    'B+ cinema MOKO (旺角東)',
    'B+ cinema apm (觀塘)',
    'PREMIERE ELEMENTS',
    '電影中心',
    '旺角',
  ]

  const hongkong = [
    'MOViE MOViE Pacific Place (金鐘)',
    'MOViE MOViE Cityplaza (太古城)',
    'PALACE ifc',
  ]

  const newTerritories = ['MY CINEMA YOHO MALL', '葵芳', '荃灣', '嘉湖']
</script>
<style scoped>
  .cinemas_region {
    color: #9c7738;
    font-size: 15px;
  }
</style>
