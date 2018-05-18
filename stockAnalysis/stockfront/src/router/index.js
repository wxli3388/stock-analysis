import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios'

import Layout from '@/components/layout/Layout'
import HelloWorld from '@/components/HelloWorld'
import Test from '@/components/Test'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Router)
Vue.use(ElementUI)
window.axios = axios

export default new Router({
    routes: [{
            path: '/',
            component: Layout
        },
        {
            path: '/test',
            component: Test
        }
    ]
})