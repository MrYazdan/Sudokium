from selenium.webdriver.common.by import By


def get_table(browser, tr_selector, td_selector, data_selector):
    table = []

    trs = browser.find_elements(By.CSS_SELECTOR, tr_selector)
    for tr in trs:
        row = []
        tds = tr.find_elements(By.CSS_SELECTOR, td_selector)

        for td in tds:
            try:
                span = td.find_element(By.CSS_SELECTOR, data_selector)
                data = int(span.text.strip())
            except Exception as e:
                data = 0

            row.append(data)

        table.append(row)
        
    return table