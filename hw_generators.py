# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем
import os


def check_unique_string_generator():
	with open(os.getcwd() + '/files/hw_9.txt', 'r') as f:
		lines = f.readlines()
	checked_line = []
	for line in lines:
		if line.rstrip() not in checked_line:
			checked_line.append(line.rstrip())
			yield line.rstrip()
		else:
			pass


check_line = check_unique_string_generator()
print(next(check_line))
print(next(check_line))
print(next(check_line))
print(next(check_line))
print(next(check_line))


# print(next(check_line))
# print(next(check_line))
# print(next(check_line))


# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
# # ```
# def coroutine(*args):
# 	# your code here
#
#
# @coroutine
# def grep(*args):
# 	# your code here
#
#
# @coroutine
# def printer():
# 	# your code here
#
#
# @coroutine
# def dispenser(*args):
# 	# your code here
#
#
# def follow(*args):
# 	# your code here
# ```
#
# Каждый grep следит за определенной сигнатурой
#
# Как это будет работать:
#
# ```
# f_open = open('log.txt') # подключаемся к файлу
# follow(f_open,
#        # делегируем ивенты
#        dispenser([
#            grep('python', printer()), # отслеживаем
#            grep('is', printer()),     # заданные
#            grep('great', printer()),  # сигнатуры
#        ])
#        )
# ```
# Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть
#
# Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.
#
# Если все плохо - план Б лекция Дэвида Бизли
# [warning] решение там тоже есть :)
# https://www.dabeaz.com/coroutines/Coroutines.pdf


# Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source ---send()--->coroutine1------send()---->coroutine2----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и обработку ошибки GeneratorExit.
#
# Например: Ваш source (это не корутина, не генератор и прочее, это просто функция ) в ней опеделите цикл из 10 элементов
# которые будут по цепочке отправлены в каждый из корутин и в каждом из корутив вызвано сообщение о полученном элементе.
# После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.


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
