$("path, circle").hover(function(e) {
  $('#info-box').css('display','block');
  $('#info-box').html('<div>' + $(this).data('name') + '</div>');
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

  $(window).scrollTop(0);

  $('#info-box').css('display','block');
  $('#info-box').html('<div>' + $("#coffee-" + name + ' circle').data('name') + '</div>');

  var bbox = $("#coffee-" + name)[0].getBoundingClientRect();

  $('#info-box').css('top', bbox.top-154);
  $('#info-box').css('left', bbox.left);

  $('.whatabout').hide();
  $(whatabout).show('slow');
});

$('.whatabout-back').click(function(e) {
  $('#info-box').css('display','none');

  $('.whatabout').hide();
  $('#whatabout-link-list').show();
});

$(document).mousemove(function(e) {
  var bbox = $("#map")[0].getBoundingClientRect();

  if (e.pageX > bbox.left && e.pageX < bbox.right &&
      e.pageY > bbox.top && e.pageY < bbox.bottom) {
    $('#info-box').css('top', e.pageY-154);
    $('#info-box').css('left', e.pageX+8);
  }
}).mouseover();
