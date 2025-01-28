adjustSize = () => {
  [...document.querySelectorAll('article.lvl')].forEach((card) => {
    card.style.width = `${document.querySelector('div.size-slider>input[type="range"]').value}%`;
  })
}

window.onload = () => {
  adjustSize();
}
document.querySelector('div.size-slider>input[type="range"]').addEventListener('change', (e) => {
  adjustSize();
})