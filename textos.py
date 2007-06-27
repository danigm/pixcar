#todos las cadenas utilizadas en el juego
#para facilitar la traduccion
#una clase por idioma
#para cambiar el idioma cambiar la asignacion a la variable idioma.


class es:
	def __init__(self):
		self.time = 'tiempo:'
		self.lap = 'Vuelta:'
		self.ready = 'LISTO...'
		self.complete = 'CIRCUITO COMPLETADO!!!'
		self.play = 'Jugar'
		self.credits = 'Creditos'
		self.options = 'Opciones'
		self.quit = 'Salir'
		self.loading = 'Cargando...'

		self.credit_cab = ("Un juego de:", "Programadores:", "Disenadores Graficos", "Musicos:")
		self.options_h = 'Opciones de PiX Car'
		self.select_car = 'Seleccionar Coche'
		self.language = 'idioma'
		self.select_circuit = 'Selecciona Circuito:'
		self.select_circuit = 'Selecciona Circuito:'
		self.toggle_fs = "Cambiar fullscreen"
		self.hof = "Salon de la Fama"
		self.name = "Escribe tu nombre"

		self.controls = ("acelerar", "marcha atras", "izquierda", "derecha", "freno")
		self.opt_controls = "controles"
		
class en:
	def __init__(self):
		self.time = 'time'
		self.lap = 'lap:'
		self.ready = 'READY...'
		self.complete = 'CIRCUIT COMPLETED!!!'
		self.play = 'Play'
		self.credits = 'Credits'
		self.options = 'Options'
		self.quit = 'Quit'
		self.loading = 'Loading...'

		self.credit_cab = ("A Game produced by:", "Programmers:", "Grafic Designers", "Music:")
		self.options_h = 'PiX Car Options'
		self.select_car = 'Select Car'
		self.language = 'language'
		self.select_circuit = 'Select Circuit:'
		self.toggle_fs = "Toggle fullscreen"
		self.hof = "Hall of Fame"
		self.name = "Write your name"

		self.controls = ("accelerate", "reverse", "left", "right", "brake")
		self.opt_controls = "controls"

class Lang:
	def __init__(self):
		self.lang = es()
	
	def set_language(self, language):
		if language == 'es':
			self.lang = es()
		elif language == 'en':
			self.lang = en()


idioma = Lang()
