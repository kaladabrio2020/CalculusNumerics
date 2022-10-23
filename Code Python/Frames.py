import PySimpleGUI as sg

def frams():
    sg.theme("DarkBlack1")
    coluna0 = [
        [sg.Frame(' Métodos ',[
        [
            sg.Checkbox('Bissecção',key='bissecao'),
            sg.Checkbox('Falsa Posição',key='falsa'),      
        ],
        [
            sg.Checkbox('Newton  ',key='newton'),
            sg.Checkbox('Secante',key='secante')  
        ],
        [
            sg.InputText("x**3-2*x**2-12*x+5",key='fx',size=(80,100),font='cabibri')
            ]
            ],size=(300,125) , title_location='n')],

        [sg.Frame(" Opções ",[
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
            sg.Text('Iter  ='),sg.Slider(range=(3,100),size=(21,20),key='maxit',orientation='h')
            ]],size=(300,250) , title_location='n')],
        
        [sg.Button(' Ok '),sg.Button('Sair ')]
    ]


    parte1 = [
            [sg.Text("",text_color='orange',key ='fx1',font='cabibri')],
            [sg.Text("",text_color='orange',key ='x'  ,font='cabibri')],
            [sg.Text("",text_color='orange',key ='x1' ,font='cabibri')],
            [sg.Text("",text_color='orange',key ='x2' ,font='calibri')],
            [sg.Text("",text_color='orange',key ='itr',font='cabibri')],
            [sg.Text("",text_color='orange',key ='intx',font='cabibri')] 
        ]


    parte2  = [ 
                [sg.Canvas(size=(360,360),key='plota')]
            ]
        
    
    tab_grupo = [
        [sg.TabGroup([
            [
                sg.Tab("Resultado" , parte1),
                sg.Tab("Plot",parte2)
             ]
        ],size=(390,375))]
    ]
    
    uniao  = [
        [
            sg.Column(coluna0, element_justification='c'),sg.Column(tab_grupo, element_justification='c')
        ]
    ]
    window =sg.Window("Métodos Numéricos",uniao,icon='method_numeric.ico',font=('calibri light',12),titlebar_font=('calibri',13))
    return window