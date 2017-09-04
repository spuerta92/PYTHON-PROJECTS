# Even numbers
# Sebastian Puerta Hincapie

def find_evens(data,length):
    arr_evens = []
    for i in range (0,length):
        x = data[i] % 2;
        if(x == 0):
            arr_evens.append(data[i])

    return arr_evens
    
        
def main():
    from random import randint
    arr = {}
    for i in range (0,10):
        arr[i] = randint(0,100)

    n = len(arr)
    for i in range (0,n):
        print(arr[i], " ", end = "")

    new_arr = find_evens(arr,n)
    print("")
    print(new_arr)
    
main()
