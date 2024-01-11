var profile = document.getElementById('profile');
var course = document.getElementById('course');
var certificate = document.getElementById('certificate');
var liveClasses = document.getElementById('liveClasses');
var profileDetails = document.getElementById('registered-details-section');
var formContent = document.getElementById('form-section');
var blackshadow = document.getElementById('blackshadow');
var CourseDetails = document.getElementById('courseDiv');
var certi_section = document.getElementById('certificate-section');
var live_section = document.getElementById('liveClasses-section');
var editDetails = document.getElementById('edit-details');
var closeForm = document.getElementById('close-details-section')
var activeHai = document.getElementsByClassName('activeHai')

editDetails.addEventListener('click',() => {
    formContent.style.display='block';
    blackshadow.style.display='block';
})
closeForm.addEventListener('click',() => {
    formContent.style.display='none'
    blackshadow.style.display='none';

})
profile.addEventListener('click' , () => {
    profileDetails.style.display = "block";
    CourseDetails.style.display = "none";
    certi_section.style.display = "none";
    live_section.style.display = "none";
    profile.classList.add("activeHai");
    course.classList.remove("activeHai");
    certificate.classList.remove("activeHai");
    liveClasses.classList.remove("activeHai");

});
course.addEventListener('click' , () => {
    profileDetails.style.display = "none";
    CourseDetails.style.display = "block";
    certi_section.style.display = "none";
    live_section.style.display = "none";
    profile.classList.remove("activeHai");
    course.classList.add("activeHai");
    certificate.classList.remove("activeHai");
    liveClasses.classList.remove("activeHai");

});
certificate.addEventListener('click' , () => {
    profileDetails.style.display = "none";
    CourseDetails.style.display = "none";
    certi_section.style.display = "block";
    live_section.style.display = "none";
    profile.classList.remove("activeHai");
    course.classList.remove("activeHai");
    certificate.classList.add("activeHai");
    liveClasses.classList.remove("activeHai");

});
liveClasses.addEventListener('click' , () => {
    profileDetails.style.display = "none";
    CourseDetails.style.display = "none";
    certi_section.style.display = "none";
    live_section.style.display = "block";
    profile.classList.remove("activeHai");
    course.classList.remove("activeHai");
    certificate.classList.remove("activeHai");
    liveClasses.classList.add("activeHai");

});
