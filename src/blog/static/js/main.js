window.onscroll = function() {
    document.getElementById('backtotop').style..display = (document.body.scrollTop) ? 'block' : 'none';
}

function backToTop() {
    var scroll = setInterval(function() {
        window.scrollBy(0, -40);
        if (document.body.scrollTop === 0) {
            clearInterval(scroll);
        }
    }, 1000);
}
