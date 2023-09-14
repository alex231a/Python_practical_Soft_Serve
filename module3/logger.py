def logger(func):
    def wrapper(*args, **kwargs):
        list_args = []
        for i in args:
            list_args.append(str(i))

        for i in kwargs.values():
            list_args.append(str(i))

        if len(list_args) < 1:
            str_output = list_args[0]
        else:
            str_output = ', '.join(list_args)

        result = func(*args, **kwargs)
        # Print function information
        print(f"Executing of function {func.__name__} with arguments {str_output}...")

        # Call the original function


        return result

    return wrapper

# Apply the logger decorator to the concat function
@logger
def concat(*args, **kwargs):
    list_args = []
    for i in args:
        list_args.append(str(i))

    for i in kwargs.values():
        list_args.append(str(i))

    if len(list_args) < 1:
        combined_args = list_args[0]
    else:
        combined_args = ''.join(list_args)

    return combined_args

@logger
def sum(a, b):
    return a + b

@logger
def print_arg(arg):
    print(arg)


print_arg(2)
# print(concat(1))
# # Test the decorated function
# # print(concat(2, 3))
# # print(concat('hello', 2))
# print(concat(first='one', second='two'))
# print(concat('first string', second = 2, third = 'second string'))

