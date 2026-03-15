import requests
from bs4 import BeautifulSoup

url = "https://app.allrobotics.co/login"
s = requests.Session()
r = s.get(url)
soup = BeautifulSoup(r.text, "html.parser")
csrf = soup.find("input", {"name":"csrf_token"})
print("CSRF token:", csrf["value"] if csrf else "ไม่พบ")
