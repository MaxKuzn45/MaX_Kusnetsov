# дз 9.1
import numpy as np
import matplotlib.pyplot as plt

def f(x, alpha, beta):
    if x == 0 and beta >=0:
        return np.inf if alpha > 0 else -np.inf if alpha <0 else 0
    if x == 0 and beta < 0:
        return 0

    if x == 0 and alpha == 0 and beta == 0:
        return np.nan
    if x == 0 and alpha == 0:
        return 0
    if x == 0 and beta == 0:
        return 1
    if abs(x) < 1e-15:
        return 1 + (alpha/abs(x))**beta
    return (x**beta + alpha**beta) / x**beta
x = np.linspace(0.1, 10, 500)

plt.figure(figsize=(12, 8))
plt.plot(x, f(x, 1, 1), label='α=1, β=1')
plt.plot(x, f(x, 2, 1), label='α=2, β=1')
plt.plot(x, f(x, 1, 2), label='α=1, β=2')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График x>0')
plt.legend()
plt.grid(True)

plt.figure(figsize=(12, 8))
ax1 = plt.axes([0.1, 0.1, 0.8, 0.8])
ax2 = plt.axes([0.1, 0.6, 0.3, 0.3])
ax3 = plt.axes([0.6, 0.6, 0.3, 0.3])

ax1.plot(x, f(x, 1, 1), label='α=1, β=1')
ax1.plot(x, f(x, 2, 1), label='α=2, β=1')
ax1.plot(x, f(x, 1, 2), label='α=1, β=2')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_title('Графики x>0')
ax1.legend()
ax1.grid(True)

x_small = np.linspace(0.01, 0.5, 100)
ax2.plot(x_small, f(x_small, 1, 1), label='α=1, β=1')
ax2.plot(x_small, f(x_small, 2, 1), label='α=2, β=1')
ax2.plot(x_small, f(x_small, 1, 2), label='α=1, β=2')
ax2.set_title('малые x')
ax2.grid(True)

x_large = np.linspace(5, 100, 100)
ax3.plot(x_large, f(x_large, 1, 1), label='α=1, β=1')
ax3.plot(x_large, f(x_large, 2, 1), label='α=2, β=1')
ax3.plot(x_large, f(x_large, 1, 2), label='α=1, β=2')
ax3.set_title('большие x')
ax3.grid(True)
plt.show()
# дз 9.2

x_neg = np.linspace(-10, -0.1, 500)

plt.figure(figsize=(10,6))
plt.plot(x_neg, f(x_neg, 1, 1), label='α=1, β=1')
plt.plot(x_neg, f(x_neg, 2, 1), label='α=2, β=1')
plt.plot(x_neg, f(x_neg, 1, 2), label='α=1, β=2')
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.8)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Графики x < 0')
plt.legend()
plt.grid(True)

plt.show()

# дз 9.3
x = np.linspace(0.1,10,500)
plt.figure(figsize=(10,6))
plt.plot(x,f(x,1,0.5), label='α=1, β=0.5')
plt.plot(x,f(x,1,-0.5), label='α=1, β=-0.5')
plt.plot(x,f(x,1,-1.5), label='α=1, β=-1.5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График β')
plt.legend()
plt.grid(True)
plt.show()

#дз 9.4
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
x = np.linspace(0.1, 10, 500)
plt.plot(x, f(x, 1, 0.5), label='α=1, β=0.5')
plt.plot(x, f(x, 1, 0.8), label='α=1, β=0.8')
plt.plot(x, f(x, 1, 0), linestyle='--', color='b', label='α=1, β=0')
plt.plot(x, f(x, 1, -1), linestyle='--', color='r', label='α=1, β=-1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График 1')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(x, f(x, 1, -0.5), label='α=1, β=-0.5')
plt.plot(x, f(x, 1, -0.8), label='α=1, β=-0.8')
plt.plot(x, f(x, 1, 0), linestyle='--', color='b', label='α=1, β=0')
plt.plot(x, f(x, 1, -1), linestyle='--', color='r', label='α=1, β=-1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График 2')
plt.legend()
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(x, f(x, 1, -1.5), label='α=1, β=-1.5')
plt.plot(x, f(x, 1, -2.5), label='α=1, β=-2.5')
plt.plot(x, f(x, 1, 0), linestyle='--', color='b', label='α=1, β=0')
plt.plot(x, f(x, 1, -1), linestyle='--', color='r', label='α=1, β=-1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График 3')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()