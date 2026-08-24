import numpy as np
import matplotlib.pyplot as plt

class HexagonoInterativo:
    def __init__(self):
        self.letras = ['A', 'B', 'C', 'D', 'E', 'F']
        self.valores = [1024, 2048, 1536, 768, 2816, 1600]  # só para rótulos
        
        angulos = np.linspace(0, 2 * np.pi, 7)[:-1]
        a, b = 6, 4
        self.pontos = np.array([[a * np.cos(ang), b * np.sin(ang)] for ang in angulos])

        self.dragging_point = None

        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.ax.set_aspect('equal')
        self.ax.grid(True)
        self.ax.set_title('Hexágono Interativo - Arraste os pontos azuis')

        self.pontos_plot, = self.ax.plot(self.pontos[:,0], self.pontos[:,1], 'bo', ms=10, picker=5)
        self.hex_lines, = self.ax.plot([], [], 'b-', lw=2, label='Hexágono')
        self.diag_lines = [self.ax.plot([], [], 'r--', lw=2)[0] for _ in range(3)]
        self.texts = []
        self.intersecao_plot = self.ax.scatter([], [], color='green', s=100, zorder=10, label='Interseção')

        self._update_plot()

        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)

        self.ax.legend()
        plt.show()

    def _update_plot(self):
        # Atualizar hexágono
        xs = list(self.pontos[:,0]) + [self.pontos[0,0]]
        ys = list(self.pontos[:,1]) + [self.pontos[0,1]]
        self.hex_lines.set_data(xs, ys)

        # Atualizar diagonais
        pares_opostos = [(0,3), (1,4), (2,5)]
        intersecoes = []
        for i, (i1, i2) in enumerate(pares_opostos):
            p1 = self.pontos[i1]
            p2 = self.pontos[i2]
            self.diag_lines[i].set_data([p1[0], p2[0]], [p1[1], p2[1]])
            intersecoes.append((p1, p2))

        # Calcular interseções
        inter1 = self.intersecao(intersecoes[0][0], intersecoes[0][1], intersecoes[1][0], intersecoes[1][1])
        inter2 = self.intersecao(intersecoes[1][0], intersecoes[1][1], intersecoes[2][0], intersecoes[2][1])
        inter3 = self.intersecao(intersecoes[0][0], intersecoes[0][1], intersecoes[2][0], intersecoes[2][1])

        if inter1 is not None and inter2 is not None and inter3 is not None:
            ponto_medio = (inter1 + inter2 + inter3) / 3
            self.intersecao_plot.set_offsets(ponto_medio)

            if hasattr(self, 'intersecao_text'):
                self.intersecao_text.set_position((ponto_medio[0] + 0.3, ponto_medio[1]))
                self.intersecao_text.set_text(f"({ponto_medio[0]:.2f}, {ponto_medio[1]:.2f})")
            else:
                self.intersecao_text = self.ax.text(
                    ponto_medio[0] + 0.3, ponto_medio[1], 
                    f"({ponto_medio[0]:.2f}, {ponto_medio[1]:.2f})", 
                    color='green', fontsize=10, fontweight='bold'
                )

            # 👉 Imprime ponto de interseção
            print(f"\nPonto de interseção: ({ponto_medio[0]:.4f}, {ponto_medio[1]:.4f})")
        else:
            self.intersecao_plot.set_offsets([])
            if hasattr(self, 'intersecao_text'):
                self.intersecao_text.set_text("")
            print("\nAs diagonais não se encontram (paralelas ou inválidas).")

        # Atualizar textos dos pontos
        for txt in self.texts:
            txt.remove()
        self.texts = []

        print("\nCoordenadas dos pontos do hexágono:")
        for i, (x, y) in enumerate(self.pontos):
            texto = f"{self.letras[i]}\n({x:.1f},{y:.1f})"
            self.texts.append(self.ax.text(x + 0.3, y, texto, fontsize=9))
            print(f"{self.letras[i]}: ({x:.4f}, {y:.4f})")

        self.fig.canvas.draw_idle()

    def intersecao(self, p1, p2, p3, p4):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
        if denom == 0:
            return None
        px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
        py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
        return np.array([px, py])

    def on_pick(self, event):
        if event.artist == self.pontos_plot:
            ind = event.ind[0]
            self.dragging_point = ind

    def on_motion(self, event):
        if self.dragging_point is None or event.xdata is None or event.ydata is None:
            return
        self.pontos[self.dragging_point] = [event.xdata, event.ydata]
        self._update_plot()

    def on_release(self, event):
        self.dragging_point = None

if __name__ == "__main__":
    HexagonoInterativo()
