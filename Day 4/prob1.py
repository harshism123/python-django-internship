class cal1:
    n1=n2=n3=0
    def setdata(self,n1,n2,n3):
        self.n1= n1
        self.n2= n2
        self.n3= n3

    def display(self):
        total = n1 + n2 + n3
        print(n1,'+',n2,'+',n3,"=",total)

calc = cal1()
n1 = int(input("enter first nunber :"))
n2 = int(input("enter second number :"))
n3= int(input("enter third number :"))
calc.setdata(n1,n2,n3)
calc.display()
