
  const sections = ['#home', '#about', '#resume', '#work', '#contact'];
  const navLinks = $('.nav-link-bg');

  function updateNavLinks() {
    let currentSection = null;

    sections.forEach((sectionId) => {
      const section = $(sectionId);
      const scrollTop = $(window).scrollTop();
      const sectionTop = section.offset().top - 100;

      if (scrollTop >= sectionTop) {
        currentSection = sectionId;
      }
    });

    navLinks.each((index, link) => {
      const linkHref = $(link).attr('href');
      if (linkHref === currentSection) {
        $(link).addClass('active');
      } else {
        $(link).removeClass('active');
      }
    });
  }

  $(window).on('scroll', updateNavLinks);

  // 初始化时更新一次
  updateNavLinks();