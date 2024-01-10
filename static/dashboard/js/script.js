document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("form-section").style.display = "none";

  //edit details button
  document.getElementById("edit-details").addEventListener("click", () => {
      
      document.getElementById("form-section").style.display = "block";
      document.getElementById("blackshadow").style.display="block";
  })

  //close details button
  document.getElementById("close-details").addEventListener("click", () => {
      
      document.getElementById("form-section").style.display = "none";
      document.getElementById("blackshadow").style.display="none";

     
  })

  //for media queries:up arrow to display main contain 
  document.querySelector(".links .down").addEventListener("click", () => {
      document.getElementById("aside").style.display = "none";
      document.querySelector(".main .down").style.display = "flex";

  })

  //for media queries:down arrow to display aside contain 
  document.querySelector(".main .down").addEventListener("click", () => {
      document.getElementById("aside").style.display = "block";
      document.querySelector(".main .down").style.display = "none";

  })

  
})