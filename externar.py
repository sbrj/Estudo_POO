from typing import Type
from ler_dados import LerDados
from dados_validos import DadosValidos

class Externar:

	'''
	:conteudo 		- Objeto da classe Conteudo
	:nome_arquivo 	- Nome do arquivo a ser analisado
	'''

	def __init__(self, conteudo: Type[LerDados], nome_arquivo: str) -> None:
		self.conteudo = conteudo.arquivoInterface(nome_arquivo)

	def resultado(self) -> dict:
		'''
		Métoodo responsável por chamar os métodos responsáveis pelo tratamento do conteúdo
		'''
		try:
			conteudo_arquivo = DadosValidos()
			dados = conteudo_arquivo.get_all(self.conteudo)
			return dados
		except:
			print('Não encontrou nenhum resultado')

	def imprimir(self) -> print:
		try:
			imprime = self.resultado()
			return print(imprime)
		except:
			print('Não conseguiu imprimir')