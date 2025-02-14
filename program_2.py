# Author: Michael Beaudet 
# Title: Week 4 program 2
# Date: 2/13/25

def main(): 

    total_tickets = 0  

    while True:
        movie = input("Enter the movie name (or type 'done' to finish): ")
        
        if movie.lower() == 'done':  
            break
        
        tickets = int(input("How many tickets? "))
        total_tickets += tickets  

    print(f"Your Total is: {total_tickets}")



if __name__ == '__main__':
    main()