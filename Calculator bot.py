import math

def calculator_bot():
    while True:
        print("\nCalculator Menu")
        print("""
        1. Addition (+)
        2. Subtraction (-)
        3. Multiplication (*)
        4. Division (/)
        5. Power (x^y)
        6. Square Root
              """)
        sec_num = int(input("Enter number to choose a operation (1-6) : "))
        
        while sec_num < 1 or sec_num > 6:
            print("This number of operation have not in the bot.")
            sec_num = int(input("Enter number to choose a operation : "))
            
        if sec_num == 6:
            num = int(input("Enter number : "))
            ans = int(math.sqrt(num)) 
            print("Answer : ", ans)
        else:
            num1 = int(input("Enter first number : "))
            num2 = int(input("Enter second number : "))
            
            if sec_num == 1:
                ans = num1 + num2
                print("Answer : ", ans)
            elif sec_num == 2:
                ans = num1 - num2
                print("Answer : ", ans)
            elif sec_num == 3:
                ans = num1 * num2
                print("Answer : ", ans)
            elif sec_num == 4:
                if num2 == 0:
                    print("Wrong! Cannot divide by zero.")
                else:
                    ans = num1 // num2 
                    print("Answer : ", ans)
            elif sec_num == 5:
                ans = int(math.pow(num1, num2))
                print("Answer : ", ans)
                
        more_sec = input("Are you calculate next? (Y/N) : ").upper()
        if more_sec == "Y":
            continue
        else:
            print("Thanks you for using this bot! Happy day!")
            break

def start():
    print("Welcome to Calculator bot!\nI'm Math Bot.")
    
    while True:
        
        user = input("\nEnter your message: ").lower()
        
        
        if ("hello" in user) or ("hi" in user ) or ("hey" in user):
            
            print("Hello friend. What can I help you?")
           
        elif ("calculate" in user) or ("math" in user) or ("calculator" in user):
            
            calculator_bot()
            
        elif "break" in user:
            
            print("Ok. You break this bot. Thank you for using the bot!")
            break
            
        else:
            print("Please type again.")

start()
    
