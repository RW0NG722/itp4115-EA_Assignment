<template>
  <div class="w-[747px] h-[870px]" align="center">
    <Row :justify="'space-between'" class="pl-5 pr-5" v-for="i in imgList">
      <Col class="w-[170px] h-[230px] bg-red-500 mb-3" v-for="j in i">
        <img :src="j" alt="movie" style="width: 100%; height: 100%" />
      </Col>
    </Row>
    <div class="w-[95%] text-3xl bg-yellow-50 pt-2 pb-2">更多电影</div>
  </div>
</template>
<script setup lang="ts">
  import { Col, Row } from 'ant-design-vue'
  import { ref } from 'vue'

  const imgList = ref([
    [
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1744971265.jpg',
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1743150081.jpg',
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1741834137.jpg',
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1745477895.jpg',
    ],
    [
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1743672933.jpg',
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1745386970.jpg',
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1741238336.jpg',
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1745564421.jpg',
    ],
    [
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1729681665.jpg',
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1745477562.jpg',
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1742806291.jpg',
      'https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1742190177.jpg',
    ],
  ])
</script>
<style></style>
