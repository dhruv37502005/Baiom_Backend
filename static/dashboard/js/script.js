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
var closeForm = document.getElementById('close-details-section');
var activeHai = document.getElementsByClassName('activeHai');
var graduationYear = document.getElementById("graduation-year");
var education = document.getElementById("education");
var aside = document.getElementById("aside");
var main = document.getElementById("main");
var downArrow = document.getElementById("down-arrow");
var upArrow = document.getElementById("up-arrow");
var live_card=document.getElementById("live-card");
var live_close=document.getElementById("live-close");
var live_content=document.getElementById("live-content");



var gradYear = `<option selected disabled hidden>Graduation Year</option>`;
for (i = 1980; i < 2030; i++){
    gradYear+=`<option>${i}</option>`
}
graduationYear.innerHTML = gradYear;


const list=["Board of Intermediate","B-tech","MCA","Diploma"]
var degreeCourse = `<option selected disabled hidden>Education</option>`;
for (i =0; i < list.length; i++){
    degreeCourse+=`<option>${list[i]}</option>`
}
education.innerHTML = degreeCourse;


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


function addIcon() {

    var parent = document.getElementById("socialmedia-section");

    var div = document.createElement("div");
    div.classList.add('input-group');

    var firstChild = document.createElement("input");
    firstChild.placeholder="Social Media URL";
    firstChild.type = "text";
    
    var secondChild = document.createElement("button");
    secondChild.innerHTML = "&times;";
    secondChild.classList.add('cross-btn');

    secondChild.onclick= function(){
        parent.removeChild(div);
    };
    
    div.appendChild(firstChild);
    div.appendChild(secondChild);
    parent.appendChild(div);
};

downArrow.addEventListener("click", () => {
    aside.style.display = "revert";
    main.style.display = "none";
    downArrow.style.display = "none";
});

upArrow.addEventListener("click", () => {
    aside.style.display = "none";
    main.style.display = "revert";
    downArrow.style.display = "revert";
});

live_card.addEventListener("click", () => {
    if (live_content.style.display == "none") {

        live_content.style.display = "block";
    }
    else {
        
        live_content.style.display = "none";
    }
})
