from os import path, getcwd

FRUIT = 'fruit.png'
SNAKE_BODY = 'snake_body.png'
SNAKE_HEAD = 'snake_head.png'
EMPTY_FIELD = 'empty_field.png'

RELATIVE_PATH = 'snake/assets'

__EXECUTION_PATH = getcwd()

def get_absolute_file_path(file_name):
    return path.join(__EXECUTION_PATH, RELATIVE_PATH, file_name)