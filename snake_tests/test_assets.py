from os import getcwd

from snake.assets import get_absolute_file_path

def test_get_absolute_file_path():
    """
    get_absolute_file_path returns absolute path for file in assets directory
    """
    assert get_absolute_file_path('file.png') == '{}/snake/assets/file.png'.format(getcwd())