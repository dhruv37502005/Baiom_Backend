// adding cross icon onclick in navbar
const navBartoggler = document.querySelector(".navbar-toggler")
const navIcon = document.querySelector(".navbar-toggler-icon")

navBartoggler.addEventListener('click',function(){
    // if(navIcon.classList.contains("navbar-toggler-icon")){
    //     navIcon.s("class","")

    // }
    // else{
    //     navIcon.setAttribute("class","navbar-toggler-icon")
    // }
    navIcon.classList.toggle("navbar-toggler-icon")
    navIcon.classList.toggle("fa-solid")
    navIcon.classList.toggle("fa-xmark")
})
// code end