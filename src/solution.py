from dataclasses import dataclass

@dataclass
class Solution:
    x: dict   # ouverture des entrepôts
    y: dict   # affectations
    cost: float

    def entrepot_ouverts(self):
        return [i for i, val in self.x.items() if val > 0.5]

    def affectations(self):
        affect = {}
        for (i,j), val in self.y.items():
            if val > 0.5:
                affect[j] = i
        
        return affect
    
    def afficher(self):
        print("\n Entrepôts ouverts :")
        for i in self.entrepots_ouverts():
            print(f" - {i} ")
        
        print("\n Affectations :")
        for j, i in self.affectations().items():
             print(f" - {j} -> {i}")

                print(f"\n Coût total = {self.cost}")



