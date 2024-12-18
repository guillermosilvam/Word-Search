function showGamePage() {
    var container = document.getElementById("rules");
    var gamePage = document.getElementById("gamePage");

    container.classList.add('hidden')
    gamePage.classList.remove('hidden')
}

window.onload = function rules() {
    var rules = document.getElementById("rules");
    rules.classList.remove('hidden')
    rules.classList.add('flex')
}


