// $(document).ready(function(){
//   alert("Hello! I am an alert box!!");
//
// })


$(function() {

  // submit post on submit
  $('#employee-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!");
    create_employee();
  })

  // AJAX for posting a new employees
  function create_employee() {
    // console.log("create post is working!") // sanity check
    // console.log($('#employee-name').val())
    // console.log($('#employee-job-title').val())
    // console.log($('#employee-years-experience').val())
    // console.log($('#employee-department').val())
    // console.log($('#employee-image').val())
    $.ajax({
      url: "/employees/create_post/", // target the endpoint
      type: "POST",
      data: {name: $('#employee-name').val(), job_title: $('#employee-job-title').val(), years_experience: $('#employee-years-experience').val(), department: $('#employee-department').val()},

      // handle a successful reponse
      success: function(json) {
        ('#employee-form').trigger("reset");
        console.log(json);
        console.log('success');
      },
      // handle a non-successful response
      error: function(xhr, errmsg, err){
        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+" <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
    });
};

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});
