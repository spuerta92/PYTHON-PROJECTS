# Future Value
# Sebastian Puerta

def future_value():
    principal = eval(input("Enter principal: "))
    apr = eval(input("Enter annual interest rate: " ))
    fw = 0
    for i in range(10):
        fw = fw + (principal * (1 + apr))
    print("Future Worth of your investment: ", fw)

def main():
    future_value()

main()
