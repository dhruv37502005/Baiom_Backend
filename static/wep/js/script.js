

var carousel = document.getElementById("testi");
var firstCardWidth = carousel.querySelector(".testimonials").offsetWidth;
var arrowBtns = document.querySelectorAll(".temp i");
// var popup_form = document.getElementById("popup-form");
// var I_am_interested = document.getElementById("button-one");
// var popup_close = document.getElementById("popup-close");

arrowBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    carousel.scrollLeft += btn.id == "left" ? -firstCardWidth : firstCardWidth;
  });
});


// var carouselTwo = document.querySelector(".carousel-two");
// var plansCardWidth = carouselTwo.querySelector(".plans").offsetWidth;
// var arrowBtnsTwo = document.querySelectorAll(".carousel-two i");

// arrowBtnsTwo.forEach((btn) => {
//   btn.addEventListener("click", () => {
//     carouselTwo.scrollLeft +=
//       btn.id == "left" ? -plansCardWidth : plansCardWidth;
//   });
// });

//popup form

// I_am_interested.addEventListener("click", () => {
//   popup_form.style.display = "revert";
//   // document.getElementById("container").style.opacity = "0.7";
// })

// popup_close.addEventListener("click", () => {
//   popup_form.style.display = "none";
// })

// popup_form.addEventListener("submit", (e) => {
//   e.preventDefault();
//   popup_form.style.display = "none";
// })


var splide = new Splide('.splide', {
  perPage: 3,
  perMove: 1,
  gap: '2rem',
  padding: '1rem',
  // autowidth: 'true',
  fixedWidth:'30%',
  type: 'loop',
  drag: 'free',
  snap: true,
  pagination: true,

  breakpoints: {
    640: {
      perPage: 2,
      gap: '.7rem',
      // height:'6rem',

    },
    480: {
      perPage: 1,
      gap: '.7rem',
      // height:'6rem',

    },
  },
});

splide.mount();

