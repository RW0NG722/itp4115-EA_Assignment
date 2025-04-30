<template>
  <Row>
    <Col :span="18" align="center">
      <a-carousel effect="fade">
        <div>
          <div style="display: flex; align-items: center">
            <div class="border w-[178px] h-[250px] ml-6 mt-3 mb-3">
              <img
                src="https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1744971265.jpg"
                alt="movie"
                style="width: 100%; height: 100%"
              />
            </div>
            <div class="border w-[65%] h-[250px] ml-8">
              <iframe
                width="100%"
                height="100%"
                src="https://www.youtube.com/embed/ppSnaucz0bA?si=P-XNHTsV13BjeJ1j"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen
              />
            </div>
          </div>
        </div>

        <div>
          <div style="display: flex; align-items: center">
            <div class="border w-[178px] h-[250px] ml-6 mt-3 mb-3">
              <img
                src="https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1743672088.jpg"
                alt="movie"
                style="width: 100%; height: 100%"
              />
            </div>
            <div class="border w-[65%] h-[250px] ml-8">
              <iframe
                width="100%"
                height="100%"
                src="https://www.youtube.com/embed/5UDyNgBkgv0?si=VZBxcAvLerBcZ5Ac"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen
              ></iframe>
            </div>
          </div>
        </div>

        <div>
          <div style="display: flex; align-items: center">
            <div class="border w-[178px] h-[250px] ml-6 mt-3 mb-3">
              <img
                src="https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1744794603.jpg"
                alt="movie"
                style="width: 100%; height: 100%"
              />
            </div>
            <div class="border w-[65%] h-[250px] ml-8">
              <iframe
                width="100%"
                height="100%"
                src="https://www.youtube.com/embed/AGpmfQAcMHo?si=zRaWDdUX2ek8mQha"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen
              ></iframe>
            </div>
          </div>
        </div>

        <div>
          <div style="display: flex; align-items: center">
            <div class="border w-[178px] h-[250px] ml-6 mt-3 mb-3">
              <img
                src="https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1742190177.jpg"
                alt="movie"
                style="width: 100%; height: 100%"
              />
            </div>
            <div class="border w-[65%] h-[250px] ml-8">
              <iframe
                width="100%"
                height="100%"
                src="https://www.youtube.com/embed/sHXvex0hWQ4?si=9vry0WEx6yWIocYv"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen
              ></iframe>
            </div>
          </div>
        </div>

        <div>
          <div style="display: flex; align-items: center">
            <div class="border w-[178px] h-[250px] ml-6 mt-3 mb-3">
              <img
                src="https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/movie/movie_1743150081.jpg"
                alt="movie"
                style="width: 100%; height: 100%"
              />
            </div>
            <div class="border w-[65%] h-[250px] ml-8">
              <iframe
                width="100%"
                height="100%"
                src="https://www.youtube.com/embed/2qI2D2oU5fo?si=qcinw1Lhly3S-C0M"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                referrerpolicy="strict-origin-when-cross-origin"
                allowfullscreen
              ></iframe>
            </div>
          </div>
        </div>
      </a-carousel>
    </Col>
    <Col :span="6" align="center">
      <a-row justify="space-around" align="middle" style="height: 100%">
        <a-col :span="24">
          <img
            src="https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/webcms/images/bcSunday2023Ticketing banner-300x76_163c9f532d18f5.png"
          />
        </a-col>
        <a-col :span="24">
          <img
            src="https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/webcms/images/IMAX_163c8dc38dd5b5.jpg"
          />
        </a-col>
        <a-col :span="24">
          <img
            src="https://mediafiles.cinema.com.hk/broadway/cmsimg/cinweb/webcms/images/FT%20Banner%20Ad%20300x76_167f38817b0b11.jpg"
          />
        </a-col>
      </a-row>
    </Col>
  </Row>
</template>
<script setup lang="ts">
  import { Col, Row } from 'ant-design-vue'

  console.log('script')
</script>

<style scoped>
  :deep(.slick-slide) {
    text-align: center;
    height: 290px;
    line-height: 220px;
    background: #364d79;
    overflow: hidden;
  }
  :deep(.slick-slide h3) {
    color: #fff;
  }
</style>
