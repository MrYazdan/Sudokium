config = {
    'livesudoku': {
        'base_url': 'https://www.livesudoku.com/en/sudoku/',
        'levels': ['easy', 'medium', 'hard', 'evil'],
        'selectors': {
            'tr': '#playtable>tbody>tr',
            'td': "td",
            'data': "span"
        }
    },
    'sleep': 1,  # Sleep time to set number in block of sudoku table
}

line = "--------------------------------------------------"

flag = f"""
   _____           __      __   _               
  / ___/__  ______/ /___  / /__(_)_  ______ ___ 
  \__ \/ / / / __  / __ \/ //_/ / / / / __ `__ \\
 ___/ / /_/ / /_/ / /_/ / ,< / / /_/ / / / / / /
/____/\__,_/\__,_/\____/_/|_/_/\__,_/_/ /_/ /_/ 

# Isfahan Gonbad - selenium livesudoku solver                                      
> repo : https://github.com/MrYazdan/Sudokium/
> version : 1.0
{line}"""
