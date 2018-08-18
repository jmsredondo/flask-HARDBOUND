
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
        getbyusername();
        break;
    case 3:
        day = "Wednesday";
        break;
    case 4:
        day = "Thursday";
        break;
    case 5:
        day = "Friday";
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

            for(var i =0; i <= data.length-1; i++){
           // genre += "<h1>Genre(For udpate)</h1>";
            div += "<div class=\"row bg-white has-shadow\">" +
                    "<div class=\"left-col col-lg-6 d-flex align-items-center justify-content-between\">"+
                      "<div class=\"project-title d-flex align-items-center\">"+
                        "<div class=\"image has-shadow\"><img src=\"static/img/hp6.jpg \" style=\"height: 110%; width: 100%;\" alt=\"...\" class=\"img-fluid\"></div>" +
                        "<div class=\"text\">" +
                          "<h2>"+data[i].title+"</h2>"+
                          "<i>"+data[i].author+"</i>"+
                        "</div>"+
                      "</div>"+
                      "</div>"+
                    "<div class=\"right-col col-lg-4 d-flex align-items-center\">"+
                      "<div class=\"desc\">"+data[i].description+"</div>"+
                    "</div>"+
                "<div class=\"right-col col-lg-2 d-flex align-items-center\">" +
                "<form method=\"post\" action=\"/library\"><input name = \"book\" type=\"hidden\" value= "+data[i].book_id+">" +
                "<button type=\"submit\" class=\"btn btn-warning\">Add book</button></form>"+
                "<form method=\"delete\" action=\"/book"+"/"+data[i].book_id+"\">" +
                "<button type=\"submit\" class=\"btn btn-danger\">Delete</button></form>"+
                      "</div>"+
                    "</div>";
            }
            $listbook.html(div);
           // $genrecontainer.html(genre);
        }
    });


    }

    function getbyusername()
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
    }
function init_userlist(listurl) {
    $userTable = $('#userlist');
    var table = $userTable;

        $.ajax({
            url: listurl,
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



});