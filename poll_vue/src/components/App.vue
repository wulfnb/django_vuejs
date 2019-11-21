<template>
    <div id='app'>
        <ul class="nav">
            <li class="nav-item">
                <!-- Link activates if its not in the same page -->
                <router-link 
                    :class="(this.$route.path !== '/addpoll')? 'nav-link': 'nav-link disabled'" 
                    :to="{ name: 'AddPoll', params: { } }">
                    Add Poll question
                </router-link>
            </li>
            <li class="nav-item">
                <router-link :class="(this.$route.path !== '/vote')? 'nav-link': 'nav-link disabled'" :to="{ name: 'Vote', params: { } }">
                    Vote
                </router-link>
            </li>
            <li class="nav-item">
                <router-link :class="(this.$route.path !== '/listvote')? 'nav-link': 'nav-link disabled'" :to="{ name: 'ListVote', params: { } }">
                    List the votes Vote
                </router-link>
            </li>
        </ul>

        <router-view></router-view>
    </div>
</template>