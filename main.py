import json
from classes import Podatok
from classes import Platnyk

print("Podatky")
print("Author: Stepan Zazuliak")
print("Start the prorgam")
print()

def help_podatok():
    '''
    Get info about the podatok
    '''
    
    inp = input("Введіть назву податку: ")
    path = "d:/UCU/coursework/podatky.json"

    with open(path, 'r', encoding='utf-8') as f:
        decoded_kved = json.load(f)

    try:
        for n in range(len(decoded_kved['sections'])):
            for k in range(len(decoded_kved['sections'][n]['divisions'])):
                for l in range(len(decoded_kved['sections'][n]['divisions'][k]['groups'])):
                    for h in range(len(decoded_kved['sections'][n]['divisions'][k]['groups'][l]['classes'])):
                        percent = decoded_kved['sections'][n]['divisions'][k]['groups'][l]['classes'][h]['percent']
                        obj  = decoded_kved['sections'][n]['divisions'][k]['groups'][l]['classes'][h]['object']
                        group = decoded_kved['sections'][n]['divisions'][k]['groups'][l]['groupname']
                        payer = decoded_kved['sections'][n]['divisions'][k]['groups'][l]['payer']
                        division = decoded_kved['sections'][n]['divisions'][k]['divisionName']
                        section = decoded_kved['sections'][n]['sectionName']
                        if inp == group:
                            print('Куди -> ', section)
                            print('Чого -> ', division)
                            print('Що -> ', group)
                            print('Хто ->', payer)
                            print('Скільки -> ', percent,'% ', obj)
                            print()

    except Exception:
        print("Виникла помилка з програмою")

def create_platnyk():
    '''
    Function to create the Platnyk
    '''

    n = input("Ім'я: ")
    d = int(input("Дохід: "))
    v = input("Власність: ")

    platnyk = Platnyk(n, d, [v], [])

    return platnyk

def create_podatok():
    '''
    Function to create podatok
    '''

    help_podatok()

    n = input("Ім'я: ")
    v = int(input("Відсоток: "))
    pn = input("Назва податку: ")
    b = int(input("База: "))
    d = input("Опис: ")

    podatok = Podatok(n, v, pn, b, d)

    return podatok

def zvit(pl):
    '''
    Return zvit of pl
    '''

    return str(pl)

def calculate(pl):
    '''
    Function to calculate pl
    '''

    pl.calculate()
    print(pl.sum)

def main():
    '''
    Start the module
    '''

    p = create_platnyk()
    pod = create_podatok()
    p.addPodatok(pod)
    print(zvit(p))

    while True:
        print("1 -- Додати податок")
        print("2 -- Нарахувати податок")
        print("3 -- Звіт")
        print("4 -- Змінити дохід")
        print("5 -- Додати власність")
        print("6 -- Оплата")

        inp = input('Введіть номер дії: ')

        if inp == '1':
            pod = create_podatok()
            p.addPodatok(pod)
            print(zvit(p))

        elif inp == '2':
            calculate(p)
            print(zvit(p))

        elif inp == '3':
            print(p.zvit())
            print(zvit(p))

        elif inp == '4':
            nd = input("Новий дохід: ")
            p.changedohid(nd)

        elif inp == '5':
            nv = input("Нова власність: ")
            p.changedohid(nv)

        elif inp == '6':
            s = int(input("Сума оплати: "))
            p.oplata(s)

        else:
            print("Невірний номер дії!")

main()