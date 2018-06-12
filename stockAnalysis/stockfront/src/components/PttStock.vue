<template>
  <div class="my-content" >
    <div class="filter-container">
      <el-input @keyup.enter.native="handleFilter" style="width: 200px;" class="filter-item" v-model="listQuery.keyword">
      </el-input>
      <el-select style="width: 90px" class="filter-item" v-model="listQuery.column">
        <el-option v-for="item in columnOptions" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select>
      <!-- <el-select style="width: 90px" class="filter-item" v-model="listQuery.column">
        <el-option v-for="item in columnOptions" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select> -->
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">搜尋</el-button>
    </div>
    <el-table :data="list" v-loading="listLoading" element-loading-text="資料加載中">
      <el-table-column
        prop="publish_date_string"
        label="日期">
      </el-table-column>
      <el-table-column
        prop="author"
        label="作者">
      </el-table-column>
      <el-table-column label="標題">
        <template slot-scope="scope">
          <a :href="scope.row.article_url">{{scope.row.title}}</a>
        </template>
      </el-table-column>
    </el-table>
    <div class="pagination-container">
      <el-pagination background @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="listQuery.page" :page-sizes="[10,20,50]" :page-size="listQuery.limit" layout="total, sizes, prev, pager, next, jumper" :total="total">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import Qs from 'qs'
export default {
  data () {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        keyword: undefined,
        column: 'title',
        type: undefined
      },
      columnOptions: [{
        value: 'title',
        label: '標題'
      }, {
        value: 'author',
        label: '作者'
      }
      ]
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      axios.post('api/stock/ptt-stock-article',
      // axios.post('http://127.0.0.1:8000/api/stock/ptt-stock-article',
        Qs.stringify(this.listQuery),
        {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}
      ).then(response => {
        if (response.data.statusCode === 200) {
          this.list = response.data.payload.data
          this.total = response.data.payload.total
          this.listLoading = false
        }
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getList()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.getList()
    },
    onTitleClick(url) {
      window.location.href = url
    }
  }
}
</script>
