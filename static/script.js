$guess = $('#guess')
$guessBtn = $('#guessBtn')
$guessBtn.on('click', postGuess)
async function postGuess(){
    let response = await axios({
        method: "post",
        url: 'http://127.0.0.1:5000/guess',
        data: {
            guess: $guess.val()
        }
    })
    console.log(response)
    $guess.val('')
    return response
}
