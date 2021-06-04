from metodos_abstratos import NomeNotasABS

class NomeNotas(NomeNotasABS):

	def __init__(self):
		pass
	
	def get_nome(self, lista: list) -> str:
		nome = lista[0]
		return nome


	def get_notas(self, lista: list) -> list:
		lista.pop(0)
		return lista
