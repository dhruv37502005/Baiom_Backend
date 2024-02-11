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
var splide = new Splide( '.splide', {
  perPage: 3,
  perMove: 1,
  gap    : '7rem',
  padding : '1rem',
  autowidth: 'true',
  type: 'loop',
  drag: 'free',
  snap: true,
  pagination : true,
 
  breakpoints: {
  640: {
      perPage: 2,
      gap    : '.7rem',
      // height:'6rem',
      
  },
  480: {
      perPage: 1,
      gap    : '.7rem',
      // height:'6rem',
     
  },
  },
} );

splide.mount();
