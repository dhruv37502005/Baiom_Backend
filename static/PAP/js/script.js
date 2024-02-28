var swiper = new Swiper('.blog-slider', {
    spaceBetween: 30,
    effect: 'fade',
    loop: true,
    mousewheel: {
      invert: false,
    },
    // autoHeight: true,
    pagination: {
      el: '.blog-slider__pagination',
      clickable: true,
    }
});
  
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