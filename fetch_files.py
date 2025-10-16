import requests

username = "hisham-ux"
repo = "python-repo"
folder = "MY-SQL"
url = f"https://api.github.com/repos/{username}/{repo}/contents/{folder}"

response = requests.get(url)
files = [item['name'] for item in response.json() if item['type'] == 'file']

print(files)