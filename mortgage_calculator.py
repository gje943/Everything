def cleanInput(amount):
    """ Converts user input to a float """
    return float("".join([char for char in amount if char.isdigit() or char == "."]))

class mortgageInfo(object):
    def __init__(self, house_value, deposit, term, interest_rate):
        self.mortgage = cleanInput(house_value) - cleanInput(deposit)
        self.term = cleanInput(term)
        self.interest_rate = cleanInput(interest_rate)/100
    
    def getMortgage(self):
        return self.mortgage
    
    def getTerm(self):
        return self.term

    def getInterestRate(self):
        return self.interest_rate         

    def getMonthlyPayments(self):
        i = self.getInterestRate() / 12
        n = 12 * self.getTerm()
        p = self.getMortgage()
        first_half = i*((1 + i)**n)
        second_half = ((1 + i)**n) - 1
        return p * (first_half / second_half)

    def getMortgagePlusInterest(self):
        period = self.getTerm() * 12
        return period * self.getMonthlyPayments()

    def getInterestPayable(self):
        return self.getMortgagePlusInterest() - self.getMortgage()
    

house_value = input("What's the total value of the house you intend to purchase?")
deposit = input("How much deposit are you putting down? ")
term = input("How long is your mortgage in years? ")
interest_rate = input("What interest rate has the bank offered? ")
print("------------------------------------")
info = mortgageInfo(house_value, deposit, term, interest_rate)
print("The total value of your mortgage with interest is: £{:,.2f}".format(info.getMortgagePlusInterest()))
print("The minimum monthly payment will be: £{:,.2f}".format(info.getMonthlyPayments()))
print("The total interest payable on your mortgage will be: £{:,.2f}".format(info.getInterestPayable()))



    
        




    

        

