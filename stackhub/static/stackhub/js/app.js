$(document).ready(function() {
  // alert('hi');
  $('.modal').modal();

  // login handler
  $('.login-submit').on('click', function() {
    $('form.login-form').submit();
  })

  //search handler
  $('.search-input').on('keyup', function(event) {
    // console.log(event);
    var searchTerm = event.target.value;
    $.get('/search/', {'q': searchTerm}, function(data){
      $('.search-results').html(data.result_page);
    })
  })
})

//answer updation
$("button").on('click',function(){
      $.post('/answer/',{'ans': answer,'que_id':q_id}, function(data){

    })
})
