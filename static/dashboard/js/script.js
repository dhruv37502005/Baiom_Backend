document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById("menuIcon");
    const sidebar = document.getElementById("sidebar");
  
    function toggleSidebar() {
        sidebar.style.display = sidebar.style.display === "none" ? "block" : "none";
    }
    menuIcon.addEventListener("click", toggleSidebar);
  });
  
  function closeSidebar() {
    const sidebar = document.getElementById("sidebar");
    const content = document.getElementById("content");
  
    sidebar.style.display = "none";
    content.style.width = "100%";
    content.style.left = "0";
  }
  function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const closebtn = document.getElementById("close");
    const sidebarWidth = 0; // Change this value to match your sidebar width
  
  
    sidebar.style.display = sidebar.style.display === "none" ? "block" : "none";
  
    if (sidebar.style.display === "none" && sidebar.style.left === '-250px') {
      sidebar.style.left = '0';
    } else {
        closebtn.style.display = "block";
        sidebar.style.left = `-${sidebarWidth}px`;
  
    }
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  //CONTENT FOR SIDEBAR
  window.onload = function() {
      document.getElementById('content1').style.display = 'block'; // Show content for Button 1 on page load
      hideAllContentExcept('content1'); // Hide other content initially
    };
    document.getElementById('line-1').addEventListener('click', function() {
      hideAllContentExcept('content1'); // Show content for Button 1
    });
  
    document.getElementById('line-2').addEventListener('click', function() {
      hideAllContentExcept('content2'); // Show content for Button 1
    });
    
    document.getElementById('line-3').addEventListener('click', function() {
      hideAllContentExcept('content3'); // Show content for Button 2
    });
    
    document.getElementById('line-4').addEventListener('click', function() {
      hideAllContentExcept('content4'); // Show content for Button 3
    });
    
    document.getElementById('line-5').addEventListener('click', function() {
      hideAllContentExcept('content5'); // Show content for Button 4
    });
    document.getElementById('line-6').addEventListener('click', function() {
      hideAllContentExcept('content6'); // Show content for Button 4
    });
    document.getElementById('line-7').addEventListener('click', function() {
      hideAllContentExcept('content7'); // Show content for Button 4
    });
    
    function hideAllContentExcept(contentId) {
      // Hide all content divs except the specified one
      document.getElementById('content1').style.display = contentId === 'content1' ? 'block' : 'none';
      document.getElementById('content2').style.display = contentId === 'content2' ? 'block' : 'none';
      document.getElementById('content3').style.display = contentId === 'content3' ? 'block' : 'none';
      document.getElementById('content4').style.display = contentId === 'content4' ? 'block' : 'none';
      document.getElementById('content5').style.display = contentId === 'content5' ? 'block' : 'none';
      document.getElementById('content6').style.display = contentId === 'content6' ? 'block' : 'none';
      document.getElementById('content7').style.display = contentId === 'content7' ? 'block' : 'none';
    }
    