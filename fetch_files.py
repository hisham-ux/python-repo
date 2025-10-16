import requests

username = "hisham-ux"
repo = "python-repo"
folder = "my-sql"

url = f"https://api.github.com/repos/{username}/{repo}/contents/{folder}"

response = requests.get(url)

# Show status and raw text for debugging
print("Status code:", response.status_code)

# If successful (status code 200)
if response.status_code == 200:
    data = response.json()

    # GitHub API returns a list of dicts for a folder
    if isinstance(data, list):
        files = [item['name'] for item in data if item['type'] == 'file']
        print("Files found:", files)
    else:
        print("Unexpected response format:", data)

# If not successful, show the error message
else:
    print("Error response from GitHub:")
    print(response.text)
