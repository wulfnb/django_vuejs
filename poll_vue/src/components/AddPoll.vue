<template>
    <div id="poll">
        <div class="row">
            <div class="col-md-3">
                Question
            </div>
            <div class="col-md-3">
                <input type="text" v-model="question" class='form-group'>
            </div>
            
        </div>
        <div class="row">
            <div class="col-md-3">
                Publish Date
            </div>
            <div class="col-md-3">
                <input type="date" v-model="pub_date" class='form-group'>
            </div>
        </div>

            <div v-for="(opt,key) in options" class="row">
                <div class="col-md-3">
                    Option {{key+1}}
                </div>
                <div class="col-md-3">
                    <input type="text" :value="opt" v-on:input="updateOption(key,$event.target.value)" class='form-group'>
                    <input v-if="key+1 == options.length" type="button" @click="addNewOptions()" class="btn btn-primary" value="+" title="Add More option">
                </div>

            </div>
            <div class="row">
                <div class="col-md-offset-3 col-md-3">
                    <input type="button" @click="postPollQuestion()" class="btn btn-primary" value="Save Question">
                </div>
            </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      question: '',
      pub_date: '',
      options: ['','',''],
    }
  },
  methods: {
    // Here we setting the value of question
    updateOption(key, val){
        this.options[key] = val
    },

    addNewOptions(){
        this.options.push('')
    },

    postPollQuestion(){
        let opts = {
            question_text: this.question,
            pub_date: this.pub_date,
            choices: this.options
        }

        fetch('http://127.0.0.1:8000/polls/create/', {
            method: 'post',
            body: JSON.stringify(opts)
        }).then(function(response) {
            return response.json();
        }).then(function(data) {
            console.log('Created Gist:', data.html_url);
            alert('question added successfully');
            this.question= '';
            this.pub_date= '';
            this.options= ['','',''];

        });
    }
  }
}

</script>