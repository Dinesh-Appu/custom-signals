

class CustomSignal():

	def __init__(self):
		self.num : int
		self.trigger_function = None


	def emit(self, text, *args, **kwargs):
		if self.trigger_function == None:
			return

		self.trigger_function(text , *args)


	def connect(self, func):
		self.trigger_function = func
