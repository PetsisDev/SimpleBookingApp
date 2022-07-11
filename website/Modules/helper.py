import os

my_secret = os.environ['credentials.json']


def create_credentials_file():
	credentials_string = os.environ['credentials.json']
	with open('./website/Modules/Google/credentials.json', 'w') as f:
		f.write(credentials_string)
		f.close()
	