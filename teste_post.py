import requests

headers = {'Authorization': 'Token 775541e1a93f7d1f40f24fa4f29adece2f5e2ee7'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


## Testes método POST
novo_curso = {
  "titulo": "Gerência Ágil de Projetos com Scrum",
  "url": "http://www.geek.com.br/scrum"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo do informado
assert resultado.json()['título'] == novo_curso['titulo']

