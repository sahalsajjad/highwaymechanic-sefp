$(document).ready(function(){
    $("#register-form").validate({
    
        // Specify the validation rules
        rules: {
            username: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 8
            },
            password_again: {
                required:true,
                minlength: 8,
                equalTo: '#password'
            },

        },
        
        
        messages: {
            
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 8 characters long"
            },
            password_again:{
                required:"Please enter the password again",
                equalTo:"Passwords do not match"
            },
            username: "Please enter a valid email address",
           
        },
        
        submitHandler: function(form) {
            form.submit();
        }
    });
});

