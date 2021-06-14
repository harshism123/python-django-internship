from os import set_inheritable


class publisher:
    title = "jack dorsey"
    def display(self):
        print("name : ",self.title,"\n")
class book(publisher):
    pages = 350
    def display(self):
        print("name ",self.title)
        print("pages",self.pages, "\n")
class new(book)
    time = 3
    def display("self"):
        print("name : ", self.title)
        print("pages :",self.pages)
        print("time : {} hrs",format(self.time),"\n")
    
obj1 = publisher()
obj2 = book()
obj3 = new()
print("-------publisher class---------")
obj1.display()
print("-------book class--------")
obj2.display()
print("--------new class-------")
obj3.display()