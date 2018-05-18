var options = {
    enableHighAccuracy: true,
    timeout: 10000, // milliseconds
    maximumAge: 0 // 0 = the device cannot use a cached position
};
var watchId = null;

$('#current').on('click', function () {
    if (!geolocation()) {
        return
    }
    navigator.geolocation.getCurrentPosition(
        function (pos) {success(pos, 'current')},
        function (err) {error(err)},
        options
    );
});

$('#watch').on('click', function () {
    if (!geolocation()) {
        return
    }
    watchId = navigator.geolocation.watchPosition(
        function (pos) {success(pos, 'watch')},
        function (err) {error(err)},
        options
    );
});

$('#clear').on('click', function () {
    clear();
    $('.message').html('Clear OK').animateCss('flash');
});

function geolocation() {
    clear();
    if (navigator.geolocation) {
        $('.message').html('Geolocation is available').animateCss('flash');
        return true
    } else {
        $('.message').html('Geolocation IS NOT available').animateCss('flash');
        return false
    }
}

function success(pos, method) {
    $('.latitude').html(pos.coords.latitude);
    $('.longitude').html(pos.coords.longitude);
    $('.altitude').html(pos.coords.altitude);
    $('.accuracy').html(pos.coords.accuracy);
    $('.altitudeAccuracy').html(pos.coords.altitudeAccuracy);
    $('.heading').html(pos.coords.heading);
    $('.speed').html(pos.coords.speed);
    $('.timestamp').html(pos.timestamp);
    switch(method)
    {
        case 'current':
        $('.message').html('Current OK').animateCss('flash');
        break;
        case 'watch':
        $('.message').html('Watch OK').animateCss('flash');
        break;
    }
}

function error(err) {
    switch(err.code)
    {
        case 1:
        $('.message').html('PERMISSION_DENIED').animateCss('flash');
        break;
        case 2:
        $('.message').html('POSITION_UNAVAILABLE').animateCss('flash');
        break;
        case 3:
        $('.message').html('TIMEOUT').animateCss('flash');
        break;
        $('.message').html(err.message).animateCss('flash');
        break;
    }
}

function clear() {
    $('.latitude').html('');
    $('.longitude').html('');
    $('.altitude').html('');
    $('.accuracy').html('');
    $('.altitudeAccuracy').html('');
    $('.heading').html('');
    $('.speed').html('');
    $('.timestamp').html('');
    if (watchId) {
        navigator.geolocation.clearWatch(watchId);
        watchId = null;
    }
}

$.fn.extend({
    animateCss: function (animationName) {
        var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
        this.addClass('animated ' + animationName).one(animationEnd, function() {
            $(this).removeClass('animated ' + animationName);
        });
    }
});
