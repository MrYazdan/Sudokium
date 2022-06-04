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

def get_browser(url: str):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from time import sleep

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(url)
    
    sleep(config['sleep'])

    return browser