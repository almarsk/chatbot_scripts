document.addEventListener("DOMContentLoaded", function() {
  var delay = 2500;  // v milisekundách
  var loader = document.getElementById("loader");
  var odpik = document.getElementById("odpik");
  var chat_form = document.getElementById("chat-form");

  odpik.addEventListener("click", function(event) {
    event.preventDefault();
    loader.classList.remove("display-none");
    setTimeout(function() { chat_form.submit() }, delay);
  });
});
