# In this case, our goal is to find out exactly how much tip to provide after a service. In this case, you must request the total invoice. With this, we will apply the tip for 18%, 20% and 25%.

# The percentage of tip that will be charged to diners is calculated
bill = ''
while str(type(bill))!= "<class 'float'>":
    try:
        bill = float(input('What is the total bill for today please? '))
    except:
        pass
if bill > 0: tip = 18
if bill > 99.99999: tip = 20
if bill > 199.9999: tip = 25
# The number of diners is requested 
diners = ''
while str(type(diners))!= "<class 'int'>":
    try:
        diners = int(input('How many diners are they? '))
    except:
        pass
# The user is asked if they want to divide the account equally or if they prefer to use a different distribution
weighings = ''
choice = ''
while choice not in {'yes','no'}:
    choice = input('Do you want to split the bill equally, yes or no? ').lower()
    if choice == 'no':
        while len(weighings) != diners:
            weighings = input('Enter the percentages you want to divide the food into separated by commas and make sure they add up to 100% ').split(',')
            print(f'The tip applying {tip}% is ${round(bill*(tip/100),2)}, which accounts for a total of ${round(bill*(1 + tip/100),2)} and they get:')
            for i in range(len(weighings)):
                print(f'Diner {i+1} gets ${round(bill*(1 + tip/100)*(float(weighings[i])/100),2)}')
    if choice == 'yes':
        print(f'The tip applying {tip}% is ${round(bill*(tip/100),2)}, which accounts for a total of ${round(bill*(1 + tip/100),2)} and they get {round(bill*(1 + tip/100)*(1/diners),2)}')
