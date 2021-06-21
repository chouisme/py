import threading  
                                            #執行續 (thread) a light weighted process  

def set_interval(func,sec):
    def func_wrapper():
        set_interval(func,sec)
        func()
    t = threading.Timer(sec,func_wrapper)
    t.start()
    return t
def call():
    print("hi")
set_interval(call,3)