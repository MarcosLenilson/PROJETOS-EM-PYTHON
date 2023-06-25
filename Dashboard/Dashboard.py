# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel('Vendas.xlsx')

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")

app.layout = html.Div(
    
        children=[
        html.H1(children='Faturamento das Lojas'),
        html.H2(children='Gráfico com o Faturamento de Todos os Produtos Separados por Loja'),
        html.Div(children='''
            Obs: Esse gráfico mostra a quantidades de produtos vendidos, não o faturamento
        '''),
        

        dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),

        dcc.Graph(
            id='grafico_quantidade_vendas',
            figure=fig
        )
    ]
)

@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if (value == 'Todas as Lojas'):
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja']==value, :]  
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")  
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

