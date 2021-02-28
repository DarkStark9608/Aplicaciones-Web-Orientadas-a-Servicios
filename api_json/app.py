import web
import json
urls = (
    '/agenda?', 'Agenda',)    
app = web.application(urls, globals())
class Agenda():
  archivo_json = {}
  def GET(self):
    parametros = web.input() # Parametros por URL
    action=parametros.action 
   
    if action=="get":
      return self.getAction()
    if action=="put":
      try:
        nombre = parametros.nombre
        fecha = parametros.fecha    
        nacimiento=fecha[6:11]
        edad=2021-int(nacimiento)
        return self.putAction(nombre,edad)
      except:
        Error = {
        "Error": "Datos incorrectos"
      }
      with open("datos.json") as file:
          self.archivo_json = json.load(file) 
      self.archivo_json["errores"].append(Error)
      print(self.archivo_json)  
      with open("datos.json","w") as file:
        json.dump(self.archivo_json, file)
      print(self.archivo_json)  
      return self.getAction()


  def getAction(self):
    try:
      with open("datos.json") as file:
          self.archivo_json = json.load(file)
      print(self.archivo_json)
      return json.dumps(self.archivo_json)     
    except Exception as error:
      print("Error {}".format(error.args[0]))

  def putAction(self, nombre, edad):
    try:
      persona = {
        "nombre": nombre,
        "edad": edad
      }
      with open("datos.json") as file:
          self.archivo_json = json.load(file) 
      self.archivo_json["agenda"].append(persona)
      print(self.archivo_json)  
      with open("datos.json","w") as file:
        json.dump(self.archivo_json, file)
      print(self.archivo_json)  
      return self.getAction()
    except Exception as error:
      print("Error {}".format(error.args[0]))
  
    	
if __name__ == "__main__":
    app.run()


 