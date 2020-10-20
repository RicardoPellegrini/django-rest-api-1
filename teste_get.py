import requests

# GET Avaliações

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o status code
# print(avaliacoes.status_code)

# Acessando os dados da requisição
# print(avaliacoes.json())

headers = {'Authorization': 'Token 775541e1a93f7d1f40f24fa4f29adece2f5e2ee7'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
print(resultado.json())

## Testes método GET
# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 2

# Testando o nome do primeiro elemento
assert resultado.json()['results'][0]['titulo'] == 'Criação de APIs REST com Django REST Framework'


## Testes método POST
novo_curso = {
  "titulo": "Gerência Ágil de Projetos com Scrum",
  "url": "http://www.geek.com.br/scrum"
}

