import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



def graph(F,pontos):
    interval   = np.linspace(-1*abs(min(pontos)),1+abs(max(pontos)),100)
    
    valores_fx = []
    for x in interval: valores_fx.append(F(x))
    
    valores_pfx = []
    for x in pontos:   valores_pfx.append(F(x))

    plt.figure(figsize =(10, 6))
    plt.plot(list(interval),valores_fx,color='purple')
    plt.axhline(0, color='black'); plt.axvline(0, color='black')
    plt.scatter(pontos,valores_pfx,marker='8',color='red',alpha = 0.65)
    plt.scatter(pontos,valores_pfx,marker='8',color='red',alpha = 0.1)
    plt.axhline(0, color='black'); plt.axvline(0, color='black')
    
    return plt.gcf()    




def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

