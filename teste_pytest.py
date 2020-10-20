import requests


class TesteCursos:
  headers = {'Authorization': 'Token 775541e1a93f7d1f40f24fa4f29adece2f5e2ee7'}
  url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

  def test_get_cursos(self):
    cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

    assert cursos.status_code == 200
  
  def test_get_curso(self):
    curso = requests.get(url=f'{self.url_base_cursos}2/', headers=self.headers)

    assert curso.status_code == 200
  
  def test_post_curso(self):
    novo = {
      "titulo": "Curso de Programação com Ruby",
      "url": "http://www.geek.com.br/ruby"
    }

    resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)

    assert resposta.status_code == 201
    assert resposta.json()['titulo'] == novo['titulo']
  
  def test_put_curso(self):
    atualizado = {
      "titulo": "Novo curso de Ruby",
      "url": "http://www.geek.com.br/novo-ruby"
    }

    resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado)

    assert resposta.status_code == 200
    assert resposta.json()['titulo'] == atualizado['titulo']

  def test_delete_curso(self):
    resposta = requests.delete(url=f'{self.url_base_cursos}3/', headers=self.headers)

    assert resposta.status_code == 204 and len(resposta.text) == 0

## Executar os testes com 'pytest teste_pytest.py'


