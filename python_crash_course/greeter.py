def greet_user():
    """显示简单的问候语"""
    print("hello !")

greet_user()


def greet_user(username):
    """ 显示简单的问候语，有参数"""
    print(f"Hello , {username} !")

greet_user("Jarvis ")