from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
def f(x1, x2): return 100*(x2-x1**2)**2+(x1-1)**2
x1 = np.linspace(-5, 10)
x2 = np.linspace(-5, 10)
X1, X2 = np.meshgrid(x1, x2)
F = f(x1, x2)
plt.contour(X1, X2, f(X1, X2))

def plotter(E, A):
  fig = plt.figure(figsize = [12, 8])
  ax = plt.axes(projection='3d')
  ax.plot_surface(X1, X2, f(X1, X2), cmap='jet', alpha=0.8)
  ax.plot_wireframe(X1, X2, f(X1, X2), rcount=15, ccount=15)
  ax.view_init(elev=E, azim=A)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('f(X, Y)')
  ax.contourf(x1, x2, f(X1, X2))
  print("solution 2")
plotter(45, 45)
from ipywidgets import interactive
iplot = interactive(plotter, E = (-90, 90, 5),
                             A = (-90, 90, 5))
iplot