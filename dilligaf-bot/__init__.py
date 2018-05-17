import requests

if __name__ == '__main__':
	with open('.api-key') as key_file:
		key = key_file.read().strip()
	tok_req = requests.post('https://www.reddit.com/api/v1/access_token',
	                        auth = ('HXy8EFRi6Kv8JQ', key),
	                        data = {'grant_type': 'password',
	                                'redirect_uri': 'http://localhost:8080'})
	print(r.content)
