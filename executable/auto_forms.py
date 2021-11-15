import time
from browser import get_browser


def load_form():
    get_browser().get("https://docs.google.com/forms/d/e/1FAIpQLScxM63-DsFO1HKCTpCnfY-DHmEBZd6DgBwNUz7_Ooh3blJBmA/viewform")
    time.sleep(3)


def fill_name(name):
    xpath = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"

    element = get_browser().find_element_by_xpath(xpath)
    element.send_keys(name)


def fill_email(email):
    xpath = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"

    element = get_browser().find_element_by_xpath(xpath)
    element.send_keys(email)


def fill_source(source):
    if source == 'Atacado':
        option = 1
    else:
        # Seta Varejo
        option = 2
    
    xpath = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[{option}]/label/div'

    element = get_browser().find_element_by_xpath(xpath)
    element.click()


def fill_categories(categories):
    for category in categories.split(', '):
        if category == 'Camisa':
            option = '1'
        elif category == 'Calça':
            option = '2'
        elif category == 'Vestido':
            option = '3'
        else:
            # Set Roupas Íntimas
            option = '4'
        
        xpath = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[{option}]/label/div/div[1]/div[2]'
        element = get_browser().find_element_by_xpath(xpath)
        element.click()


def fill_account_type(account_type):
    xpath_open = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]"

    element = get_browser().find_element_by_xpath(xpath_open)
    element.click()
    time.sleep(1)

    if account_type == 'Não Cadastrado':
        option = '3'
    elif account_type == 'Cadastrado':
        option = '4'
    elif account_type == 'Cliente Regular':
        option = '5'
    else:
        # Set Cliente Premium
        option = '6'

    xpath = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[{option}]'

    element = get_browser().find_element_by_xpath(xpath)
    element.click()


def fill_rating(rating):
    xpath = f'/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[{rating}]/div[2]/div/div/div[3]'

    element = get_browser().find_element_by_xpath(xpath)
    element.click()


def send_form():
    xpath = f'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span'

    element = get_browser().find_element_by_xpath(xpath)
    element.click()


def fill_form(sale):
    load_form()

    fill_name(sale['FULL_NAME'])
    time.sleep(1)

    fill_email(sale['EMAIL'])
    time.sleep(1)

    fill_source(sale['SOURCE'])
    time.sleep(1)

    fill_categories(sale['CATEGORIES'])
    time.sleep(1)

    fill_account_type(sale['TYPE'])
    time.sleep(2)

    fill_rating(sale['RATING'])
    time.sleep(2)

    send_form()
    time.sleep(3)