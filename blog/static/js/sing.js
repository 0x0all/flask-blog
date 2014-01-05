var canvas = document.createElement("canvas"); 
canvas.width = screen.availWidth;
canvas.height = screen.availHeight; 
var context = canvas.getContext("2d"); 

if (typeof webkitAudioContext !== undefined) {
    var audioCtx = new webkitAudioContext; 
} else {
    var audioCtx = new AudioContext; 
}
var oscillator = audioCtx.createOscillator();
var NoteFrq = [0, 262, 294, 330, 349, 392, 440, 494, 523]; 
var runId; 


function sing(e) {
    if (runId) {
        clearInterval(runId); 
    }
    var img = new Image(); 
    img.src = e.src; 
    img.onload = function() {
        context.drawImage(img, 0, 0); 
        var imgdata = context.getImageData(0, 0, img.width, img.height); 
        var i = 0; 
        runId = setInterval(function() {
            var r = imgdata.data[i]; 
            var g = imgdata.data[++i]; 
            var b = imgdata.data[++i]; 
            var a = imgdata.data[++i]; 
            var frq = NoteFrq[(r + g + b + a) % 8 + 1]; 
            oscillator.frequency.value = frq; 
            oscillator.connect(audioCtx.destination); 
            oscillator.noteOn(0); 
        }, 500); 
    }; 
}
