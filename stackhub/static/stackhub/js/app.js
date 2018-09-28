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

  //answer updation
  $("#answer-submit-btn").on('click',function(){
      // console.log('answer submit');
      var answer = $('.materialize-textarea').val();
      var q_id = $('#q_id').val();
      var csrf_token = $('[name="csrfmiddlewaretoken"]').val();
      // var user_id = $('#user_id').val();

      // console.log(answer, q_id, csrf_token, 'answer, q_id, csrf_token')

      $.post('/question_detailpage/' + q_id + '/', {
        'answer': answer,
        // 'qid': q_id,
        'csrfmiddlewaretoken': csrf_token,
        // 'user_id': user_id
      }, function(data){
        if (data.success) {
          // console.log('data success')
          var ans_append = $('.answers-list')
          ans_append.append("<p>"+answer+"</p><hr/>")
}
      })
  })
})
