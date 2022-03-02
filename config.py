import json

class Config:
	def __init__(self):
		with open("config.json", "r") as file:
			self.data = json.load(file)

	def get_config(self, config):
		if config in self.data:
			return self.data[config]
		return None

	def set_config(self, config, value):
		self.data[config] = value

		with open("config.json", "w") as file:
			json.dump(self.data, file, indent=4)