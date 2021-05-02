import requests
url = 'http://localhost:5000/result'
r = requests.post(url,json={'article':"PHOTOS: દેવ દિવાળી ઉજવવા બનારસ પહોંચ્યો અનિલ"})
print(r.json())
