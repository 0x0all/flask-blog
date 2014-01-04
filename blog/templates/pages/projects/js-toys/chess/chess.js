var NUM = Number(prompt('size?'));
var TOTAL = NUM * NUM;
var arr = new Array();
var steps = 0;

function body_onload() {
    var square = document.createElement("input");
    square.type = "submit";
    square.className = "square";
    square.style.backgroundColor = 'white';
    square.value = ' ';
    var br = document.createElement('br');
    var brr = new Array();

    for (var i = 0; i < TOTAL; i++){
        arr[i] = square.cloneNode(true);
        arr[i].onclick = buttonClick;
        document.body.appendChild(arr[i]);
        if ((i + 1) % NUM == 0){
            brr[i] = br.cloneNode(true);
            document.body.appendChild(brr[i]);
        }
    }
}

 
function buttonClick(){
    var index ;
    for (index = 0; index < TOTAL; index++){
        if (arr[index] == this)
            break;
    }
    var temp = index + 1;
    var top, bottom, left, right;
    temp - NUM <= 0 ? top = undefined : top = arr[index - NUM];
    temp + NUM > TOTAL ? bottom = undefined : bottom = arr[index + NUM];
    temp % NUM == 1 ? left = undefined : left = arr[index - 1];
    temp % NUM == 0 ? right = undefined : right = arr[index + 1];
    targets = [top, bottom, left, right];
    for (var k = 0; k < targets.length; k++){
        if (targets[k] != undefined)
            targets[k].style.backgroundColor == 'white' ? targets[k].style.backgroundColor = 'black' : targets[k].style.backgroundColor = 'white';
    }
    steps += 1;
    document.getElementById('step').innerHTML = steps + ' steps';
    if (checkResult()){
        alert('Congratrulations!!\nIt took you ' + steps + ' steps!!');
        location.reload();
    }
}


function checkResult(){
    for (var i = 0; i < TOTAL; i++){
        if (arr[i].style.backgroundColor == 'white'){
            return false;
        }
    }
    return true;
}
