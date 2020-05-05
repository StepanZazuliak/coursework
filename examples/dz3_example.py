import json

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