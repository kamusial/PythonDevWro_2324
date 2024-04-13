class ContextManagerShowOff:

    def __init__(self):
        print("Object created")

    def __enter__(self):
        print("Entered with statement")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exited with statement")

    def greet(self):
        print("Hi, I'm a context manager and I like to show off :D")
        raise ValueError(":(")


with ContextManagerShowOff() as cm:
    cm.greet()


