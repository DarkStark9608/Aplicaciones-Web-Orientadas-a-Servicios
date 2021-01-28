import requests
import json

resultado = requests.get("https://www.googleapis.com/books/v1/volumes?q=harry+potter")

print (resultado.text)

