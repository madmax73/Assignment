class gumballMachine:
    def __init__(self, money = 0, gumballs=['red','green','blue','yellow','pink','purple','cyan','red','red']):        
        self.money = money
        self.gumballs = gumballs

    @property
    def gum_num(self):
        print(f'there are {len(self.gumballs)} in the machine')

    def report(self):
        print(f'Gumballs in machine : {len(self.gumballs)}')
        print(f'Money in machine: ${self.money:.2f}')
    
    def dispense(self,value):
        if len(self.gumballs) == 0:
            print('Machine is empty, no gumball will be dispensed')
            pass
        else:
            if value == 0.25:
                dispensed_gum = self.gumballs[-1:]
                self.gumballs.pop(len(self.gumballs)-1)
                self.money += value
                print(f'Accepting ${value:.2f}; Dispensing a {dispensed_gum} gumball')
            else:
                print('Invalid coin, no gumball will be dispensed')
                pass
    
    def count_gumballs_by_type(self,type):
        print(self.gumballs.count(type))
        

machine = gumballMachine()
