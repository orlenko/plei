$(function() {

var stackSlides2 = function(curr, next, fwd) {
	// Because of the fx we use, we need all the slides
	// other than current and next to be invisible.

	var opts = this.opts();
    if ( !curr ) {
        curr = opts.slides[opts.currSlide];
        next = opts.slides[opts.nextSlide];
        fwd = !opts.reverse;
    }

    // reset the zIndex for the common case:
    // curr slide on top,  next slide beneath, and the rest in order to be shown
    $(curr).css('zIndex', opts.maxZ);

    var i;
    var z = opts.maxZ - 2;
    var len = opts.slideCount;
    if (fwd) {
        for ( i = opts.currSlide + 1; i < len; i++ )
            $( opts.slides[i] ).css( 'zIndex', z-- ).css('display', 'none');
        for ( i = 0; i < opts.currSlide; i++ )
            $( opts.slides[i] ).css( 'zIndex', z-- ).css('display', 'none');
    }
    else {
        for ( i = opts.currSlide - 1; i >= 0; i-- )
            $( opts.slides[i] ).css( 'zIndex', z-- ).css('display', 'none');
        for ( i = len - 1; i > opts.currSlide; i-- )
            $( opts.slides[i] ).css( 'zIndex', z-- ).css('display', 'none');
    }

    $(next).css('zIndex', opts.maxZ - 1).css('display', 'block');
}

$.fn.cycle.transitions.shuffleFromLeft = {
    before: function( opts, curr, next, fwd ) {
    	if (!opts.API.stackSlides2) {
    		opts.API.stackSlides2 = stackSlides2;
    	}
        opts.API.stackSlides2( curr, next, fwd );
        var w = opts.container.css('overflow','hidden').width();
        opts.cssBefore = { left: -w-20, top: 0, opacity: 1, display: 'block' };
        opts.cssAfter = { zIndex: opts._maxZ - 2, left: 0, display: 'none' };
        opts.animIn = { left: 0 };
        opts.animOut = { left: -w-20 };
    }
}


});