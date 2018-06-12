<template>
  <div class="my-content" >
    <div class="filter-container">
      <el-input @keyup.enter.native="handleFilter" style="width: 200px;" class="filter-item" v-model="listQuery.keyword">
      </el-input>
      <el-select style="width: 90px" class="filter-item" v-model="listQuery.column">
        <el-option v-for="item in columnOptions" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select>
      <!-- <el-select clearable class="filter-item" style="width: 130px" v-model="listQuery.type">
        <el-option v-for="item in pageOptions" :key="item.key" :label="item.display_name+'('+item.key+')'" :value="item.key">
        </el-option>
      </el-select>
      <el-select @change='handleFilter' style="width: 140px" class="filter-item" v-model="listQuery.sort">
        <el-option v-for="item in sortOptions" :key="item.key" :label="item.label" :value="item.key">
        </el-option>
      </el-select> -->
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">搜尋</el-button>
      <!-- <el-button class="filter-item" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-edit">{{$t('table.add')}}</el-button>
      <el-button class="filter-item" type="primary" :loading="downloadLoading" v-waves icon="el-icon-download" @click="handleDownload">{{$t('table.export')}}</el-button>
      <el-checkbox class="filter-item" style='margin-left:15px;' @change='tableKey=tableKey+1' v-model="showReviewer">{{$t('table.reviewer')}}</el-checkbox> -->
    </div>
    <el-table :data="list" v-loading="listLoading" element-loading-text="資料加載中" >
      <el-table-column
        prop="code"
        label="代號">
      </el-table-column>
      <el-table-column
        prop="name"
        label="名稱">
      </el-table-column>
      <el-table-column
        prop="publish_date"
        label="日期">
      </el-table-column>
      <el-table-column
        prop="trading_volume"
        label="成交股數">
      </el-table-column>
      <el-table-column
        prop="transaction"
        label="成交筆數">
      </el-table-column>
      <el-table-column
        prop="turn_over"
        label="成交金額">
      </el-table-column>
      <el-table-column
        prop="opening_price"
        label="開盤價">
      </el-table-column>
      <el-table-column
        prop="highest_price"
        label="最高價">
      </el-table-column>
      <el-table-column
        prop="lowest_price"
        label="最低價">
      </el-table-column>
      <el-table-column
        prop="closing_price"
        label="收盤價">
      </el-table-column>
      <el-table-column
        prop="change,opening_price"
        label="漲跌(+/-)">
        <template slot-scope="scope">
          <span v-bind:style="[parseFloat(scope.row.change)>0 ? {color:'red'}:{color:'green'}]">
            {{scope.row.change}} ({{(scope.row.change*100/scope.row.opening_price).toFixed(2)}}%)
          </span>
        </template>
      </el-table-column>
      <el-table-column
        prop="last_ask_price"
        label="最後揭示買價">
      </el-table-column>
      <el-table-column
        prop="last_bid_price"
        label="最後揭示賣價">
      </el-table-column>
      <el-table-column
        prop="price_earnings_ratio"
        label="本益比">
      </el-table-column>
    </el-table>
    <div class="pagination-container">
      <el-pagination background @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="listQuery.page" :page-sizes="[10,20,30, 50]" :page-size="listQuery.limit" layout="total, sizes, prev, pager, next, jumper" :total="total">
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
        limit: 20,
        keyword: undefined,
        column: 'code',
        type: undefined,
        sort: '+id'
      },
      columnOptions: [{
        value: 'code',
        label: '代號'
      },
      {
        value: 'name',
        label: '名稱'
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
      // axios.post('api/stock/stock-data',
      axios.post('http://127.0.0.1:8000/api/stock/stock-data',
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
    }
  }
}
</script>

<style slot-scope>
/* .my-content{
  background-color:black;
} */
</style>
