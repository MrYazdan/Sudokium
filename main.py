from core.check import run
from core.utils import clear, get_livesudoku_url
from core.settings import flag


def main():
    # check user to install dependencies
    run()
    
    # get level from user
    clear() # clear screen
    print(flag)

    _counter = 0
    while True:

        if _counter == 3:
            pass

        try:
            level = input(f"> Enter level of livesudoku [easy, medium, hard, evil] : ")
            url = get_livesudoku_url(level)

        except AssertionError as e:
            _counter += 1
            print(e, ",Try again!")

        except KeyboardInterrupt as e:
            pass

    #   run browser driver
    #   get sudoku table
    #   solve sudoku by z3
    #   set solved sudoku in web table
    #   send sudoku
    #   kill browser !

    pass

if __name__ == "__main__":
    main()
