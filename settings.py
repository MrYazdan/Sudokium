config = {
    'livesudoku': {
        'base_url': 'https://www.livesudoku.com/en/sudoku/',
        'levels': ['easy', 'medium', 'hard', 'evil']
    }
}

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