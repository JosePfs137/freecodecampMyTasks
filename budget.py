class Category:
        def __init__ (self, name):
            self.name = name
            self.ledger = []
        def deposit (self, amount, desc = ''):
            #try:
            self.amount = amount
            self.amount = float(self.amount)
            #except:
                #print('Error: the amount must be a number')
                #quit()
            self.ledger.append((self.amount, desc))
            #print('Deposit completed')

        def get_balance (self):
            sum = 0
            for a in self.ledger:
                sum = sum + a[0]
            return sum

        def check_funds (self, amount):
            try:
                self.amount = amount
                self.amount = float(self.amount)
            except:
                print('Error: the amount must be a number')
                quit()
            if self.amount <= self.get_balance():
                return True
            elif self.amount > self.get_balance():
                return False

        def withdraw (self, amount, desc = ''):
            try:
                self.amount = amount
                self.amount = float(self.amount)
            except:
                print('Error: the amount must be a number')
                quit()
            if self.check_funds(self.amount):
                self.amount = (-1) * self.amount
                self.ledger.append((self.amount, desc))
                return True
            else:
                return False
            #print('Withdraw completed')
        def transfer (self, amount, budget):
            if self.check_funds(amount):
                self.withdraw(amount, 'Transfer to ' + budget.name)
                budget.deposit(amount, 'Transfer from ' + self.name)
                return True
            else:
                return False

        def print_budget (self):
            len_name = len(self.name)
            rounded = []
            descriptions = []
            line = ''
            for v in self.ledger:
                newV = round(v[0], 2)
                newV = '{:.2f}'.format(newV)
                space = ''
                for i in range(30 - len(v[1]) - len(newV)):
                    space = space + ' '
                rounded.append((newV, v[1], space))

            for i in range(15 - len_name//2):
                line = line + '*'
            pr_budget = line + self.name + line + '\n'

            for v in rounded:
                #print(v)
                pr_budget = pr_budget + '{:}{:}{:>}\n'.format(v[1][:24], v[2], v[0][:8])
            pr_budget = pr_budget + 'Total: {:.2f}\n'.format(self.get_balance())
            return pr_budget
        def __str__ (self):
            return self.print_budget()
def create_spend_chart(categories):
    Values = []
    binValues = []
    Rows = []
    maxName = 0
    for budget in categories:
        bw_sum = 0
        bd_sum = 0
        for amount in budget.ledger:
            if amount[0] < 0:
                bw_sum = bw_sum + amount[0]
        bd_sum = budget.get_balance() - bw_sum
        pmoney_S = int((bw_sum * -10) // bd_sum)
        if len(budget.name) > maxName:
            maxName = len(budget.name)
        Values.append((budget.name, pmoney_S))
    for value in Values:
        AbiValue = []
        for cell in range(11):
            if cell in range(value[1] + 1):
                AbiValue.append('O')
            else:
                AbiValue.append(' ')
        binValues.append(AbiValue)
    #print(binValues)
    for v in range(12):
        space = ''
        if v == 11:
            line = '    '
            for l in range(len(binValues)):
                line = line + '--'
            Rows.append(line)
            break
        elif v > 0:
            space = ' '
        row = space + str(10 - v) + ' | '
        for bV in binValues:
            row = row + bV[10 - v] + ' '
        Rows.append(row)
    for cell in range(maxName):
        row = '     '
        for n in Values:
            try:
                l = n[0][cell]
            except:
                l = ' '
            row = row + l + ' '
        Rows.append(row)
    for r in Rows:
        print(r)


food = Category('Food')
food.deposit(100, 'Initial deposit')
food.withdraw(30, 'groceries')
food.withdraw(40, 'hamburger')
food.withdraw(30, 'Maicitos')
food.withdraw(30, 'lemon')
clothing = Category('Clothing')
clothing.deposit(100, 'Initial deposit')
clothing.withdraw(90, 'CR7 tenis')
clothing.withdraw(10, 'T-shirt')
clothing.deposit(100, 'Sunday pay')
print(food, clothing)
create_spend_chart([food, clothing])
