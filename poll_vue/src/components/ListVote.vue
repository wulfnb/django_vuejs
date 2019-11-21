<template>
    <div class="">
        <h3>
        Votes counted
        </h3>
        <div v-for="(item,key) in questions">
            <hr>
            <!-- {{ item }} -->
            <p class="text-danger">{{ item.question_text }} </p>
            <div v-for="(opt,k) in item.options">
                <p class="text-info"> {{ opt.choice }} - {{ opt.votes }} </p>

            </div>
        </div>
        <button v-if="votes" @click="saveVote" class="btn btn-primary">
            Save my vote
        </button>
    </div>
</template>


<script>
export default {
  data() {
      return {
          questions: '',
      }
  },
  created () {

  },
  mounted () {
      this.getPolls()
  },
  methods: {
    getPolls(){
        fetch('http://127.0.0.1:8000/polls/', {
                method: 'GET',
                headers: {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                },
            }).then(response => {
                return response.json()
            }).then(json => {
                this.questions = json.data
            })
    },
  }
}

</script>