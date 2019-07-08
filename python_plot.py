import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(8,5))
x = np.linspace(0,2*np.pi,1000)
y = np.cos(x)
ax.plot(x,y)
ax.set_xlim(0,2*np.pi)
fig.tight_layout()



