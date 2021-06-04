from metodos_abstratos import MediaABS

class Media(MediaABS):
	'''Utilização de método abstrato'''

	def __init__(self):
		super().__init__()
		pass

	def media_notas(self, notas: list) -> float:
			total = 0
			for nota in notas:
				total += int(nota)
			media = total/4
			return media
