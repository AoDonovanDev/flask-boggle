class Game{
    constructor(){
        this.score = 0
        this.guesses = []
        this.$guess = $('#guess')
        this.$guessBtn = $('#guessBtn')
        this.$guessBtn.on('click', this.postGuess)
        setTimeout(this.endGame, 60000)
        self = this;
    }

    async endGame(){
        console.log(self)
        self.$guessBtn.empty()
        self.$guessBtn.append('time is up! new game?')
        self.$guessBtn.on('click', function(){
            location.reload()
        })
        let form = new FormData()
        form.append('score', self.score)
        let response = await axios({
            method: "post",
            url: 'http://127.0.0.1:5000/end',
            data: form
        })
        let servData = await response
        console.log(servData)
        $('#highScore').empty()
        $('#highScore').append(servData.data.highScore)
        $('#count').empty()
        $('#count').append(servData.data.count)
    }
    async postGuess(){
        console.log($(this))
        console.log(self)
        let guess = $('#guess').val()
        if(self.guesses.indexOf(guess) === -1){
        let form = new FormData()
        form.append('guess', guess)
        let response = await axios({
            method: "post",
            url: 'http://127.0.0.1:5000/guess',
            data: form
        })
        console.log(response)
       
        let msg = await response
        $('#msg').empty()
        $('#msg').append(msg.data.result)
        if(msg.data.result === "ok"){
            self.score += guess.length
            self.guesses.push(guess)
            $('#score').empty()
            $('#score').append(self.score)
        }
        $('#guess').val('')
    } 
    }
}
new Game()



