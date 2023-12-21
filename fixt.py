def any_fix(other_func):
    def inside_func():
        print("message before")
        other_func()
        print("message after")
    return inside_func()
def print_message_hi():
    print ("stroka")

@any_fix
def def_1():
    print("что-то")