def convert_to_time_span(expression):
    expression = expression.replace('Z', '')
    expression = expression.partition("T")[2]
    return expression
