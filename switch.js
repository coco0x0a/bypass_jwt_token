$(function() {
    $('#signin-link').click(function(e) {
		$("#signin").delay(100).fadeIn(100);
 		$("#signup").fadeOut(100);
		$('#signup-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});
	$('#signup-link').click(function(e) {
		$("#signup").delay(100).fadeIn(100);
 		$("#signin").fadeOut(100);
		$('#signin-link').removeClass('active');
		$(this).addClass('active');
		e.preventDefault();
	});

});  
///
