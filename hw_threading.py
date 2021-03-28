from aiohttp import web, ClientSession


apis_dict = {
	'api_1': {
		'url': 'https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total',
		'params': {"country": "Ukraine"},
		'headers': {'x-rapidapi-key': "52807abab7msha07c6984af16427p177ed8jsnb79c51c4bd57",
					'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"},
		'result': 'data',  # that field will take yours data from each request, and add it to result key
		'description': 'covid'  # that field will be a key in a result
	},
	'api_2': {
		'url': 'https://icanhazdadjoke.com/',
		'headers': {
			'Accept': "application/json"},
		'result': 'joke',
		'description': 'super_joke'
	},
	'api_3': {
		'url': 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1',
		'result': 'text',
		'description': 'cats_facts'
	}
}


async def requester_urls():
	result_list = {}

	for api in apis_dict.keys():
		session = ClientSession()
		async with session.get(url=apis_dict[api]['url'],
									headers=apis_dict[api]['headers'] if apis_dict.get(api).get('headers') else None,
									params=apis_dict[api]['params'] if apis_dict.get(api).get('params') else None) as resp:
			result = await resp.json()
			await session.close()
			result_list[apis_dict[api]['description']] = result[apis_dict[api]['result']]
		await ClientSession.close(self=ClientSession())
	return result_list


async def handle(request):
	response = await requester_urls()
	print(response)

	return web.Response(text=f" covid info: {response['covid']}\n super joke: {response['super_joke']}\n cats facts: {response['cats_facts']}\n")


app = web.Application()
app.add_routes([web.get('/collect_info', handle)])


if __name__ == '__main__':
	web.run_app(app)