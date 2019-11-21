import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './components/App.vue'

Vue.use(VueRouter)
import AddPoll from './components/AddPoll.vue'
import Vote from './components/Vote.vue'
import ListVote from './components/ListVote.vue'

const router = new VueRouter({
    mode: 'history',
    // Setting routs
    routes: [
        { path: '/addpoll', component: AddPoll, name: 'AddPoll' },
        { path: '/vote', component: Vote, name: 'Vote' },
        { path: '/listvote', component: ListVote, name: 'ListVote' }
    ]
})

new Vue({
    el: '#app',
    router,
    render: h=> h(App),
    data: {
        question: '',
    },
    methods: {
    }
})