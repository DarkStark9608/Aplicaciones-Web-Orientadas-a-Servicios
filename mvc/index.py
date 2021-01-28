import web
import requests
import json

render= web.template.render("mvc/")

class Index():
  def GET(self):
    return render.index()

  def POST(self)  :
    form=web.input()
    nombre_libro=form.nombre_libro

    resultado = requests.get("https://www.googleapis.com/books/v1/volumes?q="+nombre_libro)

    book = resultado.json()

    items = book["items"]

    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    url = decoded[0]["volumeInfo"]["infoLink"]

    link ="<a target='blank' href='"+url+"'>"+nombre_libro+"</a>"

    return link