import requests
import datetime 


getHoje = datetime.datetime.today()
ontem = getHoje - datetime.timedelta(days=3)
ontem = ontem.strftime("%d/%m/%Y")


url = (f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.1178/dados?formato=json&dataInicial={ontem}&dataFinal={ontem}")


r = requests.get(url)
data = r.json()
valor = float(data[0]['valor'])
print("O valor atual da taxa selic é: ", valor, "%")


inv_inicial = int(input("Digite o valor a ser investido: "))
inv_meses = int(input("Digite o aporte mensal: "))
inv_duracao = int(input("Digite a quantidade de meses que ira receber o aporte: "))
selic = int(input("Digite a % do CDI no investimento: ")) / 100
valor /= 100 * 12 * selic
inv_final = ((inv_inicial + (inv_meses * inv_duracao)) * valor * (inv_duracao - 1)) + (inv_inicial + inv_meses * inv_duracao)
print(inv_final)
