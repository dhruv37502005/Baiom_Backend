// adding cross icon onclick in navbar
const scriptURL = ''

I

const form = document.forms['contact-form']

form.addEventListener('submit', e => {
e.preventDefault()

fetch(scriptURL, { method: 'POST', body: new FormData(form)})

// .then(response => alert("Thank you! your form is submitted successfully." )) .then(() => { window.location.reload(); })

.catch(error => console.error('Error!', error.message))

});

const navBartoggler = document.querySelector(".navbar-toggler")
const navIcon = document.querySelector(".navbar-toggler-icon")

navBartoggler.addEventListener('click',function(){
    // if(navIcon.classList.contains("navbar-toggler-icon")){
    //     navIcon.s("class","")

    // }
    // else{
    //     navIcon.setAttribute("class","navbar-toggler-icon")
    // }
    navIcon.classList.toggle("navbar-toggler-icon")
    navIcon.classList.toggle("fa-solid")
    navIcon.classList.toggle("fa-xmark")
})
// code end