from selenium import webdriver

BROWSER = None


def start_browser():
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    browser.maximize_window()
    return browser


def get_browser():
    global BROWSER

    if BROWSER is None:
        BROWSER = start_browser()
    
    return BROWSER


def quit_browser():
    global BROWSER

    if BROWSER is None:
        BROWSER = start_browser()
    
    BROWSER.quit()