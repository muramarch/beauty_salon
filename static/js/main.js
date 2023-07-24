// При загрузке страницы вызываем функцию checkScroll
window.addEventListener('load', checkScroll);

// При прокрутке страницы вызываем функцию checkScroll
window.addEventListener('scroll', checkScroll);

function checkScroll() {
  const navbar = document.getElementById('navbar');

  // Если прокрутка больше 50 пикселей, добавляем класс "non-transparent", чтобы навбар стал непрозрачным
  if (window.scrollY > 50) {
    navbar.classList.add('non-transparent');
  } else {
    // Иначе удаляем класс "non-transparent", чтобы навбар стал прозрачным
    navbar.classList.remove('non-transparent');
  }
}
