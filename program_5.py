# Author: Michael Beaudet
# Title: Week 4 Program 5
# Date 2/14/25

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         
    total = 0.0

    budget = float(input('Enter the budget for this month: '))

    while True:
        spent = float(input('Enter an amount you have spent (or type 0 to finish): '))

        if spent == 0:
            break
        total += spent
    difference = total - budget 
    
    if difference < 0:
        print(f'You are under budget by: ${difference:.2f}')
    elif difference > 0: 
        print(f'You are over budget by: ${difference:.2f}')
    else:
        print('Congrats you are exactly on the budget!')
    
if __name__ == '__main__':
    main()