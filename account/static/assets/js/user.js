
$('#resgister-user').click(function(){
    var username = $('#username').val();
    var email = $('#email').val();
    var password = $('#password').val();
    var password_confirm = $('#password-confirm').val();
    var agreeTerms = $('#agreeterms');
    var passwordLen = password.length;

    // ÀÁÂÃÄÅàáâãäåÒÓÔÕÖØòóôõöøÈÉÊËèéêëÇçÌÍÎÏìíîïÙÚÛÜùúûüÿÑñ

    if(username != "" && /^[a-zA-Z ÀÁÂÃÄÅàáâãäåÒÓÔÕÖØòóôõöøÈÉÊËèéêëÇçÌÍÎÏìíîïÙÚÛÜùúûüÿÑñ]+$/.test(username)){
        $('#username').removeClass('is-invalid');
        $('#username').addClass('is-valid');
        $('#error-register-username').text('');

            if(email != "" && /^[a-z0-9._-]+@[a-z0-9._-]+\.[a-z]{2,6}$/.test(email)){
                $('#email').removeClass('is-invalid');
                $('#email').addClass('is-valid');
                $('#error-register-email').text('');

                if(passwordLen >= 8 ){
                    $('#password').removeClass('is-invalid');
                    $('#password').addClass('is-valid');
                    $('#error-register-password').text('');

                    if(password_confirm == password ){
                        $('#password-confirm').removeClass('is-invalid');
                        $('#password-confirm').addClass('is-valid');
                        $('#error-register-password-confirm').text('');

                        if(agreeTerms.is(' :checked') ){
                            $('#agreeterms').removeClass('is-invalid');
                            $('#error-register-agreeterms').text('');

                            //envoi du formulaire
                            $("#form-register").submit();

                        }else{
                            $('#agreeterms').addClass('is-invalid');
                            $('#error-register-agreeterms').text('Vous devez accepter nos terms et conditions !');
                        }

                    }else{
                        $('#password-confirm').addClass('is-invalid');
                        $('#password-confirm').removeClass('is-valid');
                        $('#error-register-password-confirm').text('Vos mots de passe doivent etre identiques !');
                    }

                }else{
                    $('#password').addClass('is-invalid');
                    $('#password').removeClass('is-valid');
                    $('#error-register-password').text('Votre mot de passe doit avoir plus de 8 caracteres !');
                }

            }else{
                $('#email').addClass('is-invalid');
                $('#email').removeClass('is-valid');
                $('#error-register-email').text('Email adress is not valid !');
            }

    }else{
        $('#username').addClass('is-invalid');
        $('#username').removeClass('is-valid');
        $('#error-register-username').text("Nom d'utiliateur invalide !");
    }
});


$('#agreeterms').change(function(){
    var agreeTerms = $('#agreeterms');

    if(agreeTerms.is(' :checked') ){
        $('#agreeterms').removeClass('is-invalid');
        $('#error-register-agreeterms').text('');

    }else{
        $('#agreeterms').addClass('is-invalid');
        $('#error-register-agreeterms').text('Vous devez accepter nos terms et conditions !');
    }
});

////////////

$('#login-user').click(function(){
    var email = $('#email').val();
    var password = $('#password').val();
    var agreeTerms = $('#agreeterms');
    var passwordLen = password.length;

            if(email != "" && /^[a-z0-9._-]+@[a-z0-9._-]+\.[a-z]{2,6}$/.test(email)){
                $('#email').removeClass('is-invalid');
                $('#email').addClass('is-valid');
                $('#error-login-email').text('');

                if(passwordLen >= 8 ){
                    $('#password').removeClass('is-invalid');
                    $('#password').addClass('is-valid');
                    $('#error-login-password').text('');

//                     if(agreeTerms.is(' :checked') ){
//                            $('#agreeterms').removeClass('is-invalid');
//                            $('#error-register-agreeterms').text('');
//
//                            //envoi du formulaire
//                            $("#form-login").submit();
//
//                     }else{
//                            $('#agreeterms').addClass('is-invalid');
//                            $('#error-register-agreeterms').text('Vous devez accepter nos terms et conditions !');
//                     }

                }else{
                    $('#password').addClass('is-invalid');
                    $('#password').removeClass('is-valid');
                    $('#error-login-password').text('Votre mot de passe doit avoir plus de 8 caracteres !');
                }

            }else{
                $('#email').addClass('is-invalid');
                $('#email').removeClass('is-valid');
                $('#error-login-email').text('Email adress is not valid !');
            }

});