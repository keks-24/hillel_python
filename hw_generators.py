# Задача-1
import os
import time


def check_unique_string_generator():
	with open(os.getcwd() + '/files/hw_9.txt', 'r') as f:
		lines = f.readlines()
	checked_line = []
	for line in lines:
		if line.rstrip() not in checked_line:
			checked_line.append(line.rstrip())
			yield line.rstrip()


check_line = check_unique_string_generator()
print(next(check_line))
print(next(check_line))
print(next(check_line))
print(next(check_line))
print(next(check_line))
# print(next(check_line))
# print(next(check_line))
# print(next(check_line))


# Задача-2 пришлось подсмотреть
# Архитектура пайплайна
#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------
def coroutine(func):
	"""activate coroutine"""
	def start(*args,**kwargs):
		cr = func(*args, **kwargs)
		next(cr)
		return cr
	return start


@coroutine
def grep(*args):
	grep_word = args[0]  # искомое слово
	while True:
		line = (yield)  # полученная линия из dispenser
		if grep_word in line:
			args[1].send(line)  # шлем в принтер найденую линию если нашли слово в строке


@coroutine
def printer():
	while True:
		line = yield  # получаем линию которую завалидил grep
		print(line)


@coroutine
def dispenser(*args):
	while True:
		item = yield
		for coro in list(*args):  # в каждую корутину шлем строку полученную из follow
			coro.send(item)


def follow(file_open, dispenser_coro):
	while True:
		line = file_open.readline().rstrip()  # вычитываем строку из открытого файла
		if not line:
			time.sleep(0.1)  # символическая задержка
			continue
		dispenser_coro.send(line)  # отправляем строку в dispenser


f_open = open(os.getcwd() + '/files/log.txt', 'r')  # читаем файл
prnt = printer()
follow(f_open, dispenser([grep('python', prnt), grep('is', prnt), grep('great', prnt)]))
# Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть


# # Задача-3
def source(coro):
	next(coro)
	for i in range(0, 10):
		coro.send(i)
	coro.close()


def coroutine1(coro):
	try:
		next(coro)
		while True:
			value = yield
			print(f"c1 got {value}")
			coro.send(value)
	except GeneratorExit:
		print('c1 job done')
		coro.close()


def coroutine2(sink):
	try:
		next(sink)
		while True:
			value = yield
			print(f"c2 got {value}")
			sink.send(value)
	except GeneratorExit:
		print('c2 job done')


def sink():
	try:
		while True:
			number = yield
			print('Sink received number: ', number)
	except GeneratorExit:
		print('Sink closed.')


source(coroutine1(coroutine2(sink())))
