import requests

headers = {'Authorization': 'Token 775541e1a93f7d1f40f24fa4f29adece2f5e2ee7'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


## Testes método DELETE

# # Verificando se curso existe com id = 3
# curso = request.get(url=f'{url_base_cursos}3/', headers=headers)

resultado = request.delete(url=f'{url_base_cursos}3/', headers=headers)

# Testando o código de status HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retornado é zero
assert len(resultado.text) == 0
