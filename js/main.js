$("path, circle").hover(function(e) {
  $('#info-box').css('display','block');
  $('#info-box').html($(this).data('info'));
});

$("path, circle").mouseleave(function(e) {
  $('#info-box').css('display','none');
});

$("circle.coffee").click(function(e) {
  var id = $(this).parent('g').attr('id');
  var name = id.replace(/coffee-/, '');
  var whatabout = '#whatabout-' + name;

  $('.whatabout').hide();
  $(whatabout).show('slow');  
});

$(".whatabout-link").click(function(e) {
  var name = $(this).data('whatabout');
  var whatabout = '#whatabout-' + name;
  
  $('.whatabout').hide();
  $(whatabout).show('slow');  
});

$('.whatabout-back').click(function(e) {
  $('.whatabout').hide();
  $('#whatabout-link-list').show();
});

$(document).mousemove(function(e) {
  $('#info-box').css('top',e.pageY-$('#info-box').height()-30);
  $('#info-box').css('left',e.pageX-($('#info-box').width())/2);
}).mouseover();

var ios = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
if(ios) {
  $('a').on('click touchend', function() {
    var link = $(this).attr('href');
    window.open(link,'_blank');
    return false;
  });
}

$(document).ready(function() {
});
