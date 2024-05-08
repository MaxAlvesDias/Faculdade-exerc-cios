import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation, FFMpegWriter 

plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\maxpn\\Documents\\ffmpeg\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe'

# Função para resolver o problema das Torres de Hanói
def hanoi(n, origem, destino, auxiliar):
    if n > 0:
        # Move n - 1 discos da haste de origem para a haste auxiliar
        hanoi(n - 1, origem, auxiliar, destino)
        
        # Move o disco restante da haste de origem para a haste de destino
        print(f'Move disco {n} de {origem} para {destino}')
        
        # Move n - 1 discos da haste auxiliar para a haste de destino
        hanoi(n - 1, auxiliar, destino, origem)

# Função para construir a árvore de chamadas recursivas
def build_call_tree(n):
    G = nx.DiGraph()
    build_call_tree_recursive(G, n, 'Origem', 'Destino', 'Auxiliar')
    return G

# Função recursiva para construir a árvore de chamadas recursivas
def build_call_tree_recursive(G, n, origem, destino, auxiliar, parent=None, num_etapa=0):
    if n > 0:
        num_etapa += 1
        current_node = f'Move disco {n} de {origem} para {destino}\n(Etapa {num_etapa})'
        G.add_node(current_node)
        if parent is not None:
            G.add_edge(parent, current_node)
        build_call_tree_recursive(G, n - 1, origem, auxiliar, destino, current_node, num_etapa)
        build_call_tree_recursive(G, n - 1, auxiliar, destino, origem, current_node, num_etapa)


# Função para atualizar a posição da "bolinha" e as arestas na animação
def update_animation(frame):
    ax.clear()
    if frame < len(animation_path):
        current_position = animation_path[frame]
        nx.draw(arvore, pos, with_labels=True, node_color='lightblue', node_size=1500, ax=ax, font_size=8)
        if current_position in steps_with_movement:
            # Se o quadro atual corresponde a uma etapa com movimento, desenhe a "bolinha" em amarelo
            nx.draw_networkx_nodes(arvore, pos, nodelist=[current_position], node_color='yellow', node_size=1500, ax=ax)
        else:
            # Caso contrário, desenhe a "bolinha" em vermelho
            nx.draw_networkx_nodes(arvore, pos, nodelist=[current_position], node_color='red', node_size=1500, ax=ax)
        if frame > 0:
            prev_position = animation_path[frame - 1]
            nx.draw_networkx_edges(arvore, pos, edgelist=[(prev_position, current_position)], width=2, edge_color='red', ax=ax)
        plt.title(f'Bolinha na etapa {frame + 1}')
    else:
        anim.event_source.stop()

# Constrói a árvore de chamadas para a Torre de Hanói com 5 discos
arvore = build_call_tree(5)
pos = nx.spring_layout(arvore, seed=42)

# Calcula o caminho de animação (simula o movimento da "bolinha" na árvore)
animation_path = list(nx.dfs_preorder_nodes(arvore))

steps_with_movement = ['Move disco 1 de Origem para Destino\n(Etapa 1)',
                       'Move disco 2 de Origem para Auxiliar\n(Etapa 2)',
                       'Move disco 1 de Destino para Auxiliar\n(Etapa 3)',
                       'Move disco 3 de Origem para Destino\n(Etapa 4)',
                       'Move disco 1 de Auxiliar para Origem\n(Etapa 5)',
                       'Move disco 2 de Auxiliar para Destino\n(Etapa 6)',
                       'Move disco 1 de Origem para Destino\n(Etapa 7)',
                       'Move disco 4 de Origem para Auxiliar\n(Etapa 8)',
                       'Move disco 1 de Destino para Auxiliar\n(Etapa 9)',
                       'Move disco 2 de Destino para Origem\n(Etapa 10)',
                       'Move disco 1 de Auxiliar para Origem\n(Etapa 11)',
                       'Move disco 3 de Destino para Auxiliar\n(Etapa 12)',
                       'Move disco 1 de Origem para Destino\n(Etapa 13)',
                       'Move disco 2 de Origem para Auxiliar\n(Etapa 14)',
                       'Move disco 1 de Destino para Auxiliar\n(Etapa 15)',
                       'Move disco 5 de Origem para Destino\n(Etapa 16)',
                       'Move disco 1 de Auxiliar para Origem\n(Etapa 17)',
                       'Move disco 2 de Auxiliar para Destino\n(Etapa 18)',
                       'Move disco 1 de Origem para Destino\n(Etapa 19)',
                       'Move disco 3 de Auxiliar para Origem\n(Etapa 20)',
                       'Move disco 1 de Destino para Auxiliar\n(Etapa 21)',
                       'Move disco 2 de Destino para Origem\n(Etapa 22)',
                       'Move disco 1 de Auxiliar para Origem\n(Etapa 23)',
                       'Move disco 4 de Auxiliar para Destino\n(Etapa 24)',
                       'Move disco 1 de Origem para Destino\n(Etapa 25)',
                       'Move disco 2 de Origem para Auxiliar\n(Etapa 26)',
                       'Move disco 1 de Destino para Auxiliar\n(Etapa 27)',
                       'Move disco 3 de Origem para Destino\n(Etapa 28)',
                       'Move disco 1 de Auxiliar para Origem\n(Etapa 29)',
                       'Move disco 2 de Auxiliar para Destino\n(Etapa 30)',
                       'Move disco 1 de Origem para Destino\n(Etapa 31)']

# Cria a animação
fig, ax = plt.subplots()
anim = FuncAnimation(fig, update_animation, frames=len(animation_path) * 3, interval=1000)
plt.axis('off')

# Salva a animação em um arquivo MP4
writer = FFMpegWriter(fps=1000, metadata=dict(artist='Me'), bitrate=1800)
anim.save('animation.mp4', writer=writer)

plt.show()
