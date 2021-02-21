import web
import json
datos={}
urls = (
    '/calculos?', 'Calculos',)    
app = web.application(urls, globals())

class Calculos:
  
  def datos(self,parametros):
    try:
      nombre = parametros.nombre
      fecha = parametros.fecha
      
      nacimiento=fecha[6:11]
      edad=2021-int(nacimiento)
      datos["Nombre"]=nombre
      datos["Fecha nacimiento"]=fecha
      datos["Edad"]=edad
      file=open("archivos.txt","a")
      variable="Nombre: "+nombre +" Fecha de nacimiento: "+fecha+" Edad: "+str(edad)+"\n"
      file.write(variable)
      
      file.close()
      return json.dumps(datos)
    except:
      datos["Error"]="Datos invalidos"
      datos["Solucion"]="Ingresa tu nombre y tu fecha de nacimiento DD/MM/AAAA"
      file=open("archivos.txt","a")
      variable="Datos Invalidos\n"
      file.write(variable)
      encoded = json.dumps(datos)
      decoded = json.loads(encoded)
      return json.dumps(datos)


  
  def GET(self): 
    parametros = web.input() # Parametros por URL
    
    return self.datos(parametros) 		
if __name__ == "__main__":
    app.run()
