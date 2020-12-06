# https://docs.python.org/3.1/library/random.html
# https://blog.csdn.net/weixin_41571493/article/details/80549833

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(1)
print(np.random.rand(4,3))

np.random.seed(0)
print(np.random.rand(4,3))

np.random.seed(2)
print(np.random.rand(10))

np.random.seed(3)
print(np.random.rand(10))



