#More Matplotlib examples

import matplotlib.pyplot as plt
from random import choice


plt.rc('figure',figsize=(12,6))

values = list(range(0,55,5))
values

plt.plot(values)
plt.show()
