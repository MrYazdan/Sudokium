from time import sleep
from selenium.webdriver.common.by import By


def set_number(n: int, browser, sleep_time) -> None:
    sleep(sleep_time)
    browser.execute_script(f"return keypadnumber({n});")


def injector(solved_sudoku, browser, selectors, sleep_time):  
    tr_selector, td_selector, data_selector = selectors['tr'], selectors['td'], selectors['td']

    trs = browser.find_elements(By.CSS_SELECTOR, tr_selector)
    for tr in trs:
        i = trs.index(tr)
        tds = tr.find_elements(By.CSS_SELECTOR, td_selector)

        for td in tds:
            j = tds.index(td)
            sleep(0.05)
            try:
                span = td.find_element(By.CSS_SELECTOR, data_selector)
                data = int(span.text.strip())

            except Exception as e:
                td.click()
                sleep(0.05)

                set_number(solved_sudoku[i][j], browser, sleep_time)
