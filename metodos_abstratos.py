from abc import ABC, abstractmethod

class MediaABS(ABC):
	'''
	Classe abstrata.
	Não possui nenhuma dependência com outra classe
	'''

	def __init__(self):
		pass

	@abstractmethod
	def media_notas(self, notas: list) -> float:
			pass

class NomeNotasABS:
	'''
	Classe NÂO abstrata.
	Clase pai de NomeNotas, avô de Gerenciador, bisavô de Dados_validos, trisavô de Externar
	'''
	def __init__(self):
		pass

	@abstractmethod
	def get_nome(self, lista: list) -> str:
		pass

	@abstractmethod
	def get_notas(self, lista: list) -> list:
		pass