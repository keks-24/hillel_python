# Вашей задачей будет создать сервер агрегатор (он выполнит несколько запросов на адреса сторонних сайтов).
# Количество сайтов и сами сайты на которые вы будете слать реквесты вы определяете сами
# (вот например по ссылке ниже найдете список популярных ресурсов, но, как правило, они требуют регистрации,
# после чего они предоставят вам что-то типа ключа с которым вы сможете запросить информацию)
#
# 1) Познакомиться с фреймворком AIOHTTP (https://docs.aiohttp.org/en/stable/).
# 2)Создать сервер который мог бы принимать GET запросы на адрес (http://localhost/collect_info)
# 3) В ответе должна быть агрегирована информация полученная от сторонних ресурсов.
#
# https://rapidapi.com/blog/most-popular-api/?utm_source=google&utm_medium=cpc&utm_campaign=Beta_100613405446&utm_term=%2Bapi_b&gclid=Cj0KCQjwudb3BRC9ARIsAEa-vUs9wupOfL1RSzBiu31y12XUuS02AH8zdZv6UyMocYy5khg9stSoXA4aAkDUEALw_wcB


from aiohttp import web
import json
import requests


def get_covid():
	url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

	querystring = {"country": "Ukraine"}

	headers = {
		'x-rapidapi-key': "52807abab7msha07c6984af16427p177ed8jsnb79c51c4bd57",
		'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
	}

	response = json.loads((requests.request("GET", url, headers=headers, params=querystring)).text)

	return response['data']


def get_joke():
	url = "https://icanhazdadjoke.com/"

	headers = {
		'Accept': "application/json"
	}

	response = json.loads((requests.request("GET", url, headers=headers)).text)
	return response['joke']


def get_fact_about_cats():
	url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1'

	response = json.loads((requests.request("GET", url)).text)
	return response['text']


async def handle(request):
	response_covid = get_covid()
	response_joke = get_joke()
	response_cat_fact = get_fact_about_cats()

	text = "Covid info: " + str(response_covid) + "\n" + "Super joke: " + str(response_joke) + '\n' + 'Fact about cat: ' + str(response_cat_fact)
	return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/collect_info', handle)])


if __name__ == '__main__':
	web.run_app(app)