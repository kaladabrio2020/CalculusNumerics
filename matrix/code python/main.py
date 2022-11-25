import numpy       as np
import PySimpleGUI as sg 
import interface.operation   as op

from   codigo_fonte import Gauss
from   codigo_fonte import Fatoracoes
from   interface    import interface_main


def main():
    janela = interface_main.main()

    while True:
        event , values = janela.read()

        if (event == 'Sair' or event == sg.WIN_CLOSED):break

        if (event == 'Ok')  :
            if (values['result']!=''): janela['result'].update('')

            string = values['matrix'] 
            A , b  = op.transform_matrix(string)
           
            try:
                if (A=='None'  or b=='None'):
                    janela.close()
                    main()
            except Exception as e:
                pass             
            
            match (values['tipo']):
                
                case 'Gauss':
                    ab , xb = Gauss.gauss(A, b,5,True)
                    ab = op.tostring(ab)
                    a,xb = op.tostring_x(xb)
                        
                    string = f'OBS:{a}\n Ab =\n{ab}\n x =\n{xb}'
                    janela['result'].update(string)


                case 'Fatoração LU':
                    U , L , x = Fatoracoes.fatoracao_LU(A,b)
                    U = op.tostring(U)
                    L = op.tostring(L)
                    a,x = op.tostring_x(x)

                    string = f'OBS:{a} \n>U = \n{U}\n >L = \n{L} \n >x =\n{x}\n'
                    janela['result'].update(string)


                case 'Fatoração LDP':
                    L,D,P,x = Fatoracoes.fatoracao_LDP(A, b)
                    L = op.tostring(L)
                    D = op.tostring(D)
                    P = op.tostring(P)
                    a,x = op.tostring_x(x)
                    string = f'OBS:{a}\n>L = \n{L}\n >D = \n{D}\n >P =\n{P}\n >x =\n{x}\n'
                    janela['result'].update(string)
            
if __name__ == "__main__":
    main()