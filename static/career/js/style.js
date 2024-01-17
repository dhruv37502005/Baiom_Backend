// Changing Svg position according to window width
const svg = document.querySelector("svg")

// window.addEventListener("resize",function (event){
//     const windowWidth = event.target.innerWidth
//     const difference = 1214 - windowWidth

//     if(difference > 0){
//         svg.style.top = "calc( -100% + " + (difference) + "px )";
//     }
// })

// adding cross icon onclick in navbar
const navBartoggler = document.querySelector(".navbar-toggler")
const navIcon = document.querySelector(".navbar-toggler-icon")

navBartoggler.addEventListener('click',function(){
    navIcon.classList.toggle("navbar-toggler-icon")
    navIcon.classList.toggle("fa-solid")
    navIcon.classList.toggle("fa-xmark")
})
// code end