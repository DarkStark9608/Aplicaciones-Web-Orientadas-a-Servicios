import web
import requests
import json

render= web.template.render("mvc/")

class Index():
  def GET(self):
    datos=None
    return render.index(datos)

  def POST(self)  :
    form=web.input()
    nombre_libro=form.nombre_libro
    
    resultado = requests.get("https://www.googleapis.com/books/v1/volumes?q="+nombre_libro)

    book = resultado.json()

    items = book["items"]

    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    url = decoded[0]["volumeInfo"]["infoLink"]
    url_imagen=decoded[0]["volumeInfo"]["imageLinks"]["smallThumbnail"]
    nombre_autor=str(decoded[0]["volumeInfo"]["authors"])
    link ="<a target='blank' href='"+url+"'>"+nombre_libro+"</a>"
    
    imagen ="<img src='"+url_imagen+"'/>"
    autor="<label>'"+nombre_autor+"'</label>"

    datos={
      
      "nombre_libro":"Nombre del libro: "+nombre_libro,
      "imagen":imagen,
      "autor":"Autor: "+autor,
      "url":"Link de compra: "+link

    }
    return render.index(datos)
