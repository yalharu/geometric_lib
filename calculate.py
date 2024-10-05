import circle
import square
'''
	Программа вычисляет значения функции для указанной фигуры на основе ее размеров.
'''

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	'''
	Функция проверяет, что переданная фигура и функция являются допустимыми.

	figs - название фигуры (круг или квадрат)
	funcs - название функции (периметр или площадь)
	size - список размеров фигуры 
	'''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

	'''
	Eval динамически вызывает функцию из модуля с переданными аргументами size 
	Print выводит результат вычисления
	'''

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	'''
	Выполнение происходит когда скрипт запускается напрямую, переменные иницилизируется.
	'''
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	'''
	Первый цикл запрашивает у пользователя название фигуры (square/circle)
	'''
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	'''
	Второй цикл делает то же, что и первый для функции
	'''
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	'''
	Третий цикл запрашивает размеры фигуры. Get используется для получения количества аргументов из 
	sizes, но поскольку словарь пустой, всегда будет возвращаться 1.
	'''
	calc(fig, func, size)

	'''
	После успешного ввода всех данных вызывается функция calc для вычисления результата.
	'''


