window.onscroll = function() {
    document.getElementById('backtotop').style.display = (document.body.scrollTop) ? 'block' : 'none';
}


var toTopImg = document.getElementById('backtotop');

toTopImg.onclick = function backToTop() {
    var scroll = setInterval(function() {
        window.scrollBy(0, -150);
        if (document.body.scrollTop === 0) {
            clearInterval(scroll);
        }
    }, 10);
}

toTopImg.onmouseover = function wannaToTop() {
    toTopImg.style.backgroundColor = '#ffc19f';
}

toTopImg.onmouseout = function wannaToTop() {
    toTopImg.style.backgroundColor = '#ffffff';
}
