import requests 

cep = int(input('Digite um CEP: '))
url= f'http://viacep.com.br/ws/{cep}/json'
response= requests.get(url)
data= response.json()

if response.status_code == 200:
    estado=data['estado']
    localidade=data['localidade']
    uf=data['uf']
    regiao=data['regiao']
    print(f'O CEP {cep} corresponde ao estado: {estado}\nLocalidade: {localidade} \nUF: {uf}\nRegião: {regiao}')
    
else : 
    print ('Cidade não encontrada ou erro de API')
