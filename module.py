

class CustomSignal():

	def __init__(self):
		self.num : int
		self.trigger_function = None


	def emit(self, text):
		if self.trigger_function == None:
			return

		self.trigger_function(text)


	def connect(self, func):
		self.trigger_function = func
