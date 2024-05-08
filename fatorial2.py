import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Função para calcular o fatorial de um número n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Função para criar a animação
def update(frame):
    global balls
    if frame < len(balls):
        ax.clear()
        ax.axis('off')
        ax.set_xlim(0, len(balls) * 2)
        ax.set_ylim(0, len(balls) + 2)

        for i, ball in enumerate(balls[:frame + 1]):
            ax.text(i * 2 + 1, len(balls) + 1, str(ball), ha='center', fontsize=12)
            ax.add_patch(plt.Circle((i * 2 + 1, len(balls) - ball + 1), 0.5, color='blue'))
            # Mostra o resultado do fatorial de cada bola
            ax.text(i * 2 + 1, len(balls) - ball + 0.5, f'{factorial(ball)}', ha='center', fontsize=10)

        # Plotando as linhas entre os pontos
        for i in range(len(balls) - 1):
            x_values = [i * 2 + 1, (i + 1) * 2 + 1]
            y_values = [len(balls) - balls[i] + 1, len(balls) - balls[i + 1] + 1]
            ax.plot(x_values, y_values, color='black')

# Número para calcular o fatorial
n = 5

# Lista de bolas representando cada valor de n
balls = list(range(1, n + 1))

# Cria a figura e o eixo
fig, ax = plt.subplots()

# Criação da animação
anim = FuncAnimation(fig, update, frames=range(1, n + 1), interval=1000, repeat=False)

# Exibição da animação
plt.show()

