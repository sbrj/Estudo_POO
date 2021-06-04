from gerenciador import Gerenciador
from typing import Type

class DadosValidos(Gerenciador):

	'''
	Classe pai de 'Externar' e filha de 'Gerenciador'.
	Reecebe os dados, e envia para cada sessão fazer sua parte
	'''
	def __init__(self) -> None:
		super().__init__()
		self.result = {}

	def get_all(self, cont) -> dict:
		'''
		Método responsável por chamar os métodos que farão o tratamento do conteúdo
		Retorna uma lista com o conteúdo
		'''
		try:
			lista_conteudo = self.__tratar_conteudo(cont)
		except BaseException as err:
			raise err
		else:
			conteudo_arquivo = self.get_items(lista_conteudo)
			return conteudo_arquivo

	def __tratar_conteudo(self, conteudo: str) -> list:
		'''
		Função responsável por tirar a linha e converter o conteudo em uma lista
		'''
		lista_conteudo = conteudo.split('\n')
		return lista_conteudo

