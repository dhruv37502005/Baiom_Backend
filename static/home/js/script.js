$(document).ready(function() {
    $("#phone").intlTelInput({
      separateDialCode: true,
    });
  });
  
  function generateOTP() {
  var phoneNumber = $("#phone").intlTelInput("getNumber");
  var appointmentDate = $("#date").val();
  $('#genOtpBtn').css("display","none")
  $('#resendOtp').css("display","block")
  $("#otp-section").show();
  $("#bookBtn").show();
  }
  var lastScrollTop = 0;
  var navbar = document.getElementById('navbar');
  var dropdown = document.querySelectorAll('.dropdown-menu');
  window.addEventListener("scroll", function () {
    var scrollTop = window.scrollY || document.documentElement.scrollTop;
  
    if (scrollTop > lastScrollTop) {
      navbar.style.top = '-200px';
      dropdown.forEach(function(menu) {
        menu.style.top = '-200px';
    });
    } else {
      navbar.style.top = '0';
      dropdown.forEach(function(menu) {
        menu.style.top = '65px';
    });
  
    }
    lastScrollTop = scrollTop;
  });
  
  
  
  $('.carousel').carousel({
    interval: 7000
  })
  
  
  // Javascript for tab
  
  $(window).bind('load', function() {
      document.querySelector('#tab-1').classList.add('current-tab')
  });
  
  
  const tabItems = document.querySelectorAll('.tab-item');
  const tabContentItems = document.querySelectorAll('.tab-content-item');
  
  // Select tab content item
  function selectItem(e) {
      // Remove all show and border classes
      removecurrent();
      removeShow();
      // Add border to current tab item
      this.classList.add('current-tab');
      // Grab content item from DOM
      const tabContentItem = document.querySelector(`#${this.id}-content`);
      // Add show class
      tabContentItem.classList.add('show');
  }
  
  // Remove bottom borders from all tab items
  function removecurrent() {
      tabItems.forEach(item => {
          item.classList.remove('current-tab');
          
      });
  }
  
  // Remove show class from all content items
  function removeShow() {
      tabContentItems.forEach(item => {
          item.classList.remove('show');
      });
  }
  
  // Listen for tab item click
  tabItems.forEach(item => {
      item.addEventListener('click', selectItem);
  });
  
  function showTrainer(){
      document.querySelector('#virtues-tab-2 .fa').style.color="red"
      document.querySelector('#virtues-tab-1 .fa').style.color="white"
      document.querySelector('#virtues-tab-3 .fa').style.color="white"
      document.getElementById('virtues-tab-2-content').style.display="block";
      document.getElementById('virtues-tab-1-content').style.display="none";
      document.getElementById('virtues-tab-3-content').style.display="none";
  }
  function showFulltime(){
      document.querySelector('#virtues-tab-1 .fa').style.color="red"
      document.querySelector('#virtues-tab-2 .fa').style.color="white"
      document.querySelector('#virtues-tab-3 .fa').style.color="white"
      document.getElementById('virtues-tab-1-content').style.display="block";
      document.getElementById('virtues-tab-2-content').style.display="none";
      document.getElementById('virtues-tab-3-content').style.display="none";
  }
  function showEase(){
      document.querySelector('#virtues-tab-3 .fa').style.color="red"
      document.querySelector('#virtues-tab-1 .fa').style.color="white"
      document.querySelector('#virtues-tab-2 .fa').style.color="white"
      document.getElementById('virtues-tab-3-content').style.display="block";
      document.getElementById('virtues-tab-1-content').style.display="none";
      document.getElementById('virtues-tab-2-content').style.display="none";
  }
  
  const progressCircle = document.querySelector(".autoplay-progress svg");
  const progressContent = document.querySelector(".autoplay-progress span");
  var swiper = new Swiper(".mySwiperr", {
    
  
      slidesPerView: 3,
          // loop: true,
          grabCursor : true,
          spaceBetween: 20,
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