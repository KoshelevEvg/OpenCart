class Common:
    class alert_mes:
        class success:
            it = {'css': '.aler-success'}
            login = {'css': it['css'] + ' > a:nth-child(2)'}
            to_cart = {'css': it['css'] + ' > a:nth-child(2)'}

    class user_login:
        email_input = {'css': '#input-email'}
        password_input = {'css': ' #input-password'}
        login_button = {'css': ' input[value=Login]'}
