
const progressCircle = document.querySelector(".autoplay-progress svg");
const progressContent = document.querySelector(".autoplay-progress span");
var swiper = new Swiper(".mySwiper", {
  

    slidesPerView: 3,
        // loop: true,
        grabCursor : true,
        spaceBetween: 30,
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
        pagination: {
          el: ".swiper-pagination",
          clickable: true
        },
        breakpoints: {
          0: {
            slidesPerView: 1,
          },
          550: {
            slidesPerView: 1,
          },
          850: {
            slidesPerView: 2,
            // width:50,
          },
          1200: {
            slidesPerView: 3,
          },
          1300: {
            slidesPerView: 3,
          },
        },
      });

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


    