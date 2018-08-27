
$(document).ready(function() {
//get genre by id



  // url path
var windowurl = window.location.pathname;

switch (windowurl) {
    case '/books':
         var bookname = '';
         var bookurl = 'book';

        $("#bookbtnsearch").click(function () {
            var buser = $("#booksearch");
            bookname = buser.val();
            bookurl = 'book/'+bookname;
            init_getbooks(bookurl);

        });
    $('#booksearch').on('input', function() {
        if ($.trim($('#booksearch').val()) === ''){
            init_getbooks('book')
        }
    });

        if(bookname.length === 0){
            init_getbooks(bookurl)
        }
        break;

    case '/genres':
        var genreid = '';
        var genreurl = 'genre';

        $("#genbtnsearch").click(function () {
            var genid = $("#gensearch");
            genreid = genid.val();
            genreurl = 'genre/'+genreid;
            init_getgenres(genreurl);

        });
    $('#gensearch').on('input', function() {
        if ($.trim($('#gensearch').val()) === ''){
            init_getgenres('genre')
        }
    });

        if(genreid.length === 0){
            init_getgenres(genreurl)
        }
        break;
    case '/users/list':
        var uname = '';
        var listurl = '/users';

        $("#namesearch").click(function () {
            var username = $("#username");
            uname = username.val();
            listurl = uname;
            init_userlist('/users/'+listurl);

        });
        $('#username').on('input', function() {
        if ($.trim($('#username').val()) === ''){
            init_userlist('/users')
        }
    });
        if(uname.length === 0){
            init_userlist(listurl)
        }
        break;
    case '/bookbyid':
        //getbookbyid();
       // if(getbookbyid()=== true) {
             getratings();
        //}

        break;
    case '/user':
        getbyusername();
        break;
    case '/genrebyid':
        getgenrebyid();
        break;
    case '/genre/addbookstogenre':
        displaybooksgenre();
        break;
    case '/libraries':
        getuserlibrary();

}
});

//open modal functions

function openModal(id,bookid) {
    console.log(bookid)
    console.log($('#' + id));
    $('#' + id).modal();
    $("#bookmodal").val(bookid);
    $("#yesbtn").click(function () {
        addbooktogenre();

    });
}
//for add book to library
function openModallib(id,bookid) {
    //console.log(id)
    console.log($('#' + id));
    $('#' + id).modal();
    $("#bookmodallib").val(bookid);

    $("#yesbtnlib").click(function () {
        addbooktolib();

    });
}
// open modal for delete genre
function openModaldelgenre(id,genreid,genre,type) {
    //console.log(id)
    console.log($('#' + id));
    $('#' + id).modal();
    $("#typedel").val(type);
    $("#genredel").val(genre);
    $("#iddel").val(genreid);
    $("#yesbtnlib").click(function () {
        deletegenre();

    });
}

// all functions

    //retrieve genre by id
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

    //retrieve all book genres
    function init_getgenres(gurl) {

        var $genretable = $("#genretbody");
        var genretbody = [];

        $.ajax({
        url: gurl,
        dataType: 'JSON',
        success: function (data) {
            console.log(data);

            for(var i =0; i <= data.length-1; i++){
                var getgenre = data[i].genre;
                var gettype = data[i].type;
                var getgenreid = data[i].genre_id;
           // genre += "<h1>Genre(For udpate)</h1>";
            genretbody += "<tr>"+
                                "<td hidden>"+data[i].genre_id+"</td>"+
                              "<td>"+data[i].type+"</td>"+
                              "<td>"+data[i].genre+"</td>"+
                              "<td>" +
                "<div class='row'>" +
                "<form method=\"delete\" action=\"/genre"+"/"+data[i].genre_id+"\">" +
                "<button type=\"button\" onclick=\"openModaldelgenre('deletegenre',"+data[i].genre_id+",'"+data[i].genre+"','"+data[i].type+"')\" class=\"btn btn-danger\">Delete</button></form>" +
                "<form method=\"get\" style=\"padding-left:2%\">" +
                "<button type=\"button\" onclick='getbooktogenre("+data[i].genre_id+")' class=\"btn btn-warning\">Add Book</button></form>" +
                "</div>" +
                "</td>"+
                            "</tr>";

            }
            $genretable.html(genretbody);
           // $genrecontainer.html(genre);
        }
    });

    }

    // onclcik store to id to local storage
    function getbooktogenre(gid){
        localStorage.setItem('gid', gid);
        document.location.href = ('/genre/addbookstogenre');

    }

    // get all books to add to genre
    function displaybooksgenre(){
          var genre_id = localStorage.getItem('gid');
          var $genrebooks = $("#genrebooks");
        var genrebooksbody = [];
          $.ajax({
        url: '/genre/getaddbook/'+ genre_id,
        dataType: 'JSON',
        success: function (data) {
            console.log(data);
             for(var i =0; i <= data.length-1; i++) {
                 genrebooksbody += '<div class="row bg-white has-shadow">' +
                     '<div class="left-col col-lg-6 d-flex align-items-center justify-content-between">' +
                     '<div class="project-title d-flex align-items-center">' +
                     '<div class="image has-shadow"><img src="/static/img/book.jpg " style="height: 100%; width: 100%;" alt="..." class="img-fluid"></div>' +
                     '<div class="text">' +
                     '<h2>'+data[i].title+'</h2>' +
                     '<i>'+data[i].author+'</i>' +
                     '</div>' +
                     '</div>' +
                     '</div>' +
                     '<div class="right-col col-lg-5 d-flex align-items-center">' +
                     '<div class="desc">'+data[i].description+'</div>' +
                     '</div>' +
                     '<div class="right-col col-lg-1 d-flex align-items-center">' +
                     '<form">' +
                     '<button type="button" class="btn btn-primary" onclick=openModal("confirmModal",'+data[i].book_id+')>Add Book to Genre</button>'+
                     '</form>' +
                     '</div>' +
                     '</div>';


             }
             $genrebooks.html(genrebooksbody);
        }
    });
}

    // retrieve all books all books
    function init_getbooks(bookurl) {
    var $listbook = $("#listbook");
//var $genrecontainer = $("#genre"); temporary
    var div = [];
//var genre = []; temporary
    $.ajax({
        url: bookurl,
        dataType: 'JSON',
        success: function (data) {
            console.log(data);

            for (var i = 0; i <= data.length - 1; i++) {

                // genre += "<h1>Genre(For udpate)</h1>";
                div += "<div class=\"row bg-white has-shadow\">" +
                    "<div class=\"left-col col-lg-5 d-flex align-items-center justify-content-between\">" +
                    "<div class=\"project-title d-flex align-items-center\">" +
                    "<div class=\"image has-shadow\"><img src="+data[i].image+" style=\"height: 110%; width: 100%;\" alt=\"...\" class=\"img-fluid\"></div>" +
                    "<div class=\"text\">" +
                    "<input type='hidden' class='bidclass' value="+data[i].book_id+">"+
                    "<a href='bookbyid' class='bookid'><h2>" + data[i].title + "</h2></a><br>" +
                    "<small>" + data[i].author + "</small>" +
                    "</div>" +
                    "</div>" +
                    "</div>" +
                    "<div class=\"right-col col-lg-4 d-flex align-items-center\">" +
                    "<div class=\"desc\">" + data[i].description + "</div>" +
                    "</div>" +
                    "<div class=\"right-col col-lg-3 d-flex align-items-center\">" +
                    "<form id='addtolib'>" +
                    "<input name = \"book\" type=\"hidden\" value= " + data[i].book_id + ">" +
                    "<button type=\"button\" onclick=\"openModallib('confirmModallib',"+data[i].book_id+")\" class=\"btn btn-warning\">Add book</button></form>" +
                    "<form method=\"delete\" style=\"padding-left:2%\"  action=\"/book" + "/" + data[i].book_id + "\">" +
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

    //get users library
    function getuserlibrary() {
    var $listbook = $("#listbooklib");
    var div = [];
    $.ajax({
        url: 'library',
        dataType: 'JSON',
        success: function (data) {
            console.log(data);

            for (var i = 0; i <= data.length - 1; i++) {

                div += '<div class="row bg-white has-shadow">'+
                    '<div class="left-col col-lg-6 d-flex align-items-center justify-content-between">'+
                      '<div class="project-title d-flex align-items-center">'+
                        '<div class="image has-shadow"><img src="../static/img/book.jpg " style="height: 110%; width: 100%;" alt="..." class="img-fluid"></div>'+
                        '<div class="text">'+
                          '<h2>'+data[i].title+'</h2>'+
                          '<i>'+data[i].author+'</i>'+
                        '</div>'+
                      '</div>'+
                      '</div>'+
                    '<div class="right-col col-lg-5 d-flex align-items-center">'+
                      '<div class="desc">'+data[i].description+'</div>'+
                    '</div>'+
                    '<div class="right-col col-lg-1 d-flex align-items-center">'+
                      '</div>'+
                    '</div>'+
                  '</div>';
            }
            $listbook.html(div);

        }
    });


}

    //get ratings for book
    function getratings() {
        var book_id = localStorage.getItem('bid');
        var $listrating = $("#ratinguser");

        var content = [];

        $.ajax({
            url: 'rate/' + book_id,
            dataType: 'JSON',
            success: function (data) {
                console.log(data);

                for (var i = 0; i <= data.length - 1; i++) {
                    content += '<div class="feed d-flex justify-content-between">' +
                        '<div class="feed-body d-flex justify-content-between"><a href="#" class="feed-profile"><img src="img/avatar-3.jpg" alt="person" class="img-fluid rounded-circle"></a>' +
                        '<div class="content">' +
                        '<h2>' + data[i].username + '<h2>' +
                        '<h3>' + data[i].rating + ' Stars <i class="fa fa-star text-orange"></i></h3>' +
                        '<div class="full-date"><small>Date</small></div>' +
                        '</div>' +
                        '</div>' +
                        '</div>' +
                        '<div class="quote has-shadow"><p>' + data[i].comment +'</p></div>';
                    $listrating.html(content);

                }
            }
        })
    }

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

        return true;
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
    //list all users
    function init_userlist(listurl) {
    $userTable = $('#userlist');
    var divtable = [];
        $userbyusername = $('#getausername');
        $.ajax({
            url: listurl,
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

    // get value of row and store in local storage for later use
    $userTable = $('#userlist');
    var table = $userTable;
    $userTable.on('click', 'tbody tr', function() {
    var tableData = $(this).children("td").map(function() {
        return $(this).text();
    }).get();
  var username= tableData[0];
    localStorage.setItem('username', username);
    document.location.href = ('/user');
});

$(document).on('click', '.bookid', function() {

    var div = $(this).closest('div');
    var bookid = (div.find('input').val());
    localStorage.setItem('bid', bookid);

});


//post functions
    //post add book
    function addbooktogenre() {
 var bookid = $("#bookmodal").serialize();
 var genre_id = localStorage.getItem('gid');

     $.ajax({
        url: '/genre/addbook/' + genre_id,
        data: bookid,
        method: 'POST',
        dataType: 'JSON',
        success: function (data) {
            console.log(data)

        }
    });
     document.location.href = ('/genre/addbookstogenre');
}

    // get value of row and store in local storage for later use
// $genreTable = $('#genretable');
// var gentable = $genreTable;
// $genreTable.on('click', 'tbody tr', function() {
//  var tableData = $(this).children("td").map(function() {
//         return $(this).text();
//     }).get();
//  var genreid= tableData[0];
//     localStorage.setItem('genreid', genreid);
//     document.location.href = ('/genrebyid');
// });

    //add genre
    function savegenre() {
    var data = $('#genrepost').serialize();
    console.log(data);
    $.ajax({
        url: '/genre',
        data: data,
        method: 'POST',
        dataType: 'JSON',
        success: function (data) {
            console.log(data)

        }
    });
     document.location.href = ('/genres');
}

    //add new book
   $("#addbookbtn").click(function (e) {
       e.preventDefault();
       var formData = new FormData($("#adddata")[0]);
       console.log(formData)
      // var form_data = new FormData($('#upload-file')[0]);
    //    var object = {};
    // formData.forEach(function(value, key){
    // object[key] = value;
    // console.log(value)
    //     });
    //console.log(object);
    $.ajax({
        url: '/book',
        data: formData,
        method: 'POST',
        contentType: false,
        cache: false,
        processData: false,
        success: function (data) {
            console.log(data)
        }
    });
     document.location.href = ('/books');
     });


    //add book to library
    function addbooktolib() {
    var data = $('#addbooklib').serialize();
    console.log(data);
    $.ajax({
        url: '/library',
        data: data,
        method: 'POST',
        dataType: 'JSON',
        success: function (data) {
            console.log(data)
        }
    });
    document.location.href = ('/libraries');
}

    //add rating
    var book_id = localStorage.getItem('bid');
    $("#bookid").val(book_id);
    function addrating() {
    var book_id = localStorage.getItem('bid');
    var data = $('#addrating').serialize();
    console.log(data);
    $.ajax({
        url: '/rate',
        data: data,
        method: 'POST',
        dataType: 'JSON',
        success: function (data) {
            console.log(data)
        }
    });
    document.location.href = ('/bookbyid');
    }

    //delete or update functions

//delete genre
function deletegenre(genre_id) {

    var data = $('#genredel').serialize();
    console.log(data);
    $.ajax({
        url: '/rate',
        data: data,
        method: 'POST',
        dataType: 'JSON',
        success: function (data) {
            console.log(data)
        }
    });
    //document.location.href = ('/bookbyid');
    }


