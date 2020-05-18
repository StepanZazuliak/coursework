from classes import Podatok
from classes import Platnyk

kalyshka = Platnyk('Калушка Максим Віталійович', 12000.0, ['пай 2га'], [])

pod_dohid = Podatok('Калушка Максим Віталійович', 18.0, 'Прибуток із джерелом походження з України та за її межами, який визначається шляхом коригування (збільшення або зменшення) фінансового результату до оподаткування (прибутку або збитку), визначеного у фінансовій звітності підприємства відповідно до національних положень (стандартів) бухгалтерського обліку або міжнародних стандартів фінансової звітності, на різниці, які виникають відповідно до положень Податкового кодексу України (далі – Кодекс)', 12000, 'Загальнодержавні податки та збори')
pod_ner_mayno = Podatok('Калушка Максим Віталійович', 5.0, 'Вартість нерухомого майна', 54000, 'Загальнодержавні податки та збори')
pod_gosp_ugidya = Podatok('Калушка Максим Віталійович', 1.0, 'Сільськогосподарські угіддя', 54000, 'Місцеві податки та збори')

kalyshka.addPodatok(pod_dohid)
kalyshka.addPodatok(pod_gosp_ugidya)
kalyshka.addPodatok(pod_ner_mayno)

print(kalyshka.zvit())
print('--------')

kalyshka.calculate()
print(kalyshka.summa())
print('--------')

kalyshka.oplata(15000)
print(kalyshka.sum)
print('--------')

kalyshka.changedohid(15000)
kalyshka.calculate()
print(kalyshka)
