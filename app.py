import PySimpleGUI as ps


#layout
ps.theme('Reddit')
layout = [
    [ps.Text('Usuario'), ps.Input(key='Usuario', size=(20,1)) ],
    [ps.Text('Senha'), ps.Input(key='Senha', password_char='*', size=(20,1))],
    [ps.Checkbox('Salvar Login?')],
    [ps.Button('Entrar')]
]

#Aba
Aba= ps.Window('Tela de login', layout)

while True:
    evento, valores = Aba.read()
    if evento == ps.WINDOW_CLOSED:
        break
    if evento == 'Entrar':
        usuario = valores['Usuario']
        senha = valores['Senha']
        salvar_login = valores[0]
        
        
        Aba.close()

