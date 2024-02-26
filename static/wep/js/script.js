var carousel = document.querySelector(".carousel");
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




var accordionItemHeaders = document.querySelectorAll(".accordion-item-header");

accordionItemHeaders.forEach((accordionItemHeader) => {
  accordionItemHeader.addEventListener("click", () => {
    const isActive = accordionItemHeader.classList.contains("active");
    
    closeAllAccordionItems();

    if (!isActive) {
      accordionItemHeader.classList.add("active");
      const accordionItemBody = accordionItemHeader.nextElementSibling;
      accordionItemBody.style.maxHeight = accordionItemBody.scrollHeight + "px";
    }
  });
});

function closeAllAccordionItems() {
  const activeAccordionItemHeader = document.querySelector(".accordion-item-header.active");
  if (activeAccordionItemHeader) {
    activeAccordionItemHeader.classList.remove("active");
    activeAccordionItemHeader.nextElementSibling.style.maxHeight = 0;
  }
}

