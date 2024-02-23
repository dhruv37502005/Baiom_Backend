document.addEventListener("DOMContentLoaded", () => {
 document.getElementById("profile-content").style.display = "none";
   function profileButton() {
     if (document.getElementById("profile-content").style.display != "none") {
       document.getElementById("profile-content").style.display = "none";
     } else {
       document.getElementById("profile-content").style.display = "revert";
     }
   }
   document
     .getElementById("profile-btn")
     .addEventListener("click", profileButton);
 });
