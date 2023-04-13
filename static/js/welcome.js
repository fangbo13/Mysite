$(function() {
    $('#show-more').click(function() {
      $('.about-me').toggleClass('expanded');
      $(this).toggleClass('btn-secondary btn-primary');
      if ($(this).hasClass('btn-secondary')) {
        $(this).html('Show less');
      } else {
        $(this).html('Show more');
      }
    });
  });