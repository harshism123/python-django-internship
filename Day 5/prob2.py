class arith:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def summation(self):
        return(self.num1 + self.num2)
    def subtract(self):
        return(self.num2 - self.num1)
    def multiply(self):
        return(self.num1 * self.num2)

n1 = int(input("number 1 :"))
n2 - int(input("number 2 :"))
calc = arith(n1,n2)
ans = calc.summation()
print("{} + {} = {}".format(n1,n2,ans))
ans = calc.subtract()
print("{} + {} = {}".format(n1,n2,ans))
ans = calc.multiply()
print("{} + {} = {}".format(n1,n2,ans))
