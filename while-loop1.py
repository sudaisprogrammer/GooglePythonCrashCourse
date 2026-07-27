
def check_attempts(password):
    total_attempts = 4
    x = 1
    
    while(True):
        mypass = input("enter password: ")
        if(mypass!=password):
            print("incorrect password");
            print("remaining attempts are "+str(total_attempts-(x+1)))
            x+=1;
        else:
            print("password mathced in ",x," attempts ")
            break;

check_attempts("pass123")
