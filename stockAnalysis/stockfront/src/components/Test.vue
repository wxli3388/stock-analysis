<template>
  <div class="my-content">
    <el-table :data="stockData">
      <el-table-column
        prop="publish_date_string"
        label="日期">
      </el-table-column>
      <el-table-column
        prop="author"
        label="作者">
      </el-table-column>
      <el-table-column label="標題">
        <template scope="scope">
          <a :href="scope.row.article_url">{{scope.row.title}}</a>
        </template>
      </el-table-column>
    </el-table>
    <!-- <router-link to="/">Go to index</router-link> -->
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      stockTitle: ['日期', '作者', '標題'],
      stockData: null
    }
  },
  mounted () {
    //axios.get('http://127.0.0.1:8000/api/stock/ptt-stock-article')
    axios.get('api/stock/ptt-stock-article')
      .then(response => {
        if (response.data.statusCode===200)          
          this.stockData = response.data.payload
      })
  },
  methods:{
    onTitleClick(url){
      window.location.href=url
    }
  }
}
</script>

<style scoped>

</style>
