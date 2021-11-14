"""
Modul care contine modul de memorare al listelor de entitati
"""
from entities import persoana, eveniment  

class persList_repo:
    
    def __init__(self):
        """Suport pentru memorarea listei de persoane
        """
        self.__pers = []

    def store(self, persoana):
        for pers in self.__pers:
            if pers == persoana:
                raise ValueError("Persoana exista deja")

        self.__pers.append(persoana)

    def getAll(self):
        return self.__pers
    
    def size(self):
        return len(self.__pers)
    
    def deleteElem(self, pos):
        if pos < len(self.__pers):
            self.__pers.pop(pos)
        else:
            raise ValueError("Nu exista")

    def getElem(self, pos):
            return self.__pers[pos]

def test_persList():
    a = persList_repo()
    pers = persoana(1, "Andrei George", "Bulevardul Alexandru cel Bun nr 15")
    a.store(pers)
    assert(a.size() == 1)

    pers = persoana(2, "George Andrei", "Bulevardul Alexandru cel Rau nr 2")
    a.store(pers)
    assert(a.size() == 2)

class evenList_repo:
    
    def __init__(self):
        """Suport pentru memorarea listei de evenimente
        """
        self.__events = []

    def store(self, eveniment):
        for even in self.__events:
            if even == eveniment:
                raise ValueError("Evenimentul exista deja ")

        self.__events.append(eveniment)

    def getAll(self):
        return self.__events
    
    def size(self):
        return len(self.__events)
    
    def deleteElem(self, pos):
        if pos < self.size():
            self.__events.pop(pos)
        else:
            raise ValueError("Evenimentul nu exista")

    def getElem(self, pos):
        return self.__events[pos]
        

def test_eventList():
    a = evenList_repo()
    even = eveniment(1, "12/02/2022", "10:00", "Descriere de eveniment")
    a.store(even)
    assert(a.size() == 1)

    
    #!!!!!!!! Cum verifici daca programul afiseaza o exceptie???
    
    
    even = eveniment(28, "12/02/2022", "11:00", "Descriere de eveniment2")
    a.store(even)
    assert(a.size() == 2)

test_persList()
test_eventList()




class stocInscrieri:
    def __init__(self):
        self.__inscrieri = []

    def storeInscriere(self, IDpers, IDevent):
        """Stochează legăturile 

        Args:
            IDpers (int): Id-ul persoanei înscrise
            IDevent (int): Id-ul evenimentului
        """
        inscriere = (IDpers, IDevent)
        self.__inscrieri.append(inscriere)
    