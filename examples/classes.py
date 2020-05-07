class Podatok:
    '''
    Podatok ADT
    '''

    def __init__(self, platnyk, percent, descr, osnova, section):
        '''
        (Podatok, str, int, str, float, str) -> NoneType
        Create new Podatok
        '''

        self.platnyk = platnyk
        self.percent = percent
        self.descr = descr
        self.osnova = osnova
        self.section = section

    def __str__(self):
        '''
        (Podatok) -> str
        Return str of the Podatok
        '''

        res = str(self.platnyk) + ' сплачує податок ' + str(self.descr) + ' з секції ' + str(self.section) +' за сумою ' + str(self.osnova) + ' грн нараховується ' + str(self.percent) + ' %.'
        return res

    def calculate(self):
        '''
        (Podatok) -> float
        Calculate the amount of the Podatok
        '''

        res = self.osnova * (self.percent / 100)
        return res

    def describe(self):
        '''
        (Podatok) -> str
        Return descrption of the Podatok
        '''

        res = 'Секція: ' + self.section + '\n' + 'Опис: ' + self.descr
        return res

    def sectionName(self):
        '''
        (Podatok) -> str
        Return section of the Podatok
        '''

        return self.section

class Platnyk:
    '''
    Class for representing of the Platnyk
    '''

    def __init__(self, name, dohid=0.0, vlasnist=[], podatky=[], suma = 0.0, typ = "Фізична особа"):
        '''
        (Platnyk, str, float, list, list, list, float, str) -> NoneTyoe
        Create new Platnyk
        '''

        self.name = name
        self.dohid = dohid
        self.vlasnist = vlasnist
        self.podatky = podatky
        self.sum = suma
        self.typ = typ

    def __str__(self):
        '''
        (Platnyk) -> str
        Return str of the Platnyk
        '''

        res = str(self.typ) + ' ' + str(self.name) + ' має дохід ' + str(self.dohid) + ' грн, має таку власність: ' + str(self.vlasnist) + ', сплачує такі податки: ' + str(self.podatky) + ', на суму ' + str(self.sum) + ' грн/'
        return res

    def calculate(self):
        '''
        (Podatok) -> float
        Calculate sum of the podatky
        '''

        res = 0
        for p in self.podatky:
            res = res + p.calculate()

        self.sum = self.sum + res

    def zvit(self):
        '''
        (Podatok) -> str
        Return sr of podatky
        '''

        res = ''
        for p in self.podatky:
            res = res + p.__str__() + '\n'

        return res

    def addPodatok(self, podatok):
        '''
        (Platnyk, Podatok) -> NoneType
        Add new Podaton to podatky
        '''

        self.podatky.append(podatok)

    def delPodatok(self, index):
        '''
        (Podatok, int) -> NoneType
        Delete Podatok from the podatky by the index
        '''

        self.podatky.pop([index])

    def addvlasnist(self, vlasnist1):
        '''
        (Platnyk, Podatok) -> NoneType
        Add new vlasnist to podatky
        '''

        self.vlasnist.append(vlasnist1)

    def delvlasnist(self, index):
        '''
        (Podatok, int) -> NoneType
        Delete vlasnist1 from the vlasnist by the index
        '''

        self.vlasnist.pop([index])

    def changedohid(self, newdohid):
        '''
        (Podatok, float) -> NoneType
        Change the dohid
        '''

        self.dohid = newdohid

    def changetyp(self, newtyp):
        '''
        (Podatok, float) -> NoneType
        Change the typ
        '''

        self.typ = newtyp

    def summa(self):
        '''
        (Podatok) -> float
        Return sum of the debt
        '''

        return self.sum

    def oplata(self, opl):
        '''
        (Podatok, float) -> NoneType
        Make the payment
        '''

        self.sum = self.sum - opl