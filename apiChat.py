import requests

url = "https://api.api.ai/v1/query?v=20150910"
headers = { "Authorization" : "Bearer da39d236ca494f008cd2c5e2f3520688"}

userInput = "show me fabulous restaurants"


def userQuery(userInput):
	params = {
		"query" : userInput,
		"lang" : "en",
		"sessionId" : "652f9037-3045-4219-b841-d7be3aca8c0b",
		"timezone" : "Asia/Kuala_Lumpur"
	}

	return params


def googleAPI(userInput):

	r = requests.get(url,params=userQuery(userInput),headers=headers)

	inputParams = r.json().get("result").get('parameters')
	inputParams["name"] = inputParams['any']
	inputParams.pop('any')

	return inputParams


if __name__ == '__main__':
	print(googleAPI(userInput))
