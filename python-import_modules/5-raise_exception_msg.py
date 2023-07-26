def raise_exception_msg(message=""):
    class CustomException(Exception):
        pass

    raise CustomException(message)

try:
    raise_exception_msg("This is a custom exception message.")
except CustomException as e:
    print("Exception raised:", str(e))