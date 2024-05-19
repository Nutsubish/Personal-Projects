let i = 0;
let txt = '"There is no end, only new beginnings"- Nikoloz Nutsubidze'
let speed = 100; 

function typeWriter() {
    if (i < txt.length) {
        document.getElementById("demo").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    } else {
        i = 0;
        document.getElementById("demo").innerHTML = '';
      
        setTimeout(typeWriter, speed);
    }
}

window.onload = function () {
    typeWriter();
};




let dc = document.getElementById("dc");
let fbook = document.getElementById("facebook");

dc.addEventListener("click",function(){
  linked = "https://github.com/Nutsubish"
  window.open(linked,'blank_')
});
fbook.addEventListener("click",function(){
  linked1 = "https://www.facebook.com/nikoloz.nutsubidze.90"
  window.open(linked1,'blank_')
})



let Home = document.getElementById("Home");
let About = document.getElementById("About");
let Contact = document.getElementById("Contact");


function goto(sectionId) {
    const section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
  }
  
  About.addEventListener("click", function() {
    goto("Abouth"); 
  });
  
  Contact.addEventListener("click", function() {
    goto("Contacth"); 
  });



let btn = document.getElementById("btnN")
btn.addEventListener("click",function(){
  goto("navbar")
})




let myimg = document.getElementById("img")
myimg.addEventListener("click",function(){
  linkofmy = "https://www.facebook.com/nikoloz.nutsubidze.90/"
  window.open(linkofmy,'blank_')
})




//https://www.facebook.com/nika11keshelava/

let JS = document.getElementById("Js1")
JS.addEventListener("click",function(){
  jslink = "https://www.simplilearn.com/applications-of-javascript-article"
  window.open(jslink, 'blank_')
});





let html = document.getElementById("html1")
html.addEventListener("click",function(){
  htmllink = "https://www.geeksforgeeks.org/uses-of-html/"
  window.open(htmllink, 'blank_')
});





let css = document.getElementById("css1")
css.addEventListener("click",function(){
  csslink = "https://medium.com/@paulohfev/css-best-practices-you-should-know-374c388a00dd"
  window.open(csslink, 'blank_')
});






let py = document.getElementById("py1")
py.addEventListener("click",function(){
  pylink = "https://www.simplilearn.com/what-is-python-used-for-article"
  window.open(pylink, 'blank_')
});

document.addEventListener(function() {
  let form = document.getElementById("myForm");

  form.addEventListener("submit", function(event) {

    event.preventDefault();


  });
});