import subprocess, os

from tabulate import tabulate

def menu_arcserve():

    menu = [["SELECIONE A OPÇÃO CORRESPONDENTE"], ["1 - BAIXAR O ARCSERVE UDP"], ["2 - INSTALAR O ARCSERVE UDP"]]
    print(tabulate(menu, headers="firstrow"))

    option = int(input("Selecione uma das opções: "))

    if option == 1:
        print("Estamos implementando ainda...")
    elif option == 2:
        os.chdir("installers")
        print(f"Validando o caminho da instalação: {os.getcwd()}")
        subprocess("Arcserve_Unified_Data_Protection.exe -s -a -q -Products:All -User:administrator -Password:test -Https:1")


menu_arcserve()