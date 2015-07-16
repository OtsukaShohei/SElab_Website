$(function(){
    $(document).ready(function(){
	function getUrlParameter(sParam) {
	    var sPageURL = window.location.search.substring(1);
	    var sURLVariables = sPageURL.split('&');
	    for (var i = 0; i < sURLVariables.length; i++) {
		var sParameterName = sURLVariables[i].split('=');
		if (sParameterName[0] == sParam) {
		    return sParameterName[1];
		}
	    }
	};

	if (! getUrlParameter('lang') || getUrlParameter('lang') == 'jp') {
	    $('button#jp').addClass('active');
	    $('button#en').removeClass('active');
	    $('.en').hide();
	    $('.jp').show();
	} else if (getUrlParameter('lang') == 'en') {
	    $('button#en').addClass('active');
	    $('button#jp').removeClass('active');
	    $('.jp').hide();
	    $('.en').show();
	    $('a').each(function(){
		if ($(this).attr('href').search('\\?') == -1) {
		    $(this).attr('href', $(this).attr('href') + '?lang=en');
		}
	    });
	}

	$('button#jp').click(function(){
	    $('button#jp').addClass('active');
	    $('button#en').removeClass('active');
	    $('.en').hide();
	    $('.jp').show();
	    $('a').each(function(){
		$(this).attr('href', $(this).attr('href').replace(/\?lang=en$/, '').replace(/\&lang=en$/, ''));
	    });
	});

	$('button#en').click(function(){
	    $('button#en').addClass('active');
	    $('button#jp').removeClass('active');
	    $('.jp').hide();
	    $('.en').show();
	    $('a').each(function(){
		if ($(this).attr('href').search('\\?') == -1) {
		    $(this).attr('href', $(this).attr('href') + '?lang=en');
		}
	    });
	});
    });
});
