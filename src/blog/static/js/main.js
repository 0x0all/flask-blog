window.onscroll = function() {
    // display: none if on top
    document.getElementById('backtotop').style.display = (document.body.scrollTop) ? 'block' : 'none';
}


var toTopImg = document.getElementById('backtotop');

toTopImg.onclick = function backToTop() {
    // scroll to top
    var scroll = setInterval(function() {
        window.scrollBy(0, -150);
        if (document.body.scrollTop === 0) {
            // reach top
            clearInterval(scroll);
        }
    }, 10);
}
