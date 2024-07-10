def login_by_username_and_password(username :str, password :str):
    if username != "cc":
        raise ValueError("username parameter error")
    if password != "test123456":
        raise ValueError("password parameter error")


    return "login success"

