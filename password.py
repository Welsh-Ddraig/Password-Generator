from random import randint

ALPHABET = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
SPECIAL_CHARACTER = [",","!","@","#","$","%","^","&","*","(",")","-","_","=","+"]

def main():
    
    password_length = int(input("How long would you like your password? "))
    count = password_length
    alpha_or_special = randint(1,2)
    
    password = ""
    while count != 0:
        if alpha_or_special == 1:
    
                password = password + ALPHABET[randint(0,51)]
                count = count - 1
        else:
    
                password = password + SPECIAL_CHARACTER[randint(0, 14)]
                count = count - 1  
        alpha_or_special = randint(1,2)
    print(password)          
            
main()
