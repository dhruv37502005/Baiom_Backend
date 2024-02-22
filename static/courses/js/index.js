

var popup_form = document.getElementById("popup-form");
var I_am_interested = document.getElementById("button-one");
var popup_close = document.getElementById("popup-close");
//popup form

I_am_interested.addEventListener("click", () => {
  popup_form.style.display = "revert";
  // document.getElementById("container").style.opacity = "0.7";
})

popup_close.addEventListener("click", () => {
  popup_form.style.display = "none";
})

// popup_form.addEventListener("submit", (e) => {
//   e.preventDefault();
//   popup_form.style.display = "none";
// })



// FAQ's

var accordionItemHeaders3 = document.querySelectorAll(
    ".accordion-item-header"
  );

  accordionItemHeaders3.forEach((accordionItemHeader) => {
    accordionItemHeader.addEventListener("click", (event) => {
      var currentlyActiveAccordionItemHeader = document.querySelector(
        ".accordion-item-header.active"
      );
      if (
        currentlyActiveAccordionItemHeader &&
        currentlyActiveAccordionItemHeader !== accordionItemHeader
      ) {
        currentlyActiveAccordionItemHeader.classList.toggle("active");
        currentlyActiveAccordionItemHeader.nextElementSibling.style.maxHeight = 0;
      }

      accordionItemHeader.classList.toggle("active");
      var accordionItemBody = accordionItemHeader.nextElementSibling;
      if (accordionItemHeader.classList.contains("active")) {
        accordionItemBody.style.maxHeight =
          accordionItemBody.scrollHeight + "px";
      } else {
        accordionItemBody.style.maxHeight = 0;
      }
    });
  });

// Testimonials

var swiper = new Swiper(".slide-content",{
  slidesPerView:3,
  spaceBetween: 30,
  loop:true,
  centerSlide:'true',
  fade:'true',
  grabCursor:'true',
  pagination:{
    el:".swiper-pagination",
    clickable:true,
    dynamicBullets:true,
  },
  navigation:{
    nextEl:".swiper-button-next",
    prevEl:".swiper-button-prev",
  },
  breakpoints:{
    0:{
      slidesPerView:1,
    },
    520:{
      slidesPerView:2,
    },
    950:{
      slidesPerView:3,
    },
  }
});

// right course 
  var splide = new Splide('.splide', {
    perPage: 3,
    perMove: 1,
    gap: '7rem',
    padding: '1rem',
    autowidth: true,
    type: 'loop',
    drag: 'free',
    snap: true,
    pagination: true,
    arrows: true,
    breakpoints: {
      1200: {
        perPage: 2,
        gap: '.7rem',
      },
      480: {
        perPage: 1,
        gap: '.7rem',
      },
    },
  }).mount();




