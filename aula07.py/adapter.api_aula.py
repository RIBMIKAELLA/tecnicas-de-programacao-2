import json

class SistemaCSV:
    def get_dados_csv(self):
        return "nome,idade\nJoão,30"

class InterfaceJSON:
    def get_dados(self):
        pass

class CSVparaJSONAdapter(InterfaceJSON):
    def __init__(self, sistema_csv):
        self.sistema_csv = sistema_csv

    def get_dados(self):
        
        csv_data = self.sistema_csv.get_dados_csv()
        
        
        linhas = csv_data.split('\n')
        cabecalho = linhas[0].split(',') # ['nome', 'idade']
        valores = linhas[1].split(',')   # ['João', '30']

        
        dados = {}
        for i in range(len(cabecalho)):
            dados[cabecalho[i]] = valores[i]

        
        return json.dumps(dados, indent=2, ensure_ascii=False)


sistema_legado = SistemaCSV()
adaptador = CSVparaJSONAdapter(sistema_legado)
print(adaptador.get_dados())