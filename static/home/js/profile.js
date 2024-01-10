document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("profile-dropdown").style.display = "none";
  function profileButton() {
    if (document.getElementById("profile-dropdown").style.display != "none") {
      document.getElementById("profile-dropdown").style.display = "none";
    } else {
      document.getElementById("profile-dropdown").style.display = "revert";
    }
  }
  document
    .getElementById("profile-btn")
    .addEventListener("click", profileButton);
});
