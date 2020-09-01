var btn = document.createElement("button");
btn.id = "btn";
btn.innerHTML = "0";
btn.style.background = "#4FFF8F";
btn.onclick = function () {
  btn.innerHTML = parseInt(btn.innerHTML) + 1;
};
document.body.appendChild(btn);

/*
css 
button { width: 96px; height:48px; font-size:24px;}
*/
/* 
html
<html>
    <head>
        <link rel="stylesheet" href="css/button.css" type="text/css">
    </head>
    
    <body>
    	<script src="js/button.js" type="text/javascript"></script>
    </body>
</html
*/
