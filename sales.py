from dbfread import DBF
from validator import sale_validator
from auto_forms import fill_form
from browser import quit_browser
import os


def load_valid_sales():
    sales = DBF("sales.dbf")

    valid_sales = []

    for sale in sales:
        if sale_validator(sale):
            valid_sales.append(sale)
    
    return valid_sales


valid_sales = load_valid_sales()


if valid_sales is not None:
    clear = None
    for sale in valid_sales:
        fill_form(sale)

        if clear is None:
            os.system('cls||clear')
            clear = 1

        print(f"Formulário de {sale['FULL_NAME']} preenchido")


print("Finalizado")
quit_browser()