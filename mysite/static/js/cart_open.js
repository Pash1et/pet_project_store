document.getElementById('button').onmouseover = function() {
    if(document.getElementById('cart').style.visibility = 'hidden'){
        document.getElementById('cart').style.visibility = 'visible';
    }
 };

 document.getElementById('button').onmouseout = function() {
    if(document.getElementById('cart').style.visibility = 'visible'){
        document.getElementById('cart').style.visibility = 'hidden';
    }
 };
 