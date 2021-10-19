import  pandas as pd
import  numpy as np





s = pd.Series(np.arange(1,11), index = list('abcdefghij'))
s_head = s.head()
s_tail = s.tail()
print(f"s is {s}, s_head is {s_head}, s_tail is {s_tail}")
s_head = s.head(n=3)
s_tail = s.tail(3)
print(f"s_head is {s_head}, s_tail is {s_tail}")
s_take = s.take([1,3,5])
print(f"s_take is {s_take}")
s = pd.Series(np.arange(100,110), index = np.arange(1,11))
print(f"s is {s}, s[1:6] is {s[1:6]}")
print(f"s.iloc[[1,2,3,4,5]] is {s.iloc[[1,2,3,4,5]]}")
print(f"s[1:6:2] is {s[1:6:2]}")
print(f"s[:5] is {s[:5]} and s.head() is {s.head()}")
print(f"s[4:] is {s[4:]}")
print(f"s[:5:2] is {s[:5:2]}")
print(f"s[4::2] is {s[4::2]}")
print(f"s[::-1] is {s[::-1]}")
print(f"s[4::-2] is {s[4::-2]}")
print(f"s[-4:] is {s[-4:]}")
print(f"s[:-4] is {s[-4:]}")
print(f"s[-4:-1] is {s[-4:-1]}")