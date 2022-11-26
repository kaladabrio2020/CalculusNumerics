import PySimpleGUI as sg

colunas_name = [
    'it',
    '     fx     ',
    '   a   ',
    '   b   ',
    'intervalo x']

def methods_numerics():
    sg.theme("DarkBlack1")
    coluna0 = [
        [
            sg.Frame(' Métodos ',[
        [
            sg.Combo(['Bissecção','Falsa Posição','Newton','Secante'],default_value='Newton',key='type')
        ],
        [
            sg.Text('Função')
        ],
        [
            sg.InputText("x**3-2*x**2-12*x+5",key='fx',size=(80,100),font='cabibri')
            ]
            ],size=(300,125) , title_location='n',element_justification='n')],

        [
            sg.Frame(" Opções ",[
        [
            sg.Text(' Intervalo.:[a , b]')
        ],
        [
            sg.Text(' Epslon.....:[3,10]   Iter.:[3,100]')
        ],
        [
            sg.Text('x1 ='),sg.InputText("-2",size=(10,30),key='a')
        ],
        [
            sg.Text('x2 ='),sg.InputText("4",size=(10,30),key='b')
        ],
        [
            sg.Text('Eps ='),sg.Slider(range=(3,10),key='eps',size=(21,20),orientation='h')
        ],
        [
            sg.Text('Iter ='),sg.Slider(range=(3,100),size=(21,20),key='maxit',orientation='h')
        ]],size=(300,280) , title_location='n')
        ],
        [sg.Button(' Ok '),sg.Button('Cancel')]
    ]


    parte1 = [
            [sg.Text("",text_color='orange',key ='fx1',font=('calibri',14))],
            [sg.Text("",text_color='orange',key ='x'  ,font=('calibri',14))],
            [sg.Text("",text_color='orange',key ='x1' ,font=('calibri',14))],
            [sg.Text("",text_color='orange',key ='x2' ,font=('calibri',14))],
            [sg.Text("",text_color='orange',key ='itr',font=('calibri',14))],
            [sg.Text("",text_color='orange',key ='intx',font=('calibri',14))],
        ]
    

    parte2 = [ 
               [
                   sg.Canvas(size=(385,385),key='plota')
                ]
            ]
    
    parte3 = [
        [
            sg.Table(
                    headings=colunas_name,
                    values  =['','','','',''],
                    font    =('calibri',12),
                    key     ='tab',
                    auto_size_columns=True,
                
                    vertical_scroll_only = False,
                    expand_x=True,
                    expand_y=True,
                    enable_click_events=True,
                    size    =(500,500)                        
                    )
        ]
    ]
    
    tab_grupo = [
        [sg.TabGroup([
            [
                sg.Tab("Resultado" , parte1),
                sg.Tab('Tabela',parte3,element_justification='c'),
                sg.Tab("Plot",parte2)
             ]
        ],size=(390,400),expand_x=True)]
    ]
    
    uniao  = [
        [
            sg.Column(coluna0, element_justification='c'),sg.Column(tab_grupo, element_justification='c')
        ]
    ]
    window =sg.Window("Métodos Numéricos",uniao,icon=r'C:\Users\mateu\OneDrive\Git-Hub\Methods\Code Python\method_numeric.ico',font=('calibri light',12),titlebar_font=('calibri',13))
    return window


