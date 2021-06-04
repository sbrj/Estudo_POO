from ler_dados import LerDados
from externar import Externar

# -- Início Programa --

if __name__ == '__main__':
	
	'''
	Para iniciar o programa, instancie um objeto com 'LerDados()'
	Atribua a uma variável com o método 'Externar(objeto, nome_arquivo)'
	'''

	# Instanciar uma variável com o conteúdo como objeto da classe LerDados()
	lerDados = LerDados()

	# modelo de injeção de dependência
	# Utilizar um objeto(lerDados) como atributo da classe Externar
	dados_validos = Externar(lerDados, 'notas.txt')
	#dados = dados_validos.resultado()
	dados = dados_validos.imprimir()
