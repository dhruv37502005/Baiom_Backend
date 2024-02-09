
  // Target the element with the "cir" class
  const cirElement = document.querySelector('.cir');

  // GSAP animation
  gsap.from(cirElement, {
    duration: 2,
    top: '-80%',
    left: '-48%',
    ease: 'power2.out',
  });

  const cirElementOne = document.querySelector('.cir2');

  // GSAP animation
  gsap.from(cirElementOne, {
    duration: 2,
    top: '80%',
    left: '85%',
    ease: 'power2.out',
  });