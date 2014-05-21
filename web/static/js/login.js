//ON SUBMIT
$(function() {
	  $('#loginbutton').click(function() {
        var form_data = new FormData($('#loginform')[0]);
        $.ajax({
            type: 'POST',
            url: '/_attempt',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
            		if (data['ident']=='') {
            				console.log('Username/Password could not be found');
            		} else {
            		    console.log('Logged In');
            		    console.log(data['ident']);
            		}
            },
        });
	  });
});
