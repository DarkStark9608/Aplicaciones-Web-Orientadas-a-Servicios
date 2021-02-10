import web
import json
datos={}
urls=('/(.*)','Horoscopo',)
app=web.application(urls,globals())

class Horoscopo():

    def GET(self,zodiaco):
        try:
          dia=int(zodiaco[0:2])
          mes=int(zodiaco[3:5])
          print (dia,mes)
          


          if dia>=22 and mes==12 or mes==1 and dia<=19:
            datos={}
            datos["Nombre"]="Capricornio"
            datos["Fecha"]="Diciembre 22 – Enero 19"
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
          
          elif dia>=19 and mes==2 or dia<=20 and mes==3:
            datos={}
            datos["Nombre"]="Piscis"
            datos["Fecha"]="Febrero 19 – Marzo 20"
            datos["Descripcion"]="Piscis es un signo mutable y de agua, también es el último signo del zodiaco, precisamente por eso, es el más rico y complejo de todos. Sensible ante el sufrimiento de los demás, responde con buena voluntad y ganas de ayudar. No le gusta sentirse preso y ni respeta las convenciones, así, por las buenas, aunque tampoco tiende a luchar contra lo establecido, sencillamente, discurre por otro lado."
            datos["Elemento"]=" Agua"
            datos["Numero"]="3, 7, 12, 16, 21, 25, 30, 34, 43, 52"
            datos["Color"]="Mauve, Lila, Púrpura, Violeta, Verde mar"
            datos["Del_dia"]="Hoy será un día de reencuentros con las personas a quienes amas o a quienes amaste. Puede que tengas que tomar decisiones en este sentido; una persona influyente podría acercarse a ti: utiliza tu intuición y decide lo que creas conveniente. Piscis, si ya tienes pareja, podrías encontrarte en una disyuntiva nada agradable."
            datos["Del_dia"]="Tu trabajo y tu servicio serán valorados en este día, recibirás recompensas tanto en el terreno emocional como en el económico. Hoy podría ser un día de éxito y de múltiples realizaciones, siempre y cuando no te aísles. Recuerda que la amistad es algo muy importante que todos necesitamos, y tú más que nadie."
            datos["Del_dia"]="Te refugias en el pasado con demasiada frecuencia cuando sientes que el ambiente no es propicio. Hoy tratarás de aislarte, pero sería muchísimo mejor que salieses al mundo y vieras lo hermoso que es. Tienes muchas cosas que realizar; los últimos días han sido difíciles: ubícate y trata de empezar un nuevo proyecto, comprobarás el resultado."
            datos["Del_dia"]="Hoy te sentirás renovado-a y feliz; lo que más te convendrá será salir de la ciudad en companía de tu familia, pareja o amistades. Elige un lugar totalmente nuevo, pero en el que te sientas en armonía con la naturaleza. Si no puedes salir fuera, elige un buen restaurante y goza de una suculenta comida con un vinito... !pero solamente uno!"
            datos["Del_dia"]="El amor te sonreirá hoy, tal vez se trate de un reencuentro amoroso. Puede incluso que tengas que elegir entre dos opciones sentimentales: selecciona siguiendo a tu intuición, pero trata de no idealizar demasiado a esa persona o luego te desilusionarás drásticamente. Piscis, hoy todo lo relacionado con la belleza te aportará equilibrio."
            result = json.dumps(datos)
            return result
            
          elif dia>=20 and mes==1 or dia<=18 and mes==2:
            datos={}
            datos["Nombre"]="Acuario"
            datos["Fecha"]="Enero 20 – Febrero 18"
            datos["Descripcion"]="Acuario es un signo fijo y de aire, y sin duda, es el signo con mayor capacidad para la invención de toda la rueda zodiacal. Simpático, original y brillante, Acuario también es un signo muy humanitario, al mismo tiempo que independiente e intelectual. Sus puntos negativos se encuentran en su inestabilidad e imprecisión y en su tendencia a llevar la contraria casi por sistema."
            datos["Elemento"]=" Aire"
            datos["Numero"]="4, 8, 13, 17, 22, 26"
            datos["Color"]="Azul, Verde-Azul, Gris, Negro"
            datos["Del_dia"]="Esta será una semana de cambios de los que tú mismo-a te sorprenderás, sobre todo en las relaciones emocionales y de pareja. Estarás ante un momento clave para tu destino futuro. Ahora podrías tener una magnífica racha en la que recibirás gratificaciones, mejoras y te irá bien en el terreno económico; incluso tendrás suerte."
            datos["Del_dia"]="Hoy será un día de buenas noticias en todos los sentidos. Sin embargo, Acuario, deberías prestar atención y despachar lo que tengas pendiente. Los aspectos serán beneficiosos y habrá energía para el inicio de proyectos, sobre todo en el terreno económico, pues contarás con algunos cambios positivos."
            datos["Del_dia"]="Sucesos inesperados y fenómenos sorprendentes podrían darse hoy: no te precipites, trata de ser optimista, fija muy bien la atención en lo que estés haciendo y revisa los documentos que envíes. Utiliza tu intuición y tu creatividad, hoy podrías descubrir algo interesante. También podrías empezar nuevos proyectos."
            datos["Del_dia"]="Hoy será un buen día para hacer un viaje de fin de semana. Sal con tu familia o amistades, elige un lugar en el que nunca hayas estado, preferentemente un lugar cercano al agua, el agua te tranquilizará y te dará paz. Si no puedes salir, una buena opción será asistir a cualquier reunión familiar, o, simplemente disfrutar de tu pareja."
            datos["Del_dia"]="Hoy podrías sentirte contrariado-a, quizá se trate de malentendidos, sobre todo emocionales, con tu pareja. Te estás comunicando mal y esto es lo que causa los problemas; es como si cada cual estuviera en un canal diferente, por eso, todo lo que os decís acaba malinterpretado. Tenéis que evitar esta situación como sea."
            result = json.dumps(datos)
            return result


          elif dia>=21 and mes==3 or dia<=19 and mes==4:
            datos={}
            datos["Nombre"]="Aries"
            datos["Fecha"]="Marzo 21 –Abril 19"
            datos["Descripcion"]="Aries forma parte de los signos cardinales y al mismo tiempo es un signo de fuego; también es el primer signo del zodíaco, precisamente por eso, simboliza el inicio, la creación. Se caracteriza por ser una persona rebosante de energía y entusiasmo; avanzada y aventurera, adora la libertad, los retos y las nuevas ideas."
            datos["Elemento"]=" Fuego"
            datos["Numero"]="1, 9"
            datos["Color"]="Rojo"
            datos["Del_dia"]="Hoy será un día de posibles logros, Aries, tanto en el terreno profesional como en el sentimental. Una persona con experiencia podría ofrecerte su apoyo; además, las relaciones con las personas que representen cierta autoridad sobre ti, como los maestros, estarán también de tu parte. !Felicidades!"
            datos["Del_dia"]="Tendrás un día muy fecundo. Los proyectos que hoy se inicien tendrán unas magníficas perspectivas de futuro; además, podrías hacer nuevos descubrimientos. Te sentirás fuerte y vital, energético-a, y también muy sensual. Podrías desarrollar proyectos interesantes que posiblemente deriven de tus relaciones con personas de fuera de tu entorno.."
            datos["Del_dia"]="Este día deberías dedicárselo al amor y a la amistad: sé generoso-a y verás brillar el sol en tu vida. Será un día de realizaciones agradables en el amor si expresas tus emociones. Después de tus labores cotidianas, invita a tu pareja a algún lugar romántico y agradable. Ten cuidado en tus relaciones con las personas ancianas y con la autoridad."
            datos["Del_dia"]="Pasarás un día en el que tenderás a la riqueza en general, tanto en lo material como en lo sentimental. Sin embargo, es posible que tengas que tomar decisiones; podrían producirse reencuentros amorosos. Aries, es un sábado para buscar el equilibrio a través de la pareja; te notarás muy sensual."
            datos["Del_dia"]="Una persona desconocida para ti hasta ahora, pero influyente se acercará a ti: no tomes decisiones bruscas, te podrían conducir al desastre. Piensa en lo que ahora deseas cambiar en tu vida, la energía para hacer ese tipo de transformación será la apropiada. Tu energía sexual subirá y te sentirás con poder."
            result = json.dumps(datos)
            return result
          
          elif dia>=20 and mes==4 or dia<=20 and mes==5:
            datos={}
            datos["Nombre"]="Tauro"
            datos["Fecha"]="Abril 20 – Mayo 20"
            datos["Descripcion"]="Tauro pertenece a los signos fijos y simultáneamente es un signo de tierra. La proyección del Sol en su nacimiento suele influir para que sean personas firmes, decididas y constantes en varios sentidos. También adoran sentir seguridad, por eso la buscan tanto, es como una necesidad constante en sus vidas."
            datos["Elemento"]=" Tierra"
            datos["Numero"]="2, 4, 6, 11, 20, 29, 37, 47, 56"
            datos["Color"]="Azul, Rosa, Verde"
            datos["Del_dia"]="Te espera un día importante en el terreno laboral; una persona en quien confías te ayudará. También podrías resolver asuntos en los viajes que hagas, porque serán favorables. Las reuniones que mantengas tenderán a culminar en contratos que deberías firmar siempre y cuando sean justos. Tauro, la manera de comunicarte será lo principal."
            datos["Del_dia"]="Contarás con muy buenas perspectivas en el terreno económico hoy, sobre todo si te mueves en áreas científicas o estás elaborando nuevos artículos. Recibirás unas excelentes noticias. Tauro, te encuentras en un periodo de cambios que serán beneficiosos siempre y cuando estén bien fundamentados."
            datos["Del_dia"]="Tauro, hoy es posible que recibas noticias sobre algo primordial, esto simbolizará el inicio de un periodo en el que si trabajas duro, obtendrás unos magníficos resultados. Sigue a tu instinto más profundo y desarrolla tu creatividad, pero poniendo también los pies en la tierra. Tus círculos sociales te ayudarán en lo que necesites."
            datos["Del_dia"]="Alguien te ayudará este sábado. Tauro, será un día de contactos fructíferos y de energía positiva, de desplazamientos positivos: aprovecha para salir el fin de semana, pues tienes muchas opciones. Podrías salir con un grupo de amigos o con tu pareja, para quienes tengan familia, las alternativas se dirigirán hacia el disfrute de los pequenos de la casa."
            datos["Del_dia"]="Sientes que estás en pleno dominio del poder, además, tu voluntad y tenacidad son las mejores herramientas y te permiten desarrollar tu capacidad de organización. Tauro, disfrutarás de un día sensual, tengas o no pareja; en este sentido, si no la tienes y quieres tenerla sal a buscarla; alguien nuevo y excitante se acerca."
            result = json.dumps(datos)
            return result


          elif dia>=21 and mes==5 or dia<=20 and mes==6:
            datos={}
            datos["Nombre"]="Géminis"
            datos["Fecha"]="Mayo 21 – Junio 20"
            datos["Descripcion"]="Géminis es un signo mutable que forma parte del elemento aire; como signo de los gemelos, su carácter es doble y bastante contradictorio por complejo. Por una parte es capaz de adaptarse con facilidad y rapidez a todo, pero por otra puede resultar hipócrita. Su distintivo común es la comunicación y el ingenio."
            datos["Elemento"]=" Aire"
            datos["Numero"]="3, 8, 12, 23"
            datos["Color"]="Verde, Amarillo"
            datos["Del_dia"]="Te espera un día de sucesos inesperados y fenómenos sorprendentes; de todas maneras, los viajes serán favorables. El camino hacia el futuro que quieres será posible si diriges tu energía de una forma constructiva. Por otra parte, podrías resolver asuntos pendientes durante los desplazamientos o viajes. Géminis, presta atención a lo que firmes."
            datos["Del_dia"]="Deberías procurar actuar bajo unas bases justas en lo que hagas hoy: trata de escuchar, de respetar las opiniones de los demás aunque sean opuestas a las tuyas y de pensar bien antes de emitir opiniones. Tienes que actuar con control si deseas llegar al éxito. Finalmente, será un buen día para las actividades legales y educativas."
            datos["Del_dia"]="Los problemas internos se podrán solucionar si utilizas tu vitalidad de una forma constructiva: no te precipites. Piensa con optimismo y trata de clarificar tus ideas; emocionalmente te sentirás bien hoy. Las personas con quienes trabajas, especialmente las que estén en una escala jerárquica superior a la tuya, te tienen en el punto de mira, por lo que deberás cumplir con tus tareas."
            datos["Del_dia"]="Lo mejor que podrías hacer hoy es buscar un encuentro contigo mismo-a: sigue a tu intuición. En el terreno económico deberías ordenar tus finanzas y pagar lo que debas. Si puedes, haz un curso de desarrollo o busca lectura en este sentido, algunas de tus preguntas tendrán respuestas así. Aprovecha la oportunidad."
            datos["Del_dia"]="Te espera un domingo maravilloso; te sentirás mucho mejor. No te aísles, Géminis, sal y diviértete con tus amigos-as o con la familia; será un día para expresar tus emociones positivamente. Hoy podrías conocer a una persona de fuera que puede convertirse en alguien significativo en tu vida futura."
            result = json.dumps(datos)
            return result


          elif dia>=21 and mes==6 or dia<=22 and mes==7:
            datos={}
            datos["Nombre"]="Cáncer"
            datos["Fecha"]="Junio 21 – Julio 22"
            datos["Descripcion"]="Cáncer es un signo cardinal y comprendido dentro de los signos de agua. De los signos zodiacales, su carácter es el menos claro; puede ser desde retraído, insociable y pelma, hasta deslumbrante, atractivo y admirado por los demás. A veces es demasiado soñador, por eso equivoca el mundo real con la utopía que ha construido en su cabeza: el refugio de las fantasías que adora."
            datos["Elemento"]=" Agua"
            datos["Numero"]="2, 7, 11, 16, 20, 25"
            datos["Color"]="Blanco"
            datos["Del_dia"]="Hoy será un día sorprendente, podrías recibir noticias sobre algo nuevo, como un proyecto que te traerá cosas positivas. Será un día de realizaciones también en el amor, te sentirás optimista y podrás analizar profundamente cualquier asunto; tu intuición también estará en su más elevado nivel. Cáncer, paga lo que debas y todo irá bien."
            datos["Del_dia"]="Tal vez tengas que solucionar hoy algunos imprevistos familiares: trata de no alterarte ni de exagerar, al contrario. Utiliza tu aspecto más positivo, que es el optimismo. En el terreno laboral tendrás un buen día de trabajo, además, las personas que trabajan contigo estarán dispuestas a colaborar contigo."
            datos["Del_dia"]="Será un día perfecto en el terreno económico, recibirás incluso regalos de amistades o personas cercanas. Un interesante asunto económico estará en puertas, alguien influyente se acercará y te ofrecerá algo beneficioso. En el plano íntimo, tendrás un día muy sensual: sal por la noche a un lugar romántico. !Felicidades!"
            datos["Del_dia"]="Hoy será un día maravilloso, las estrellas estarán de tu parte. El amor te sonríe, si puedes, planea un fin de semana con tu pareja o amistades; lo pasaréis bien. La mejor elección será un lugar en el que te sientas equilibrado-a y en armonía con la naturaleza. No desperdicies el día en discusiones familiares, ?vale?"
            datos["Del_dia"]="Hoy podrías sentirte defraudado-a o desilusionado-a por alguien a quien quieres; lo mejor será no ser intolerante o intransigente con esa persona: trata de mostrarte humano-a y todo se solucionará. Aunque pienses que tienes la razón, no tiene caso que discutas. Aprovecha el día para disfrutar con tus amistades."
            result = json.dumps(datos)
            return result


          elif dia>=23 and mes==7 or dia<=22 and mes==8:
            datos={}
            datos["Nombre"]="Leo"
            datos["Fecha"]="Julio 23–Agosto 22"
            datos["Descripcion"]="El signo de Leo es fijo y de fuego, también el signo más dominante del zodíaco. Creativo y abierto, tiene ambición, valor, fuerza, autonomía y total seguridad en sí mismo: sabe dónde quiere llegar y nada ni nadie podrá evitarlo. En contrapartida, sus puntos negativos pueden ser tantos como las virtudes que tiene: vanidad, egocentrismo, arrogancia, impostura y un genio de mil demonios, entre otros defectos."
            datos["Elemento"]="Fuego"
            datos["Numero"]="1, 4, 10, 13, 19, 22"
            datos["Color"]="Oro, Naranja, Blanco, Rojo"
            datos["Del_dia"]="Hoy tendrás un día muy positivo y feliz en el que contarás con la energía necesaria para iniciar cualquier proyecto que te propongas. La clave será innovar y aceptar la responsabilidad que eso conlleva. Habrá vitalidad y optimismo para ti en este día. Leo, también podría ser el inicio de una relación muy fructífera."
            datos["Del_dia"]="Disfrutarás de un día en que podrías recibir gratificaciones. Leo, hoy el derecho y la razón estarán de tu parte, siempre y cuando no seas intransigente en tus relaciones con los demás. Tendrás la oportunidad de vivir un encuentro contigo mismo-a para poner en orden tu vida. !Cuidado con los asuntos relacionados con la ley!"
            datos["Del_dia"]="Hoy podrían darse sucesos inesperados y fenómenos que te sorprenderán: acepta la prueba, no intervengas. La atención y la prudencia serán las mejores aliadas con que podrás contar. Leo, trata de no beber, conduce con cuidado y deja tu coche en un lugar seguro. Este día será especialmente positivo si se lo dedicas a tu faceta más espiritual."
            datos["Del_dia"]="Si logras el equilibrio interno, ganarás. Hoy será un día magnífico para aprender, para conocer otras ideas y también para meditar o leer sobre temas que estimulen tu curiosidad. De todos modos, si no quieres, aprovecha el día para disfrutar en companía de las personas importantes de tu vida."
            datos["Del_dia"]="Tendrás un día de abundancia, sobre todo en lo que se refiere al terreno familiar y sentimental. Comparte tu mesa y alegrías con tus amistades, pareja y familia. Tus proyectos fructificarán y tendrás que ser generoso-a: confía en ti mismo-a y en los demás. Lo peor que podrías hacer hoy será aislarte, te entristecerá."
            result = json.dumps(datos)
            return result


          elif dia>=23 and mes==8 or dia<=22 and mes==9:
            datos={}
            datos["Nombre"]="Virgo"
            datos["Fecha"]="Agosto 23 – Septiembre 22"
            datos["Descripcion"]="Virgo es un signo mutable y de tierra; representado por una virgen, es un signo caracterizado por su espíritu crítico, precisión, reserva, paciencia y convencionalismo. También es lógico, metódico y aplicado, le gusta aprender y es capaz de analizar las situaciones más complejas con una claridad pasmosa."
            datos["Elemento"]="Tierra"
            datos["Numero"]="5, 14, 23, 32, 41, 50"
            datos["Color"]="Blanco, Amarillo, Beige, Verde Bosque"
            datos["Del_dia"]="Será un día importante para el amor y la amistad: trata de actuar de una forma equilibrada y de no ser intransigente. Es momento de poner en orden las cosas de tu vida. Virgo, si tienes dudas respecto a algo, háblalo con alguien de tu confianza, es posible que su punto de vista te proporcione un nuevo prisma."
            datos["Del_dia"]="Hoy será un día donde tendrás que moverte con rectitud, ser prudente y permanecer alerta ante lo que acontezca. El aprendizaje estará en la discreción, será un muy buen día para las actividades que se dediquen al bienestar físico y espiritual; el servicio hacia la sociedad será recompensado por diferentes personas, pues te ganarás su confianza."
            datos["Del_dia"]="Hoy te sentirás mucho mejor y recibirás gratificaciones o regalos, también la ayuda de alguien. Se materializarán algunos proyectos, además, te encontrarás en buena forma intelectual; sin embargo, es necesario que dejes que tus sentimientos ocupen su lugar y que tu corazón hable... A veces, te olvidas de esta faceta de la vida."
            datos["Del_dia"]="Disfrutarás de un día maravilloso que deberías dedicar a los tuyos. Sigue a tus instintos y se desarrollará tu creatividad. Habrá abundancia en el terreno material: compártela con quienes más quieres. Una buena opción será salir a comer fuera con tus amigos-as o pareja y también ir a conciertos y otras actividades culturales. !Felicidades!"
            datos["Del_dia"]="Virgo, no discutas, y menos con tu familia, no te traerá nada positivo. Mejor utiliza la energía de una forma positiva, expresa tus sentimientos, escribe aunque simplemente sea para ti mismo-a. Tus sueńos te darán respuestas. Sal al cine con los amigos a ver una película que os interese o haz cualquier cosa que evite que te aísles."
            result = json.dumps(datos)
            return result


          elif dia>=23 and mes==9 or dia<=22 and mes==10:
            datos={}
            datos["Nombre"]="Libra"
            datos["Fecha"]="Septiembre 23 – Octubre 22"
            datos["Descripcion"]="Libra es un signo cardinal y de aire, se encuentra además entre los signos más refinados del zodíaco; tiene elegancia, encanto, diplomacia y buen gusto, ama la belleza, es muy curioso por naturaleza y odia los conflictos. Sus puntos negativos a veces son la frivolidad y un carácter voluble."
            datos["Elemento"]="Aire"
            datos["Numero"]="6, 15, 24, 33, 42, 51, 60"
            datos["Color"]="Azul verde"
            datos["Del_dia"]="Este será un buen día para ti, pues tu mente estará muy creativa. Brillará el amor y la grandeza en tu vida. Si eres padre o madre, los asuntos relacionados con los hijos serán de vital importancia durante toda la semana. Por otro lado, hoy podría ser un día de realizaciones, sobre todo para las actividades innovadoras y creativas."
            datos["Del_dia"]="Disfrutarás de un día de plena fertilidad, lo que hoy empieces a poner en marcha, te dará sus frutos. Los aspectos estarán a favor: utiliza tus relaciones. Libra, hoy podrías experimentar algunos cambios en el plano emocional más o menos radicales, pero, a pesar de ello será buen día para las relaciones y el arte."
            datos["Del_dia"]="Te espera un día magnífico; aparecerá algo totalmente nuevo que tal vez tenga que ver con un contrato provechoso: acepta la oportunidad, tu trabajo será valorado. Además, será un buen día para quienes se dediquen a la espiritualidad, a la filosofía, a la educación, sobre todo dirigidas hacia ninos o jóvenes. !Felicidades!"
            datos["Del_dia"]="Será el día perfecto para las reuniones familiares, para pasarlo con la pareja y en companía de los mejores amigos. Para quienes estén en un camino espiritual, será una jornada para hacer una meditación o leer sobre el tema, pues a través de esto, se les revelará información interesante para el desarrollo espiritual."
            datos["Del_dia"]="Hoy harás nuevos descubrimientos y será un día para pasarlo en companía de tu pareja; en este sentido, tus relaciones estarán en uno de sus mejores momentos, sobre todo si ves a tu pareja como a alguien que te apoya y va a tu lado en el camino del crecimiento y del amor real. Compartiréis una relación madura y a la vez conservaréis la individualidad."
            result = json.dumps(datos)
            return result

          elif dia>=23 and mes==10 or dia<=21 and mes==11:
            datos={}
            datos["Nombre"]="Escorpio"
            datos["Fecha"]="Octubre 23 – Noviembre 21"
            datos["Descripcion"]="Escorpio es un signo fijo y de agua; su potencia y energía emocional son únicas en todo el zodíaco. Tiene mucha imaginación e intuición, además de una gran capacidad para el análisis, fuerza de voluntad y firmeza, aunque también es muy sensible y emocional consigo mismo y con el entorno."
            datos["Elemento"]="Agua"
            datos["Numero"]="9, 18, 27, 36, 45, 54, 63, 72, 81, 90"
            datos["Color"]="Escarlata, Rojo"
            datos["Del_dia"]="Te espera un día difícil en el ámbito emocional y en las relaciones, sobre todo afectivas; tendrás que actuar con templanza. Tal vez tengas dificultades para realizar contactos, esto se deberá a una comunicación deficiente o confusa. En el trabajo sería recomendable que te concentrases y que solucionases ya lo que tengas pendiente."
            datos["Del_dia"]="Escorpio, por la mańana hoy habrá aún cierta tensión: no discutas con quienes más quieres, mejor sigue a tu intuición, te ayudará. En el terreno del trabajo no será recomendable que cierres contratos; sin embargo, hoy podrías conseguir el prestigio y el reconocimiento a tu trabajo."
            datos["Del_dia"]="Hoy será un día para pasarlo bien con los amigos y con tu pareja, si la tienes, pues tu sensualidad estará a flor de piel. Además, si deseas procrear será el día perfecto, pues habrá fertilidad para sembrar cualquier cosa, desde una planta, un bebe, hasta un proyecto. Escorpio, cualquier cosa que inicies tendrá el éxito asegurado."
            datos["Del_dia"]="Si tienes oportunidad, sal a hacer un pequeńo viaje, te hará muy bien; puede ser familiar, con la pareja o con tus amistades. El campo o un lugar en el que la energía de la armonía vibre sería lo más adecuado. Aprovecha este día tanto en tus emociones como en la sensualidad, porque estarán vibrando armoniosamente y será el momento de darles expresión. !Felicidades!"
            datos["Del_dia"]="Te sentirás muy vital y tu capacidad de organizar estará en un alto nivel para iniciar cualquier proyecto que te propongas. Escorpio, este domingo tus emociones serán intensas y tu intuición profunda. También será un buen día para pasarlo con la familia, una buena comida fuera de casa será la mejor alternativa."
            result = json.dumps(datos)
            return result


          elif dia>=22 and mes==11 or dia<=21 and mes==12:
            datos={}
            datos["Nombre"]="Sagitario"
            datos["Fecha"]="Noviembre 22 - Diciembre 21"
            datos["Descripcion"]="Sagitario pertenece a los signos mutables y su elemento es el fuego; es uno de los signos más resplandecientes y positivos del zodíaco. También es versátil, adora las aventuras y buscar nuevos horizontes, ya que tiene una mente abierta a nuevas ideas y experiencias y mantiene una actitud decidida ante la adversidad; además, frecuentemente la suerte le acompaña."
            datos["Elemento"]="Fuego"
            datos["Numero"]="3, 12, 21, 30"
            datos["Color"]="Violeta, Púrpura, Rojo, Rosa"
            datos["Del_dia"]="Hoy podrás aprovechar la energía de una forma creativa, así que resolverás los asuntos familiares y dudas profesionales. Utiliza tu optimismo y podrás iniciar nuevos proyectos. Tal vez tengas que cerrar algunos asuntos pendientes o determinar cuáles son los cambios que tienes que hacer en tu vida. Sé responsable con tus obligaciones."
            datos["Del_dia"]="Es posible que hoy te ofrezcan una asociación o proposición que conlleve un cambio total en tu vida ahora, como si estuvieras iniciando un camino totalmente nuevo; esto tiene que ver con el destino que hoy podría presentarse en tu vida. Sagitario, solamente deberás aceptar si realmente así lo deseas."
            datos["Del_dia"]="Hoy te sentirás fuerte y dominarás las situaciones: acepta los retos que se presenten, el poder, la voluntad y la tenacidad te llevarán al éxito. Estás en pleno dominio de tus fuerzas físicas y mentales: aprovecha el momento para cerrar contratos que sean beneficiosos y justos para ambas partes. Rechaza de tu vida sentimientos violentos y no exageres."
            datos["Del_dia"]="Este día será para pasarlo en companía de tu familia y tu pareja, con algunos amigos también, si es posible; habrá armonía. Sagitario, si puedes, haz un pequeńo viaje de fin de semana, el lugar más adecuado será un entorno natural: recréate con la armonía del paisaje y la naturaleza de la creación estés donde estés."
            datos["Del_dia"]="Recuerda: el intelecto no lo es todo, tienes que permitir también que la vida sentimental ocupe un lugar en tu vida. Hoy atenderás a tu pareja, te sentirás muy sensual; será un día apropiado para dedicarlo a este tema. Invítala a salir y trata de crear un ambiente romántico, tu media naranja te lo agradecerá. !Felicidades!"
            result = json.dumps(datos)
            return result
        except:
          datos={}
          datos["Error"]="Dato incorrecto"
          result = json.dumps(datos)
          return result 

          
if __name__ == "__main__":
    app.run()






    #https://horoscopo.lavanguardia.com/signos-zodiaco-sagitario
    #https://www.astrology-zodiac-signs.com/es/signos-del-zodiaco/sagitario/
    #https://www.astrology-zodiac-signs.com/es/


