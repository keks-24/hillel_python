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