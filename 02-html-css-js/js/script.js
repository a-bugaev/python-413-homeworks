
document.getElementById("btn_change_corolortheme").addEventListener("click", function() {
  document.body.classList.toggle("dark-mode");
  document.getElementById("btn_change_corolortheme").innerHTML = document.body.classList.contains('dark-mode') ?
    '<img src="./img/light_icon.png" alt="icon of light mode"></img>'
  :
    '<img src="./img/dark_icon.png" alt="icon of dark mode"></img>'
})