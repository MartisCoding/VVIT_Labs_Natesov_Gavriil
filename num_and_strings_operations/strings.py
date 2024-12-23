
def camel_to_snake(camel):
    res = []
    for word in camel.split(' '):
        res += word.upper()

    return "_".join(res)

def snake_to_camel(snake):
    res = []
    for word in snake.split('_'):
        res.append(word.capitalize())
    return ''.join(res)