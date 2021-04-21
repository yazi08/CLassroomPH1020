Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Ввод():
	def __call__(self, *args, **kwargs):
		return input(*args, **kwargs)

	
>>> ввод_имени = Ввод()
>>> ввод_возраста = Ввод()
>>> имя = ввод_имени("Введите ваше имя")
Введите ваше имяСергей Постников
>>> имя
'Сергей Постников'
>>> возраст = ввод_возраста("Сколько вам лет?")
Сколько вам лет?39
>>> возраст
'39'
>>> 