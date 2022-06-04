from core.settings import config
from os import system as terminal, name as os_name


def clear():
    terminal('cls') if os_name.lower() == "nt" else terminal('clear')


def get_livesudoku_url(level: str) -> str:
    """
    Get livesudoku url via level :)

    Args:
        level (str): [valid livesudoku level such as hard, easy, ...]

    Returns:
        str: [full url of livesudoku with select level]
    """

    assert level.lower() in config['livesudoku']['levels'], 'Invalid livesudoku level!'
    return config['livesudoku']['base_url'] + level.lower()


def bye() -> None:
    print('\nGoodbye ! :)')
    exit()
