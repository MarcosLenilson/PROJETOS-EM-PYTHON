import PySimpleGUI as psg


layout = [
    [psg.Text('Usuário')],
    [psg.Input(key='usuario')],
    [psg.Text('Senha')],
    [psg.Input(key='senha')],
    [psg.Button('Login')],
    [psg.Text('', key='mensagem')]
]

window = psg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    elif event == 'Login':
        senha_correta = '1234'
        usuario_correto = 'Marcos'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso!')
        else:
            window['mensagem'].update('Senha ou Usuário incorreto!')
