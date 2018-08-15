
$(document).ready(function() {

$.ajax({
        url: 'list',
        dataType: 'JSON',
        success: function (data) {
            $userTable = $('#userlist');
                $userTable.DataTable({
                    url: 'users/viewlist',
                    columns: [{
                        field: 'balance',
                        title: 'Balance'
                    },{
                        field: 'email',
                        title: 'Username'
                    }, {
                        field: 'firstname',
                        title: 'First Name'
                    }, {
                        field: 'id',
                        title: 'Last Name'
                    }, {
                        field: 'email',
                        title: 'Email'
                    }, {
                        field: 'phonenumber',
                        title: 'Phone Number'
                    }]

    });
      }
     });

});