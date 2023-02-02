var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var particles = [];
for (var i = 0; i < 100; i++) {
   particles.push({
     x: Math.random() * canvas.width,
     y: Math.random() * canvas.height,
     size: Math.random() * 3 + 1,
     color: "rgba(" + Math.floor(Math.random() * 255) + ", " + Math.floor(Math.random() * 255) + ", " + Math.floor(Math.random() * 1000) + ", 0.8)",
     speedX: Math.random() * 5 - 2.5,
     speedY: Math.random() * 5 - 2.5
   });
}

function animate() {
   requestAnimationFrame(animate);
  
   ctx.clearRect(0, 0, canvas.width, canvas.height);
  
   for (var i = 0; i < particles.length; i++) {
     var p = particles[i];
    
     ctx.beginPath();
     ctx.arc(p.x, p.y, p.size, 0, 2 * Math.PI);
     ctx.fillStyle = p.color;
     ctx.fill();
    
     p.x += p.speedX;
     p.y += p.speedY;
    
     if (p.x > canvas.width) p.x = 0;
     if (p.x < 0) p.x = canvas.width;
     if (p.y > canvas.height) p.y = 0;
     if (p.y < 0) p.y = canvas.height;
   }
}

animate();

function changeColor(){
  // an array of possible button colors
  const buttonColors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

  // select a random color from the array
  const randomColor = buttonColors[Math.floor(Math.random() * buttonColors.length)];

  // select the login button
  const loginButton = document.querySelector("button");

  // apply the randomly selected color to the button
  loginButton.style.backgroundColor = randomColor;
}

changeColor();
window.onload = changeColor;
