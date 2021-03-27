from aiohttp import web, ClientSession


async def get_covid():
	session = ClientSession()
	url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

	querystring = {"country": "Ukraine"}

	headers = {
		'x-rapidapi-key': "52807abab7msha07c6984af16427p177ed8jsnb79c51c4bd57",
		'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
	}

	async with session.get(url, headers=headers, params=querystring) as resp:
		result = await resp.json()
	await session.close()
	return result['data']


async def get_joke():
	session = ClientSession()
	url = "https://icanhazdadjoke.com/"

	headers = {
		'Accept': "application/json"
	}

	async with session.get(url, headers=headers) as resp:
		result = await resp.json()
	await session.close()
	return result['joke']


async def get_fact_about_cats():
	session = ClientSession()
	async with session.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1') as resp:
		result = await resp.json()
	await session.close()
	return result['text']


async def handle(request):
	response_covid = await get_covid()
	response_joke = await get_joke()
	response_cat_fact = await get_fact_about_cats()

	text = "Covid info: " + str(response_covid) + "\n" + "Super joke: " + str(response_joke) + '\n' + 'Fact about cat: ' + str(response_cat_fact)
	return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/collect_info', handle)])


if __name__ == '__main__':
	web.run_app(app)