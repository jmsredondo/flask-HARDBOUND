function userregister() {
    var data = $('#userpost').serialize();
    console.log(data);
    $.ajax({
        url: '/users',
        data: data,
        method: 'POST',
        dataType: 'JSON',
        success: function (data) {
            console.log(data)
            document.location.href = ('/users/list');
        }
    });

}