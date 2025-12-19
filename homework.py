import time
print("Start", flush=True)
t=[]
for i in range(5):
    print(f"Line {i}", flush=True)
    time.sleep(1)
    t.append( i)
print("End", flush=False)
print ("time_sleep=",t)

import numpy as np
import matplotlib.pyplot as plt
print("Python + VS code is working")

print(np.array([1,2,3]))

x=np.random.rand(5)

plt.stem(x)

plt.title("A simple plot")
plt.show()