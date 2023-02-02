function openNav() {
    document.getElementById("menu-sidebar").style.width = "250px";
  }
  function closeNav() {
    document.getElementById("menu-sidebar").style.width = "0";
  }
  
  let wordBtns = document.querySelectorAll(".word-btn");
  wordBtns.forEach(wordBtn => {
    wordBtn.addEventListener("click", function() {
      let number = this.id.split("-")[2];
      let wordContainer = document.querySelector("#word-container-" + number);
      wordContainer.style.display = "block";
    });
  });
  const closeButtons = document.querySelectorAll(".close-button");

  for (let i = 0; i < closeButtons.length; i++) {
    closeButtons[i].addEventListener("click", function() {
      const wordSection = this.parentNode;
      wordSection.style.display = "none";
    });
  }
  