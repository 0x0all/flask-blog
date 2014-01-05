var canvas = document.getElementById("playground"); 
var context = canvas.getContext("2d");
context.canvas.width = window.screen.availWidth * 0.9; 
context.canvas.height = window.screen.availHeight * 0.8; 

var N = 0, angle = 0, runId; 
var boxX = 0, boxY = 0; 
var playWidth = canvas.width * 0.6; 
var playHeight = canvas.height * 0.3; 
var upperX = canvas.width * 0.2; 
var upperY = canvas.height * 0.3; 
var lowerY = upperY + playHeight; 

start(); 

function draw(N, doit) {
    var currLevel = Levels[N]; 
    if (!currLevel)
        return false; 

    // draw background 
    var bgcolor = currLevel["bgcolor"]; 
    context.fillStyle = bgcolor; 
    context.fillRect(upperX, upperY, playWidth, playHeight);    

    // draw static bars
    var barcolor = currLevel["barcolor"]; 
    context.fillStyle = barcolor; 
    for (var i = 0; i < currLevel["bars"].length; ++ i) {
        var bar = currLevel["bars"][i]; 
        var h = bar["height"] * playHeight; 
        var w = bar["width"] * box; 
        var x = bar["to-left"] * playWidth + upperX; 
        var y = bar["to-horizon"] < 0 ? upperY : upperY + playHeight * (1 - bar["to-horizon"]); 
        context.fillRect(x, y, w, h); 
    }

    doit(); 
}

function run() {
    // draw moving box 
    boxY = lowerY - box; 
    context.fillRect(upperX+boxX, boxY, box, box); 
    boxX += 2 ; 
    if (boxX+box >= playWidth) {
        clearInterval(runId);
        start(); 
    }
}

function jump(e) {
    if (e.keyCode === 32) {
        clearInterval(runId);
        runId = setInterval(function() { 
            draw(N, jumpUp); 
        }, 10); 
    }
}

function jumpUp() {
    window.removeEventListener("keypress", arguments.callee, false); 
    context.save(); 
    context.translate(upperX+boxX+box/2, boxY+box/2); 
    context.rotate(angle*Math.PI/180); 
    context.fillRect(-box/2, -box/2, box, box); 
    context.restore(); 
    boxX += 2; 
    boxY -= 2; 
    angle += 3; 
    if (boxX+box >= playWidth) {
        clearInterval(runId);
        start(); 
    }
    if (boxY + box * 4 === lowerY) {
        clearInterval(runId);
        runId = setInterval(function() { 
            draw(N, jumpDown); 
        }, 10); 
    }
}

function jumpDown() {
    context.save(); 
    context.translate(upperX+boxX+box/2, boxY+box/2); 
    context.rotate(angle*Math.PI/180); 
    context.fillRect(-box/2, -box/2, box, box); 
    context.restore(); 
    boxX += 2; 
    boxY += 2; 
    angle += 3; 
    if (boxX+box >= playWidth) {
        clearInterval(runId);
        start(); 
    }
    if (boxY + box === lowerY) {
        clearInterval(runId);
        runId = setInterval(function() { 
            draw(N, run); 
        }, 10); 
    }
}

function start() {
    N = 0, angle = 0, runId; 
    boxX = 0, boxY = 0; 
    playWidth = canvas.width * 0.6; 
    playHeight = canvas.height * 0.3; 
    upperX = canvas.width * 0.2; 
    upperY = canvas.height * 0.3; 
    lowerY = upperY + playHeight; 

    window.addEventListener("keypress", jump, false); 
    runId = setInterval(function() { draw(N, run); }, 10); 
}

