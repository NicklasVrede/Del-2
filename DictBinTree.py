from dataclasses import dataclass

class BinNode:
    def __init__(self, nøgle):
        self.k = nøgle
        self.venstre = None
        self.højre = None

class DictBinTree:
    def __init__(self):
        self.rod = None
        
    #Recursive udgave
    def search(self, k):
        #Søg efter nøglen k.
        def søg(x, k):
            if x == None: 
                return False #False istedet for None
            if x.k == k:
                return True
            
            if k < x.k: #Hvis k er mindre end T.værdi
                return søg(x.venstre, k)
            else:
                return søg(x.højre, k)

        #peg på en node og brug x som i pseudokoden. 
        x = self.rod

        if x is None:
            return False
        else:
            if k == x.k:
                return True
            
        return søg(x, k)


    #Iterativ udgave
    def search(self, k):
        #Peg på en node  og brug x som i pseudokoden
        x = self.rod

        if x is None:
            return False
        
        if k == x.k:
            return True

        #Søg efter nøglen k
        while x != None and k != x.k:
            if k < x.k:
                x = x.venstre
            else:
                x = x.højre

        if x is None:
            return False
        else:
            return True
        

    def insert(self, k):
        x = self.rod
        y = None
        while x != None:
            y = x
            if k < x.k:
                x = x.venstre
            else:
                x = x.højre

        #y pointer nu på pladsen som k skal indsættes

        if y == None: #Træet er tomt, så k bliver roden
            self.rod = BinNode(k)
        
        elif k < y.k:
            y.venstre = BinNode(k)
        else:
            y.højre = BinNode(k)


    def orderedTraversal(self):
        def træ_gang(x, res=[]):
            if x != None:
                træ_gang(x.venstre, res)
                res.append(x.k)
                træ_gang(x.højre, res)
            return res

        return træ_gang(self.rod)

