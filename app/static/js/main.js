
$(document).ready(function() {

  // url path
var windowurl = window.location.pathname;

switch (windowurl) {
    case '/books':
        init_getbooks();
        break;
    case '/genres':
       init_getgenres();
        break;
    case '/users/list':
        init_userlist();
        break;
    case '/bookbyid':
        getbookbyid();
        break;
    case '/user':
        getbyusername();
        break;
    case '/genrebyid':
        getgenrebyid();
        break;
    case 6:
        day = "Saturday";
}
// all functions

//retrieve all book genres

    function init_getgenres() {

        var $genretable = $("#genretbody");
        var genretbody = [];

        $.ajax({
        url: 'genre',
        dataType: 'JSON',
        success: function (data) {
            console.log(data);

            for(var i =0; i <= data.length-1; i++){
           // genre += "<h1>Genre(For udpate)</h1>";
            genretbody += "<tr>"+
                                "<td hidden>"+data[i].genre_id+"</td>"+
                              "<td>"+data[i].type+"</td>"+
                              "<td>"+data[i].genre+"</td>"+
                              "<td><form method=\"delete\" action=\"/genre"+"/"+data[i].genre_id+"\">" +
                "<button type=\"submit\" class=\"btn btn-danger\">Delete</button></form>" +
                "<form method=\"get\" action=\"/genre/addbook"+"/"+data[i].genre_id+"\">" +
                "<button type=\"submit\" class=\"btn btn-warning\">Add Book</button></form></td>"+
                            "</tr>";

            }
            $genretable.html(genretbody);
           // $genrecontainer.html(genre);
        }
    });

    }

    // get value of row and store in local storage for later use
$genreTable = $('#genretable');
var gentable = $genreTable;
$genreTable.on('click', 'tbody tr', function() {
 var tableData = $(this).children("td").map(function() {
        return $(this).text();
    }).get();
 var genreid= tableData[0];
    localStorage.setItem('genreid', genreid);
    document.location.href = ('/genrebyid');
});
function getgenrebyid() {

     var genre_id = localStorage.getItem('genreid');
        var divtable = [];
        $genrebyid = $('#getgenrebydtbody');
        $.ajax({
            url: 'genre/' + genre_id,
            dataType: 'JSON',
            success: function (data) {
                console.log(data);
                for(var i =0; i <= data.length-1; i++) {
                   divtable += "<tr>"+
                              "<td>"+data[i].genre_id+"</td>"+
                              "<td>"+data[i].type+"</td>"+
                       "<td>"+data[i].genre+"</td>"+
                            "</tr>";
                }
                $genrebyid.html(divtable)
            }
        });
}
// retrieve all books all books
function init_getbooks() {
    var $listbook = $("#listbook");
//var $genrecontainer = $("#genre"); temporary
    var div = [];
//var genre = []; temporary
    $.ajax({
        url: 'book',
        dataType: 'JSON',
        success: function (data) {
            console.log(data);

            for (var i = 0; i <= data.length - 1; i++) {

                // genre += "<h1>Genre(For udpate)</h1>";
                div += "<div class=\"row bg-white has-shadow\">" +
                    "<div class=\"left-col col-lg-6 d-flex align-items-center justify-content-between\">" +
                    "<div class=\"project-title d-flex align-items-center\">" +
                    "<div class=\"image has-shadow\"><img src=\"static/img/hp6.jpg \" style=\"height: 110%; width: 100%;\" alt=\"...\" class=\"img-fluid\"></div>" +
                    "<div class=\"text\">" +
                    "<input type='hidden' class='bidclass' value="+data[i].book_id+">"+
                    "<a href='bookbyid' class='bookid'><h2>" + data[i].title + "</h2></a>" +
                    "<i>" + data[i].author + "</i>" +
                    "</div>" +
                    "</div>" +
                    "</div>" +
                    "<div class=\"right-col col-lg-4 d-flex align-items-center\">" +
                    "<div class=\"desc\">" + data[i].description + "</div>" +
                    "</div>" +
                    "<div class=\"right-col col-lg-2 d-flex align-items-center\">" +
                    "<form method=\"post\" action=\"/library\"><input name = \"book\" type=\"hidden\" value= " + data[i].book_id + ">" +
                    "<button type=\"submit\" class=\"btn btn-warning\">Add book</button></form>" +
                    "<form method=\"delete\"  action=\"/book" + "/" + data[i].book_id + "\">" +
                    "<button type=\"submit\" class=\"btn btn-danger\">Delete</button></form>" +
                    "</div>" +
                    "</div>";
            }
            $listbook.html(div);
            // $genrecontainer.html(genre);

        }
    });

}
// get value of row and store in local storage for later use
$(document).on('click', '.bookid', function() {

    var div = $(this).closest('div');
    var bookid = (div.find('input').val());
    localStorage.setItem('bid', bookid);

});


  //get book by id
    function getbookbyid() {
    var book_id = localStorage.getItem('bid');
        var divtable = [];
        $bookbyid = $('#getbookbyidtable');
        $.ajax({
            url: 'book/' + book_id,
            dataType: 'JSON',
            success: function (data) {
                console.log(data);
                for(var i =0; i <= data.length-1; i++) {
                   divtable += "<tr>"+
                              "<td>"+data[i].book_id+"</td>"+
                              "<td>"+data[i].title+"</td>"+
                       "<td>"+data[i].description+"</td>"+
                       "<td>"+data[i].author+"</td>"+
                            "</tr>";
                }
                $bookbyid.html(divtable)
            }
        });
    }
    /*function getbyusername()
    {

        var uname = '';
        var listurl = 'viewlist';

        $("#search").click(function () {
            var username = $("#username");
            uname = username.val();
            listurl = uname;
            init_userlist(listurl);

            var usertble = $('#userlist').dataTable();
             usertble.fnFilter(listurl);
        });

        if(uname.length === 0){
            init_userlist(listurl)
        }
    }*/
function init_userlist() {
    $userTable = $('#userlist');
    var table = $userTable;

        $.ajax({
            url: '/users',
            dataType: 'JSON',
            success: function (data) {
                console.log(data);
                // $userTable.DataTable('refresh', {url: 'users/list'});
                table.DataTable({
                    retrieve: true,
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
// get value of row and store in local storage for later use
$userTable = $('#userlist');
var table = $userTable;
$userTable.on('click', 'tbody tr', function() {

  console.log('API row values : ', table.DataTable().row(this).data());
  var data = table.DataTable().row(this).data();
      var  username =data['username'];
      
    localStorage.setItem('username', username);
    document.location.href = ('/user');
});
// get user detail by username
function getbyusername() {
     var username = localStorage.getItem('username');
        var divtable = [];
        $userbyusername = $('#getusername');
        $.ajax({
            url: 'users/'+username,
            dataType: 'JSON',
            success: function (data) {
                console.log(data);
                for(var i =0; i <= data.length-1; i++) {
                   divtable += "<tr>"+
                              "<td>"+data[i].username+"</td>"+
                              "<td>"+data[i].firstname+"</td>"+
                       "<td>"+data[i].lastname+"</td>"+
                       "<td>"+data[i].email+"</td>"+
                        "<td>"+data[i].balance+"</td>"+
                        "<td>"+data[i].phone+"</td>"+
                            "</tr>";
                }
                $userbyusername.html(divtable)
            }
        });

}

});