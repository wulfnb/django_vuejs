<template>
    <div class="">
        <h3>
        Add Your Vote
        </h3>
        <!-- Looping through the question -->
        <div v-for="(item,key) in questions">
            <hr>
            <p class="text-danger">{{ item.question_text }} </p>
            <!-- Looping threw the options -->
            <div v-for="(opt,k) in item.options">
                <label class="text-info"><input type="radio" :name="item.id" @click="updateVote(item.id, opt.choice_id)"> {{ opt.choice }} </label>
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
          votes: {}
      }
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
    // updating the votes to an object with question id as key
    updateVote(question,choice){
        this.votes[question] = choice
    },
    saveVote(){
        fetch('http://127.0.0.1:8000/polls/vote/', {
            method: 'post',
            body: JSON.stringify(this.votes)
        }).then(function(response) {
            return response.json();
        }).then(function(data) {
            alert('Your vote added, Thankyou');
            this.votes= {}
        });
    }
  }
}

</script>