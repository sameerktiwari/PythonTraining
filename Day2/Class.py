class emp:
    name=""
    def display(self):
        print(self.name)

    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setName(self,name):
        self.name=name
