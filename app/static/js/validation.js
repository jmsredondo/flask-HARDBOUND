 //Register
 /*$( "#userpost" ).validate({
     rules: {
         registerUserName: {
             required: true,
         },
         registerFirstname:{
             required: true,
             field: { accept: "[a-zA-Z]+" }
         },
         registerLastname:{
             required: true,
             field: { accept: "[a-zA-Z]+" }
         },
         registerEmail:{
             required: true,
             email: true
         },
         registerPhoneNum:{
             required: true,
             digits: true
         },
     }
 });*/


$('#register').click(function() {
    if($("#userpost").valid()) {
        userregister()
    }else {
        alert('incomplete information')
    }
});

/*
//User Login
 $( "#loginpost" ).validate({
     rules: {
         username: {
             required: true,
         },
         password:{
             required: true,
        },
    }
 });
 $('#login').click(function() {
     if($("#loginpost").valid()) {
         userregister()
     }else {
        alert('incomplete information')
     }
 });
*/
// //Admin Login
// $( "#loginpostadmin" ).validate({
//     rules: {
//         username: {
//             required: true,
//         },
//         password:{
//             required: true,
//         },
//     }
// });


// $('#login').click(function() {
//     if($("#loginpostadmin").valid()) {
//         userregister()
//     }else {
//         alert('incomplete information')
//     }
// });

//Add book
// $( "#bookpost" ).validate({
//     rules: {
//         title: {
//             required: true,
//         },
//         description:{
//             required: true,
//         },
//         author:{
//             required: true,
//             field: { accept: "[a-zA-Z]+" }
//         }
//     }
// });
//
//
// $('#').click(function() {
//     if($("#bookpost").valid()) {
//         userregister()
//     }else {
//         alert('incomplete information')
//     }
// });
//
// //Add genre
// $( "#genrepost" ).validate({
//     rules: {
//         title: {
//             addCat: true,
//         }
//     }
// });
//
//
// $('#').click(function() {
//     if($("#genrepost").valid()) {
//         userregister()
//     }else {
//         alert('incomplete information')
//     }
// });
//
// //Add library
// $( "#genrepost" ).validate({
//     rules: {
//         title: {
//             addCat: true,
//         }
//     }
// });


// $('#').click(function() {
//     if($("#genrepost").valid()) {
//         userregister()
//     }else {
//         alert('incomplete information')
//     }
// });

//Add rating
// $("#bookpost" ).validate({
//     rules: {
//         title: {
//             required: true,
//         },
//         description:{
//             required: true,
//         },
//         author:{
//             required: true,
//             field: { accept: "[a-zA-Z]+" }
//         }
//     }
// });


// $('#').click(function() {
//     if($("#bookpost").valid()) {
//         userregister()
//     }else {
//         alert('incomplete information')
//     }
// });
