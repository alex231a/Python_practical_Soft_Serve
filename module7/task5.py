class LeafElement:
    def __init__(self, position, salary=None):
        self.position = position
        self.salary = salary

    def showDetails(self):
        print('Hello1')
        if self.salary is not None:
            print(f'\t{self.position} - Salary: {self.salary}')
        else:
            print(f"\t{self.position}")


class CompositeElement:
    def __init__(self, position):
        self.position = position
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print('Hello2')
        print(self.position)
        for child in self.children:
            child.showDetails()




topLevelMenu = CompositeElement("GeneralManager")
subMenuItem1 = CompositeElement("Manager1")
subMenuItem2 = CompositeElement("Manager2")
subMenuItem11 = LeafElement("Developer11")
subMenuItem12 = LeafElement("Developer12")
subMenuItem21 = LeafElement("Developer21")
subMenuItem22 = LeafElement("Developer22")
subMenuItem1.add(subMenuItem11)
subMenuItem1.add(subMenuItem12)
subMenuItem2.add(subMenuItem22)
subMenuItem2.add(subMenuItem22)
topLevelMenu.add(subMenuItem1)
topLevelMenu.add(subMenuItem2)
topLevelMenu.showDetails()