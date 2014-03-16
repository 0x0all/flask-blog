window.onscroll = function() {
    hljs.initHighlightingOnLoad();  // for highlight.js
    // display: none if on top
    if (document.documentElement.scrollTop||document.body.scrollTop) {
        document.getElementById('backtotop').style.display = 'block';
    } else {
        document.getElementById('backtotop').style.display = 'none';
    }
}


var toTopImg = document.getElementById('backtotop');

toTopImg.onclick = function backToTop() {
    // scroll to top
    var scroll = setInterval(function() {
        window.scrollBy(0, -150);
        if (!(document.documentElement.scrollTop||document.body.scrollTop)) {
            // reach top
            clearInterval(scroll);
        }
    }, 10);
}
