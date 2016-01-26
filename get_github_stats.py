import github
import json
import requests

with open('./secrets.json') as data_file:
	SECRETS = json.load(data_file)

USERNAME = SECRETS['github_username']
PASSWORD = SECRETS['github_password']

repos = ['paydash','paydata','hrdf','mnrega-case']
users = ['angelaambroz','ravisuhag','edodge','sgriffis']
r = requests.get('https://api.github.com/repos/hks-epod/paydata/stats/contributors', auth=(USERNAME, PASSWORD))

contributors = json.loads(r.content)
for contributor in contributors:
	print contributor['author']['login']





