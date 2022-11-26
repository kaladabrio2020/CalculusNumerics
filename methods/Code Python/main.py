import PySimpleGUI as sg
import matplotlib.pyplot as plt
from   matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from   sympy   import *
from   Metodos import * 
from   Frames  import *
from   Metodos_plot  import *


    


def main():
    df  = a = b = eps = iter = None
    fig = None
    x   = Symbol('x')
    window = methods_numerics()

    while True:
        event, values = window.read()  
        
        if event == sg.WIN_CLOSED or event == 'Cancel':  break
        
        if event == ' Ok ':
            
            fx  = values['fx'] 
            dfx = diff(fx,x)
            F  = lambdify(x,fx)
            DF = lambdify(x,dfx)
            
            if fig != None: fig.get_tk_widget().forget()
        
            
            if (values['b']==''): values['b'] = float(values['a'])+2
             
            a   = float(values['a'])
            b   = float(values['b'])
            eps = 1/10**values['eps']
            iter = int(values['maxit'])
            
            
            match (values['type']):

                case 'Bissecção':                   
                    df  = Bissecao(F,a,b,eps)           
                    dados = df.loc[len(df.index)-1].tolist()
                    
                    
                    window['fx1' ].update('Fx ='+str(dados[1]))
                    window['x'   ].update('x  ='+str(dados[5]))
                    window['x1'  ].update('x1 ='+str(dados[2]))
                    window['x2'  ].update('x2 ='+str(dados[3]))
                    window['itr' ].update('iter ='+str(dados[0]))
                    window['intx'].update('Intervalx ='+str(dados[4]))
                    
                    window['tab'].update(values=df.values.tolist())
                    fig = draw_figure(
                        window['plota'].TKCanvas,graph(F,df['x'].tolist())
                    )


                case 'Falsa Posição':
                    df    = method_falseposicao(F,a,b,eps,iter)
                    dados = df.loc[len(df.index)-1].tolist()
                
                    
                    window['fx1' ].update('Fx ='+str(dados[1]))
                    window['x'   ].update('x  ='+str(dados[5]))
                    window['x1'  ].update('x1 ='+str(dados[3]))
                    window['x2'  ].update('x2 ='+str(dados[4]))
                    window['itr' ].update('iter ='+str(dados[0]))
                    window['intx'].update('Intervalx ='+str(dados[4]))
                    
                    window['tab'].update(values=df.values.tolist())
                    
                    
                    fig = draw_figure(
                        window['plota'].TKCanvas,graph(F,df['x'].tolist())
                    )



                case 'Newton':         
                    df    = Newton(F,DF,a,eps)
                    dados = df.loc[len(df.index)-1].tolist()
                             
                    window['fx1'].update('Fx ='+str(dados[1]))
                    window['x'  ].update('x  ='+str(dados[5]))
                    window['x1' ].update('x1 ='+str(dados[1]))
                    window['x2' ].update('iter ='+str(dados[0]))
                    window['itr'].update('Intervalx ='+str(dados[4]))
                    
                    window['tab'].update(values=df.values.tolist())
                    
        
                    fig = draw_figure(
                        window['plota'].TKCanvas,graph(F,df['x'].tolist())
                    )
                    



                case 'Secante':
                    eps  = 1/10**values['eps']
                    df   = Secant(F,a,b,eps)
                    dados = df.loc[len(df.index)-1].tolist()
                    
                    
                    window['fx1'].update('Fx ='+str(dados[1]))
                    window['x'  ].update('x  ='+str(dados[5]))
                    window['x1' ].update('x1 ='+str(dados[2]))
                    window['x2' ].update('x2 ='+str(dados[3]))
                    window['itr'].update('Iter ='+str(dados[0]))
                    window['intx'].update('Intervalx ='+str(dados[4]))
                    
                    window['tab'].update(values=df.values.tolist())
                    
                    fig = draw_figure(
                        window['plota'].TKCanvas,graph(F,df['x'].tolist())
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
           
            
            a = b = eps = iter = df = None
    

            
if __name__ == "__main__":
    main()