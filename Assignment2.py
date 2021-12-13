class gumballMachine:
    def __init__(self, money = 0, gumballs=['red','green','blue','yellow','pink','purple','cyan']):
        
        self.money = money
        self.gumballs = gumballs
    def report(self):
        print(f'Gumballs in machine : {len(self.gumballs)}')
        print(f'Money in machine: ${self.money:.2f}')
    
    def dispense(self,value):
        if len(self.gumballs) == 0:
            pass
        else:
            if value == 0.25:
                self.gumballs.pop(len(self.gumballs)-1)
                self.money += value
                print(self.money,self.gumballs)
            else:
                pass
        

machine = gumballMachine()
machine.report()
machine.dispense(0.25)
machine.report()