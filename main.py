from core.check import run
from core.utils import clear, get_livesudoku_url, bye, get_browser
from core.settings import flag, line, config
from scrapper import get_table


def main():
    # check user to install dependencies
    run()
    
    # get level from user
    clear() # clear screen
    print(flag)

    _counter = 0
    while True:

        if _counter == 3:
            print("Have a good time.")
            bye()

        try:
            level = input(f"> Type level [easy, medium, hard, evil] : ")
            url = get_livesudoku_url(level)
            break

        except AssertionError as e:
            _counter += 1
            print(e, ",Try again!")

        except KeyboardInterrupt as e:
            bye()

    # run browser driver
    print(f'Starting webdriver : [LOG]\n{line}', end='')
    browser = get_browser(url)

    # get sudoku table
    selectors = config['livesudoku']['selectors']
    sudoku_table = get_table(browser, selectors['tr'], selectors['td'], selectors['data'])
    print(line, "Sudoku :", *sudoku_table, sep="\n")


    #   solve sudoku by z3
    #   set solved sudoku in web table
    #   send sudoku
    #   kill browser !

    pass

if __name__ == "__main__":
    main()
