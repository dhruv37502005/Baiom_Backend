

  // Target the element with the "cir" class
  const cirElement = document.querySelector('.cir');

  // GSAP animation
  gsap.from(cirElement, {
    duration: 2,
    top: '18%',
    left: '48%',
    ease: 'power2.out',
  });

  const cirElementOne = document.querySelector('.cir2');

  // GSAP animation
  gsap.from(cirElementOne, {
    duration: 2,
    top: '-15%',
    left: '-5%',
    ease: 'power2.out',
  });