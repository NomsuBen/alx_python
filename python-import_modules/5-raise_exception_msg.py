def raise_exception_msg(message=""):
    class CustomException(Exception):
        pass

    raise CustomException(message)

try:
    raise_exception_msg("C is fun")
except CustomException as e:
    print(e)

try:
    raise_exception_msg("Python is cool")
except CustomException as e:
    print(e)
