const carousel = document.querySelector(".carousel");
const firstCardWidth = carousel.querySelector(".testimonials").offsetWidth;
const arrowBtns = document.querySelectorAll(".carousel i");

arrowBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    carousel.scrollLeft += btn.id == "left" ? -firstCardWidth : firstCardWidth;
  });
});


const carouselTwo = document.querySelector(".carousel-two");
const plansCardWidth = carouselTwo.querySelector(".plans").offsetWidth;
const arrowBtnsTwo = document.querySelectorAll(".carousel-two i");

arrowBtnsTwo.forEach((btn) => {
  btn.addEventListener("click", () => {
    carouselTwo.scrollLeft +=
      btn.id == "left" ? -plansCardWidth : plansCardWidth;
  });
});

// FAQ's

const accordionItemHeaders = document.querySelectorAll(
  ".accordion-item-header"
);

accordionItemHeaders.forEach((accordionItemHeader) => {
  accordionItemHeader.addEventListener("click", (event) => {
    const currentlyActiveAccordionItemHeader = document.querySelector(
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
    const accordionItemBody = accordionItemHeader.nextElementSibling;
    if (accordionItemHeader.classList.contains("active")) {
      accordionItemBody.style.maxHeight = accordionItemBody.scrollHeight + "px";
    } else {
      accordionItemBody.style.maxHeight = 0;
    }
  });
});
