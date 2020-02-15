import requests

proxies = {
    'http': 'http://10.121.2.100:8080',
    'https': 'https://10.121.2.100:8080',
}

# Create the session and set the proxies.
s = requests.Session()
s.proxies = proxies

# Make the HTTP request through the session.
r = s.get('http://www.showmemyip.com/')


# Check if the proxy was indeed used (the text should contain the proxy IP).
print(r.text)