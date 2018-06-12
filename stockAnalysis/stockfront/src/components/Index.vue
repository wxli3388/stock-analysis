<template>
  <div class="my-content">
    <div style="display:inline-block">
      <img :src="stockImage">
    </div>
    <div style="display:inline-block">
      <router-link to="/ptt-stock">PTT文章</router-link>
      <router-link to="/twse-stock-data">股票資訊</router-link>
    </div>
  </div>
</template>

<script>
import stockImage from '../assets/stock.jpg'

export default {
  name: 'HelloWorld',
  data () {
    return {
      stockImage: stockImage
    }
  }
}
</script>
