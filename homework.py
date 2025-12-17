import time
print("Start", flush=True)
for i in range(5):
    print(f"Line {i}", flush=True)
    time.sleep(0.5)
print("End", flush=False)


import numpy as np
import matplotlib.pyplot as plt
print("Python + VS code is working")

print(np.array([1,2,3]))

x=np.random.rand(5)

plt.stem(x)
plt.show()