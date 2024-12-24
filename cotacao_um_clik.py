import requests

from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto_resposta['text']= f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''




janela = Tk()
janela.title('Cotaçao Atual daas Moedas')
janela.geometry('240x240')

texto_orintacoes = Label(janela, text='clique no butão para atualizar cotação')
texto_orintacoes.grid(column=0, row=0, padx=10, pady=10)

texto_orintacoes2 = Label(janela, text='clique aqui agora')
texto_orintacoes2.grid(column=0, row=1, padx=10, pady=10)
botao = Button(janela, text='Atualizar Cotação', command=pegar_cotacoes)
botao.grid(column=0, row=3, padx=10, pady=10)

texto_resposta = Label(janela, text='')
texto_resposta.grid(column=0, row=4, padx=10, pady=10)

janela.mainloop()


