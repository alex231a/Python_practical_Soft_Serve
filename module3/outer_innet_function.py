# Create function with name outer(name). This function should return inner function with name inner.
# This inner function prints message Hello, <name>!
# For example
# tom = outer("tom")
# tom() -> Hello, tom!


def outer(name):
    def inner():
        string_to_return = f"Hello, {name}!"
        print(string_to_return)
    return inner


tom = outer("tom")
tom()
