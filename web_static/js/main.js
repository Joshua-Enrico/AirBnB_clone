/*DARK MODE*/
var icon = document.getElementById("icon");

if(localStorage.getItem("theme") == null){
    localStorage.setItem("theme","light"); 
}


let localData = localStorage.getItem("theme");

if(localData == "light"){
    icon.src = "assets/img/sun-solid-84.png";
    document.body.classList.remove("dark-theme");
}else if(localData == "dark"){
    icon.src = "assets/img/moon-solid-84.png";
    document.body.classList.add("dark-theme");
}

icon.onclick = function(){
    document.body.classList.toggle("dark-theme");
    if(document.body.classList.contains("dark-theme")){
        icon.src = "assets/img/moon-solid-84.png";
        localStorage.setItem("theme","dark");
        }else{
            icon.src = "assets/img/sun-solid-84.png";
            localStorage.setItem("theme","light");
        }
}