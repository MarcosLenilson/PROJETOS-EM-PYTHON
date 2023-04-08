import PySimpleGUI as sg

# Criar as janelas e estilos(layout)


def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Digite seu nome:')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_endereco():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Digite seu endereço:')],
        [sg.Input()],
        [sg.Button('Retornar'), sg.Button('Continuar')],
    ]
    return sg.Window('Endereço', layout=layout, finalize=True)


def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Faça seu pedido:')],
        [sg.Checkbox('Pizza de Peperone', key='pizza1'), sg.Checkbox(
            'Pizza de Frango c/ Catupiry', key='pizza2')],
        [sg.Button('Retornar'), sg.Button('Fazer pedido')],
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)


# Criar as janelas iniciais

janela1, janela2, janela3 = janela_login(), None, None

# Criar um loop de leitura de eventos
while True:

    window, event, values = sg.read_all_windows()

    # Fechar janela

    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    # Ir para a próxima janela

    if window == janela1 and event == 'Continuar':
        janela2 = janela_endereco()
        janela1.hide()

    elif window == janela2 and event == 'Continuar':
        janela3 = janela_pedido()
        janela2.hide()

    # Voltar a janela anterior

    if window == janela3 and event == 'Retornar':
        janela3.hide()
        janela2.un_hide()
    elif window == janela2 and event == 'Retornar':
        janela2.hide()
        janela1.un_hide()

# Lógicas de o que deve acontecer ao clicar nos botões

    if window == janela3 and event == 'Fazer pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup(
                'Foram solicitados uma Pizza de Peperone e uma Pizza de Frango c/ Catupiry')
        elif values['pizza1'] == True:
            sg.popup('Foi solicitado uma Pizza de Peperone')
        elif values['pizza2'] == True:
            sg.popup('Foi solicitado uma Pizza de Frango c/ Catupiry')
