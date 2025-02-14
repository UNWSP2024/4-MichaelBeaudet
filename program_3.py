# Author: Michael Beaudet
# Title: Week 4 Program 3
# Date: 2/14/25

def main():

    years = int(input('Enter the amount of years: '))  

    total_months = 0
    total_rainfall = 0 

    for year in range(years):
        for month in range(1, 13):
            rainfall = float(input(f'Enter the inches of rain for month {month}: '))
            total_rainfall += rainfall 
            total_months += 1 

    average_rainfall = total_rainfall / total_months

    print(f'Total months: {total_months}')
    print(f'Total rain: {total_rainfall:.2f} inches')
    print(f'Average rain per month: {average_rainfall:.2f} inches')

if __name__ == '__main__':
    main()