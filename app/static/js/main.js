
$(document).ready(function() {

    $userTable = $('#userlist');
    var username = $("#username");
    var uname = '';


    $("#search").click(function () {
    uname = username.val();
    if(uname.length !== 0)
    listurl = uname;

    var usertble =  $('#userlist').dataTable();
    usertble.fnFilter(listurl);

    init_userlist();
    console.log(listurl);
    //console.log(uname);
});

if (uname.length === 0)
    var listurl = 'viewlist';
    init_userlist();


function init_userlist() {
    var table = $userTable;
    $.ajax({
        url: listurl,
        dataType: 'JSON',
        success: function (data) {
            console.log(data);
          // $userTable.DataTable('refresh', {url: 'users/list'});
           table.DataTable({
                //retrieve: true,
                data: data,
                columns: [{
                    "data": "username",
                    "title": "Username"
                },
                    {
                        "data": "firstname",
                        "title": 'First Name'
                    },
                    {
                        "data": "lastname",
                        "title": 'Last Name'
                    },
                    {
                        "data": "email",
                        "title": 'Email'
                    },
                    {
                        "data": "balance",
                        "title": 'Balance'
                    },
                    {
                        "data": "phone",
                        "title": 'Phone'
                    },],

           });
        }
    });



}




});