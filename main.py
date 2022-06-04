from time import sleep
from solver import solver
from core.check import run
from scrapper import get_table
from core.settings import flag, line, config
from core.utils import clear, get_livesudoku_url, bye, get_browser


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

    # solve sudoku by z3
    print('> Solving ...')
    sleep(config['sleep'])
    solved_table = solver(sudoku_table)
    print(line, "Result of solver :", *solved_table, sep="\n")
    print("> Completed !")

    #   set solved sudoku in web table
    #   send sudoku
    #   kill browser !

    pass

if __name__ == "__main__":
    main()
