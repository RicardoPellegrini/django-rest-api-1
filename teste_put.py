import requests

headers = {'Authorization': 'Token 775541e1a93f7d1f40f24fa4f29adece2f5e2ee7'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


## Testes método PUT
curso_atualizado = {
  "titulo": "Novo curso de Scrum 3",
  "url": "http://www.geek.com.br/scrum3"
}

# # Verificando se curso existe com id = 3
# curso = request.get(url=f'{url_base_cursos}3/', headers=headers)

resultado = request.put(url=f'{url_base_cursos}3/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP
assert resultado.status_code == 200

# Testando o título
assert resultado.json()['titulo'] == curso_atualizado['titulo']

