const API_BASE =
window.location.hostname==="127.0.0.1" ||
window.location.hostname==="localhost"
?
"http://127.0.0.1:8000"
:
"https://cravewise-backend.onrender.com";

loadConditions();

document
.getElementById("conditionSearch")
.addEventListener("input",function(){

const text=this.value.toLowerCase();

document
.querySelectorAll("#conditions label")
.forEach(label=>{

label.style.display=
label.textContent
.toLowerCase()
.includes(text)
?
"block"
:
"none";

});

});

if(localStorage.getItem("token")){

document.getElementById("loginModal").style.display="none";

}
