import web
import json

urls=('/','Horoscopo',)
app=web.application(urls,globals())

class Horoscopo():

    def GET(self,zodiaco):
        if zodiaco=="capricornio":
        datos={}
        datos["Nombre"]="Capricornio"
        datos["Fecha"]="22 DE DICIEMBRE AL 20 DE ENERO"
        datos["Descripcion"]="La política, la tierra, los lugares elevados, las montañas, las cimas, los lugares aislados e inaccesibles, las luchas, los obstáculos e impedimentos, la mala suerte, los reveses de fortuna, las carreras brillantes, la decadencia, el tiempo, la noche, los viejos, las deformidades, el invierno, el frío, las minas, el deber cívico y las ambiciones profesionales."
        datos["Elemento"]="Tierra"
        datos["Numero"]="1, 4, 8, 10, 13, 17, 19, 22, 26"
        datos["Color"]="Gris Oscuro, Marrón, Negro y Castaño"
        datos["Del_dia"]="Hoy será un buen día para la firma de contratos y para las asociaciones, también lo será para las actividades relacionadas con la filosofía y la educación. Sin embargo, tienes que precaverte de pensamientos utópicos, ya que esto podría hacer que tu concentración no sea óptima y que te disperses."
        datos["Del_dia"]="Hoy podrías sentir que es necesario hacer cambios de tipo ambiental, tanto en el trabajo como en casa. Alguna situación está por explotar y podría haber tendencia a rupturas. Podrías sentirte físicamente mal, será mejor que cuides de tu salud, sobre todo tus huesos y tu sistema respiratorio; si fumas, este será el momento de dejarlo."
        datos["Del_dia"]="Te sentirás feliz hoy. Será un día de reencuentros amorosos y de toma de decisiones no solamente en lo afectivo, sino también en lo profesional. Selecciona lo que creas que es mejor; te conviene seguir a tu intuición. En el terreno laboral, si tu profesión está relacionada con las finanzas, tendrás un buen día de trabajo. !Felicidades!"
        datos["Del_dia"]="Será un día para pasarlo con la familia, la pareja y los amigos. Capricornio, si puedes, sal de viaje, te sentará muy bien; olvidarás la rutina diaria y recobrarás fuerzas. En este sentido, el mejor lugar para ir será un entorno natural y plácido. También podrías salir a comer fuera con tu familia o con las personas a quienes quieres."
        datos["Del_dia"]="Hoy dedicarás el día al amor y a la amistad; la intimidad será lo que más te apetezca. Es necesario que expreses tus emociones y que comuniques lo que piensas a tu pareja, porque tal vez te esté notando algo distante y preocupado-a por los problemas cotidianos laborales. Para lograr equilibrio, hay que darle al César lo que es del César... y a tu pareja lo que le corresponde."
        result = json.dumps(datos)
        return result
                
        


if __name__ == "__main__":
    app.run()