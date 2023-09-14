def toPostFixExpression(e):
    def precedence(operator):
        if operator in ('+', '-'):
            return 1
        elif operator in ('*', '/', '%'):
            return 2
        return 0  # Lower precedence for parentheses

    def is_operator(token):
        return token in ('+', '-', '*', '/', '%')

    output = []
    operator_stack = []

    for token in e:
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # Pop the '('
        elif is_operator(token):
            while operator_stack and operator_stack[-1] != '(' and precedence(operator_stack[-1]) >= precedence(token):
                output.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        output.append(operator_stack.pop())

    return output

# Example usage:
e = ["2", "+", "3"]
postfix_notation = toPostFixExpression(e)
print(postfix_notation)  # Output: ['2', '3', '+']