class Ret:
    def __init__(self,length=1,width=2):
        self.length = length
        self.width = width
    def set_length(self,leng):
        self.length = leng
    def get_length(self):
        return self.length
    def set_width(self,wid):
        self.width = wid
    def get_width(self):
        return self.width
a = Ret()
d,e  = input("ENTER ").split(" ")
a.set_length(d)
a.set_width(e)
print(a.get_length())
print(a.get_width())