from nome_notas import NomeNotas
from media import Media


class Gerenciador(NomeNotas):
	
	'''
	Módulo responsável pelo gerenciamento das funções
	'''

	def __init__(self):
		super().__init__()

	def get_items(self, conteudo: list) -> dict:
		'''
		Modelo de inversão de depenência.
		__get_items é chamada por DadosValidos.get_all(conteudo) que
		por sua vez chama DadosValidos.set_items(nome, media)
		'''
		for item in conteudo:
			lista_dados = item.split(',')
			nome = self.get_nome(lista_dados)
			notas = self.get_notas(lista_dados)
			media = Media().media_notas(notas)
			resultado = self.set_items(nome, media)
		return resultado

	def set_items(self, nome: str, media: float) -> dict:
		self.result[nome] = media
		return self.result