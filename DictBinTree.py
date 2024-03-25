from dataclasses import dataclass

class BinNode:
    def __init__(self, nøgle):
        self.nøgle = nøgle
        self.venstre = None
        self.højre = None

class DictBinTree:
    def __init__(self):
        self.rod = None


#Recursive udgave
def search(T, k):
    #peg på en node og brug x som i pseudokoden. 
    if T.rod is None:
        x = T
    else:
        x = T.rod

    #Søg efter nøglen k.
    def søg(x, k):
        if x == None: 
            return False #False istedet for None
        if x.nøgle == k:
            return True
        
        if k < x.nøgle: #Hvis k er mindre end T.værdi
            return søg(x.venstre, k)
        else:
            return søg(x.højre, k)
    
#Iterativ udgave
def search(T, k):
    #Peg på en node  og brug x som i pseudokoden
    if T.rod is None:
        x = T.værdi
    else:
        x = T.rod

    #Søg efter nøglen k
    while x != None and k != x.nøgle:
        if k < x.nøgle:
            x = x.venstre
        else:
            x = x.højre

    if x == None:
        return False
    else:
        return True
    
def insert(T, k):
    x = T.rod
    y = None
    while x != None:
        y = x
        if k < x.nøgle:
            x = x.venstre
        else:
            x = x.højre
    #y pointer nu på pladsen som k skal indsættes
    #k.p? Vi anvender ikke forældre noder i vores class?
    if y == None: #Træet er tomt, så k bliver roden
        T.rod = BinNode(k)
    
    elif k < y.nøgle:
        y.venstre = BinNode(k)
    else:
        y.højre = BinNode(k)

def orderedTraversal(T):
    def træ_gang(x, res=[]):
        if x != None:
            træ_gang(x.venstre, res)
            res.append(x.nøgle)
            træ_gang(x.højre, res)
        return res

    return træ_gang(T.rod)

def createEmptyDict():
    return DictBinTree()