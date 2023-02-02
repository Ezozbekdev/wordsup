$(".div-button").click(function(){
    $(".word-btn").not($(this).next(".word-container")).hide();
    $(this).next(".word-container").toggle();
  });
  