$guess = $('#guess')
$guessBtn = $('#guessBtn')
$guessBtn.on('click', postGuess)
score = 0;

setTimeout(endGame, 60000)

async function endGame(){
    $guessBtn.empty()
    $guessBtn.append('time is up! new game?')
    $guessBtn.on('click', function(){
        location.reload()
    })
    let form = new FormData()
    form.append('score', score)
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



async function postGuess(){
    let form = new FormData()
    form.append('guess', $guess.val())
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
        score += $guess.val().length
        $('#score').empty()
        $('#score').append(score)
    }
    $guess.val('')
} 