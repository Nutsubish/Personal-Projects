

function  me(){
   link = "https://www.facebook.com/nikoloz.nutsubidze.90"
   window.open(link, '_blank')
}


let Home = document.getElementById("Home");
let About = document.getElementById("About");
let Images = document.getElementById("Images");
let btn = document.getElementById("Btn")


function goto(sectionId) {
  const section = document.getElementById(sectionId);
  section.scrollIntoView({ behavior: 'smooth' });
}

About.addEventListener("click", function() {
  goto("AboutSec"); 
});

Images.addEventListener("click", function() {
  goto("Imagessec"); 
});

btn.addEventListener("click",function(){
   goto("navbar")
})

Home.addEventListener("click",function(){
   goto("navbar")
})

function ando(){
  link2 = "https://ibb.co/5RMbCcc"
  window.open(link2,'_blank')
}