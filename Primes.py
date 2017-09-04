# Prime Numbers
# Sebastian Puerta Hincapie

def find_primes(data,length):
    arr_primes = []
    return arr_primes

def prime():
    # for values greater than 2
    # this implementation does not handle values less than 3
    # fixed 3 to n
    from random import randint
    n = 100;
    while(True):
        rand = randint(3,n)
        if(rand < 3 or (rand%2 == 0)): continue
        elif((rand%2) != 0): break
    return rand
        
def main():
##    from random import randint
##    arr = []
##    new_arr = []
##    for i in range (0,10):
##        arr[i] = randint(0,100)
##
##    n = len(arr)
##    for i in range (0,n):
##        print(arr[i], " ", end = "")

    x = prime()
    y = prime()
    z = x + y
    print(x, " + ", y, " = ", z)
    
main()
