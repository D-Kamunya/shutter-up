
$(document).ready(function(){

  baguetteBox.run('.demoo', {
    captions: true, // display image captions.
    buttons: 'auto', // arrows navigation
    fullScreen: false,
    noScrollbars: false,
    bodyClass: 'baguetteBox-open',
    titleTag: false,
    async: false,
    preload: 2,
    animation: 'slideIn', // fadeIn or slideIn
    verlayBackgroundColor: 'rgba(0,0,0,.8)'
  });
  $(function() {
    $('button.navbar-toggler').click(function() {
      var value = $('.content').css('padding-top');
      if (value === '120px') {
        $('.content').css('padding-top', '+=195');
      } else {
        $('.content').css('padding-top', '120px');
      }
    });
  });
});
    