import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from   matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from   sympy   import *
from   Metodos import * 
from   Frames  import *
from   Plotando  import *


def condicionais(values):
    if   values['bissecao']==True and values['falsa']==False and values['newton']==False and values['secante']==False:
        return 1
    elif values['bissecao']==False and values['falsa']==True and values['newton']==False and values['secante']==False:
        return 2
    elif values['bissecao']==False and values['falsa']==False and values['newton']==True and values['secante']==False:
        return 3
    elif values['bissecao']==False and values['falsa']==False and values['newton']==False and values['secante']==True:
        return 4
    else: return 5

    


def main():
    fig = None
    x   = Symbol('x')
    window = frams()

    while True:
        event, values = window.read()   
        fx  = values['fx'] 
        dfx = diff(fx,x)

        F  = lambdify(x,fx)
        DF = lambdify(x,dfx)
        
        
        if event == sg.WIN_CLOSED or event == 'Sair ':  break

        if event == ' Ok ':
            if fig != None: fig.get_tk_widget().forget()


            booleano = condicionais(values)
            match (booleano):

                case 1:
                    a   = float(values['a'])
                    b   = float(values['b'])
                    eps = 1/10**values['eps']

                    dados = Bissecao2(F,a,b,eps)            
                    window['fx1' ].update('Fx ='+str(F(dados[0])))
                    window['x'   ].update('x  ='+str(dados[0]))
                    window['x1'  ].update('x1 ='+str(dados[1]))
                    window['x2'  ].update('x2 ='+str(dados[2]))
                    window['itr' ].update('iter ='+str(dados[3]))
                    window['intx'].update('Intervalx ='+str(dados[4]))
            
            
                    fig = draw_figure(
                        window['plota'].TKCanvas,graph(F,dados[5])
                    )


                case 2:
                    a    = float(values['a'])
                    b    = float(values['b'])
                    eps  = 1/10**values['eps']
                    iter = int(values['maxit'])

                    dados = method_falseposicao(F,a,b,eps,iter)
                    window['fx1' ].update('Fx ='+str(F(dados[0])))
                    window['x'   ].update('x  ='+str(dados[0]))
                    window['x1'  ].update('x1 ='+str(dados[1]))
                    window['x2'  ].update('x2 ='+str(dados[2]))
                    window['itr' ].update('iter ='+str(dados[3]))
                    window['intx'].update('Intervalx ='+str(dados[4]))

                    fig = draw_figure(
                        window['plota'].TKCanvas,graph(F,dados[5])
                    )



                case 3:
                    a     = float(values['a'])
                    eps   = 1/10**values['eps']
                    dados = Newton(F,DF,a,eps)

                    window['fx1'].update('Fx ='+str(F(dados[0])))
                    window['x'  ].update('x  ='+str(dados[0]))
                    window['x1' ].update('x1 ='+str(dados[1]))
                    window['x2' ].update('iter ='+str(dados[2]))
                    window['itr'].update('Intervalx ='+str(dados[3]))

                    fig = draw_figure(
                        window['plota'].TKCanvas,graph(F,dados[4])
                    )



                case 4:
                    a    = float(values['a'])
                    b    = float(values['b'])
                    eps  = 1/10**values['eps']
                    dados = Secant(F,a,b,eps)

                    window['fx1'].update('Fx ='+str(F(dados[0])))
                    window['x'  ].update('x  ='+str(dados[0]))
                    window['x1' ].update('x1 ='+str(dados[1]))
                    window['x2' ].update('x2 ='+str(dados[2]))
                    window['itr'].update('Iter ='+str(dados[3]))
                    window['intx'].update('Intervalx ='+str(dados[4]))

                    fig = draw_figure(
                        window['plota'].TKCanvas,graph(F,dados[5])
                    )



                case 5:
                    sg.theme("DefaultNoMoreNagging")
                    sg.popup("Demasiados metodos",
                                font='calibri'  ,
                                text_color='red',
                                button_type=5   ,
                                non_blocking=True,
                                no_titlebar=True ,
                                auto_close=True  ,
                                auto_close_duration=3)

            
            
        
            
if __name__ == "__main__":
    main()