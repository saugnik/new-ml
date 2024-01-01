import requests
def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()            
            print(data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
api_url = "https://cdn.jsdelivr.net/gh/stevenschobert/instafeed.js@2.0.0rc1/src/instafeed.min.js"
fetch_data(api_url)
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Content-Type': 'application/json',
}
response = requests.get(api_url, headers=headers)

