#!/usr/bin/env

class Ввод():
	def __call__(self, *args, **kwargs):
		return input(*args, **kwargs)

def вывести(*args, **kwargs):
    return print( *args, **kwargs)

def main():
    ввод_имени = Ввод()
    ввод_возраста = Ввод()
    имя = ввод_имени("Ваше имя? ")
    лет = ввод_возраста("Сколько лет? ")
    вывести(f"Привет {имя}, вам {лет} лет!")

if __name__ == "__main__": main()
