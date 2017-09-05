'''
> Fibonacci Sequence
> Sum of Cubes
Sebastian Puerta Hincapie
'''

#function to determine the Nth value of fibonacci sequence given an input value
def fibonacci_sequence(n):
    # precondition: make sure that passed value is greater or equal to 2
    # postcondition: if passed value is greater than 2 then create a fibonacci
    # sequence and print out the nth value along with the sequence
    if(n < 2):  result = 1;
    else:
        #seeds within array
        sequence = [0,1]
        i = 2
        while(i <= n):
            sequence.append(sequence[i-1] + sequence[i-2])
            result = sequence[i]
            i += 1
            print("Sequence: ", sequence)
        
    print("Nth value: ", result)

# function to find the next Nth value
def fibonacci_recursion(n):
    if(n < 2):  return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)

# function to determine sum of the cubes of the first n natural numbers        
def fibonacci_cube_sum(n): 
    if(n < 2):  return 1
    else:
        #seeds within array
        sequence = [0,1]
        i = 2
        while(i <= n):
            sequence.append(sequence[i-1] + sequence[i-2])
            result = sequence[i]
            i += 1
        for k in range (0,len(sequence)):
            if(sequence[k] > 0):
                sequence[k] = pow(sequence[k],3)
        print("Cube Sum: ", sum(sequence))

# main       
def main():
    # Safety condition to numbers under 30, for time purposes
    # compilation would take longer for bigger numbers
    
    while(True):
        print("PART 1")
        print("Restricted to value <= 30...for time purposes")
        # user input, makes sure that it is a whole number integer
        value = round(eval(input("Please enter an integer number: ")))
        if(value > 30): continue
        else: break

    print("At n = ", value)
    fibonacci_sequence(value)

    # recursion to get the following value
    x = fibonacci_recursion(value)
    print("next Nth value: ", x)
    print()

    print("PART 2")
    y = fibonacci_cube_sum(value)
    if(y == 1): print("Cube sum: ", y)
    
    # end of program
    print()
    print("- End of program")

# are we being executed?
if __name__ == '__main__':
    main()
