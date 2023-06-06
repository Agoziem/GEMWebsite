// let mybutton = document.getElementById("myBtn");
let navigationbar = document.getElementById("navigation");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    // mybutton.style.display = "block";
    navigationbar.style.backgroundColor = "white";
  } else {
    // mybutton.style.display = "none";
    navigationbar.style.backgroundColor = "";
  }
}

// When the user clicks on the button, scroll to the top of the document

// function topFunction() {
//   document.body.scrollTop = 0; // For Safari
//   document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
// }

const hamburgerMenu = document.querySelector('.hamburger-menu');
const menu = document.querySelector('.menu');
const menuLinks = document.querySelectorAll('.menulink');

// Toggle Hamburger Menu
hamburgerMenu.addEventListener('click', () => {
  hamburgerMenu.classList.toggle('active');
  menu.classList.toggle('active');
});

// Close Hamburger Menu on Link Click
menuLinks.forEach(link => {
  link.addEventListener('click', () => {
    hamburgerMenu.classList.remove('active');
    menu.classList.remove('active');
  });
});