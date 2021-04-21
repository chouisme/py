class Person:                                  #odject is the instance of the class #class由attributos屬性、function組成
    def __init__(self,name,weight,hp,ap):      #self目前執行的物件   #物件所在位置(class Person)   #__init__建構子
       self.name = name                        #屬性
       self.weight =weight 
       self.hp =hp 
       self.ap =ap
    def eat(self):
        self.weight=self.weight-1
    def run(self,time):
        self.weight=self.weight-time*0.5
    def ua(self,me,tmp):
        self.hp=self.hp-tmp.ap

lee =Person("BBB",50,100,10)
handsome=Person("AAA",80,120,20)
print(lee.hp)
lee.ua(lee,handsome)
print(lee.hp)



#name(AAA)、weight(80)
#print(handsome)
#print(handsome.name)
#print(handsome.weight)

handsome.eat()
handsome.run(2)
handsome.run(2)

print(handsome.weight)


#print(lee)
#print(lee.name)
#print(lee.weight)