var carousel = document.querySelector(".carousel");
var firstCardWidth = carousel.querySelector(".testimonials").offsetWidth;
var arrowBtns = document.querySelectorAll(".carousel i");

// arrowBtns.forEach((btn) => {
//   btn.addEventListener("click", () => {
//     carousel.scrollLeft += btn.id == "left" ? -firstCardWidth : firstCardWidth;
//   });
// });


// var carouselTwo = document.querySelector(".carousel-two");
// var plansCardWidth = carouselTwo.querySelector(".plans").offsetWidth;
// var arrowBtnsTwo = document.querySelectorAll(".carousel-two i");

// arrowBtnsTwo.forEach((btn) => {
//   btn.addEventListener("click", () => {
//     carouselTwo.scrollLeft +=
//       btn.id == "left" ? -plansCardWidth : plansCardWidth;
//   });
// });

// FAQ's

var accordionItemHeaders2 = document.querySelectorAll(
  ".accordion-item-header"
);

accordionItemHeaders2.forEach((accordionItemHeader) => {
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
      accordionItemBody.style.maxHeight = accordionItemBody.scrollHeight + "px";
    } else {
      accordionItemBody.style.maxHeight = 0;
    }
  });
});


