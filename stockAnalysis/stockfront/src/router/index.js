import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios'

import Layout from '@/components/layout/Layout'
import PttStock from '@/components/PttStock'
import Index from '@/components/Index'
import TwseStockData from '@/components/TwseStockData'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/zh-TW'

Vue.use(Router)
Vue.use(ElementUI, { locale })
window.axios = axios

export default new Router({
  routes: [{
    path: '/',
    component: Index
  },
  {
    path: '/ptt-stock',
    component: PttStock
  },
  {
    path: '/twse-stock-data',
    component: TwseStockData
  }
  ]
})
