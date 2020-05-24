import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10):
    vetor.append(random.randint(0, 50))

plt.boxplot(vetor)
plt.show()
