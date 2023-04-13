window.addEventListener('scroll', () => {
  const navbar = document.getElementById('navbar');
  if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
  } else {
      navbar.classList.remove('scrolled');
  }
});
// ---------------------------------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', function() {
  const navbar = document.getElementById('navbar');
  const navLinks = document.querySelectorAll('.nav-link');
  const navbarBrand = document.querySelector('.navbar-brand');
  
  navbarBrand.addEventListener('mouseenter', function() {
    navbarBrand.classList.add('fa-shake');
  });
  
  navbarBrand.addEventListener('mouseleave', function() {
    navbarBrand.classList.remove('fa-shake');
  })

  navLinks.forEach(link => {
      link.addEventListener('mouseover', () => {
          link.style.color = '#fff';
          link.classList.add('fa-bounce');
      });

      link.addEventListener('mouseout', () => {
          link.style.color = '';
          link.classList.remove('fa-bounce');
      });
  });

  window.addEventListener('scroll', () => {
      if (window.pageYOffset > 50) {
          navbar.classList.add('scrolled');
      } else {
          navbar.classList.remove('scrolled');
      }
  });
});
