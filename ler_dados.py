class LerDados():

	def __init__(self) -> None:
		pass

	def __get_arquivo(self, nome_arquivo: str) -> str:
		try:
			if isinstance(nome_arquivo, str):
				arquivo = self.__abrir_arquivo(nome_arquivo)
				return arquivo
		except BaseException as err:
			print(f'__get_arquivo >>> {err}')

	def __abrir_arquivo(self, nome_arquivo: str) -> str:
		try:
			texto = open(nome_arquivo, 'r')			
			return texto
		except BaseException as err:
			raise err

	def __ler_texto(self, text: str) -> str:
		try:
			text = text.read()
			return text
		except:
			print('Não conseguiu ler o arquivo')

	def arquivoInterface(self, nome_arquivo) -> str:
		'''
		Método que retorna os dados dentro do arquivo em formato str
		'''
		try:
			texto = self.__get_arquivo(nome_arquivo)
			texto = self.__ler_texto(texto)
			return texto
		except BaseException as err:
			print(f'arquivo interface >>> {err}')