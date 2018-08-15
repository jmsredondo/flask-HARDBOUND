
$(document).ready(function() {

$.ajax({
        url: 'list',
        dataType: 'JSON',
        success: function (data) {
            $userTable = $('#userlist');
           console.log(data);
                $userTable.DataTable({
                    //url: 'viewlist',
                        data: data,
                    columns: [{
                            "data": "username",
                            "title":"Username"
                        },
                        {"data" : "firstname",
                        "title": 'First Name'
                        },
                        {"data" : "lastname",
                        "title": 'Last Name'
                        },
                        {"data" : "email",
                        "title": 'Email'
                        },
                        {"data" : "balance",
                        "title": 'Balance'
                        },
                        {"data" : "phone",
                        "title": 'Phone'
                        },],


    });
      }
     });

});