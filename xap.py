from datetime import datetime
import pandas

filename = './eventos/xap_1644783730.313227.csv'
# with open(filename) as file:
#     file
def teste():
    header = ['nome', 'data criacao', 'rg', 'cpf', 'valor transacao']
    colspecs = [(0,0), (0, 30), (31, 57), (58, 68), (69, 79), (80, 95)]
    df = pandas.read_fwf(filename, colspecs=colspecs, header=None, index_col=0)
    df.columns = header
    print(df)
    df.to_csv(f'toma_{str(datetime.now().timestamp())}.csv')

def teste_2():
    header = ['nome', 'data criacao', 'rg', 'cpf', 'valor transacao']
    widths = [30, 26, 10, 10, 15]
    df = pandas.read_fwf(filename, widths=widths, header=None)
    df.columns = header
    print(df)
    print(df['valor transacao'])
teste_2()