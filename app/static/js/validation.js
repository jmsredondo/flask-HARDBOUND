$( "#userpost" ).validate({

});
    $('#register').click(function() {
        if($("#userpost").valid()) {
            userregister()
        }else {
            alert('incomplete information')
        }
    });
