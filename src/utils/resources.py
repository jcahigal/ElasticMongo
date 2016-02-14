# -*- encoding: utf-8 -*-
'''
Created on 14/01/2016

@author: juanc352 (jchernandez@full-on-net.com)
'''
from __future__ import unicode_literals


class ElasticMongo(object):
    '''
    Class with information for elastic and mongo collections.
    '''

    # type fields
    ELASTIC_TYPE_BODY = 'body'
    ELASTIC_TYPE_TO = "headers.To"

    entries = [
        {
            "body": '''
                    MongoDB (de la palabra en inglés “humongous” que significa enorme) es un sistema de base de datos NoSQL 
                    orientado a documentos, desarrollado bajo el concepto de código abierto.

                    MongoDB forma parte de la nueva familia de sistemas de base de datos NoSQL.
                     En vez de guardar los datos en tablas como se hace en las base de datos relacionales,
                      MongoDB guarda estructuras de datos en documentos tipo JSON con un esquema dinámico 
                      (MongoDB llama ese formato BSON), haciendo que la integración de los datos en ciertas aplicaciones 
                      sea más fácil y rápida.
                    ''',
            "headers": {
                    "Content-Transfer-Encoding": "7bit",
                    "Content-Type": "text/plain; charset=us-ascii",
                    "Date": "2015-12-13T14:47:00Z",
                    "From": "donna.fulton@enron.com",
                    "Message-ID": "<8147308.1075851042328.JavaMail.evans@thyme>",
                    "Subject": "wiki MongoDB def",
                    "To": [
                            "steven.kean@enron.com",
                            "richard.shapiro@enron.com",
                            "james.steffes@enron.com",
                            "christi.nicolay@enron.com",
                            "sarah.novosel@enron.com",
                            "ray.alvarez@enron.com",
                            "sscott3@enron.com"
                    ]
            }
         },
        {
            "body": '''
                    El desarrollo de MongoDB empezó con la empresa de software 10gen en 2007 cuando estaban desarrollando una plataforma como servicio (PaaS) similar al conocido Google App Engine.5 En 2009 MongoDB fue lanzado como un producto independiente y publicado bajo la licencia de código abierto AGPL.6

                    En marzo de 2011, se lanzó la versión 1.4 y se consideró ya como una base de datos lista para su uso en producción.
                    ''',
            "headers": {
                    "Content-Transfer-Encoding": "7bit",
                    "Content-Type": "text/plain; charset=us-ascii",
                    "Date": "2015-12-13T16:47:00Z",
                    "From": "donna.fulton@enron.com",
                    "Message-ID": "<8147308.1075851042329.JavaMail.evans@thyme>",
                    "Subject": "wiki mongoDB history",
                    "To": [
                            "steven.kean@enron.com",
                            "richard.shapiro@enron.com",
                            "james.steffes@enron.com",
                            "christi.nicolay@enron.com",
                            "sarah.novosel@enron.com",
                            "ray.alvarez@enron.com",
                            "sscott3@enron.com",
                            "joe.connor@enron.com",
                            "dan.staines@enron.com",
                            "steve.montovano@enron.com",
                            "kevin.presto@enron.com",
                            "rogers.herndon@enron.com"
                    ]
            }
         },
        {
            "body": '''
                    Elasticsearch es un servidor de búsqueda basado en Lucene. Provee un motor de búsqueda de texto completo, distribuido y con capacidad de multi-tenencia con una interfaz web RESTful y con documentos JSON. Elasticsearch está desarrollado en Java y está publicado como código abierto bajo las condiciones de la licencia Apache.
                    ''',
            "headers": {
                    "Content-Transfer-Encoding": "7bit",
                    "Content-Type": "text/plain; charset=us-ascii",
                    "Date": "2015-02-02T11:47:00Z",
                    "From": "donna.fulton@enron.com",
                    "Message-ID": "<8147308.1075851042330.JavaMail.evans@thyme>",
                    "Subject": "wiki elasticsearch def",
                    "To": [
                            "steven.kean@enron.com",
                            "rogers.herndon@enron.com",
                            "mike.carson@enron.com",
                            "john.forney@enron.com",
                            "laura.podurgiel@enron.com",
                            "gretchen.lotz@enron.com"
                    ]
            }
         },
        {
            "body": '''
                    Shay Banon creó Compass en 2004.1 Mientras estaba pensando en la tercera versión de Compass se dio cuenta que sería necesario reescribir grandes partes de Compass para “crear una solución de búsqueda escalable”. Entonces creó “una solución construida desde el comienzo para ser distribuida” y utilizó una interfaz muy común, JSON sobre HTTP, adecuada también para programar lenguajes que no sean Java.1 Shay Banon liberó la primera versión de Elasticsearch en febrero de 2010.2

                    En junio de 2014, la compañía anunció la recaudación de U$S 70 millones en una ronda de financiación Serie C, tan solo 18 meses luego de haber formado la compañía. La ronda estuvo liderada por New Enterprise Associates (NEA). Otros financiadores incluyen Benchmark Capital e Index Ventures. Esta ronda obtuvo una financiación total de U$S 104 millones.
                    ''',
            "headers": {
                    "Content-Transfer-Encoding": "7bit",
                    "Content-Type": "text/plain; charset=us-ascii",
                    "Date": "2015-02-02T14:47:00Z",
                    "From": "donna.fulton@enron.com",
                    "Message-ID": "<8147308.1075851042331.JavaMail.evans@thyme>",
                    "Subject": "wiki elasticsearch history",
                    "To": [
                            "juan.hernandez@enron.com",
                            "miguel.garcia@enron.com",
                            "rudy.acevedo@enron.com",
                            "heather.kroll@enron.com",
                            "david.fairley@enron.com"
                    ]
            }
         },
        {
            "body": '''
                    Elasticsearch puede ser usada para buscar todo tipo de documentos. Provee búsqueda escalable, tiene tiempo de búsqueda cercano a tiempo real y soporta multi-tenencia.4 “Elasticsearch es distribuido, lo que significa que los índices pueden ser divididos en fragmentos y cada fragmento puede tener cero o más réplicas. Cada nodo alberga uno o más fragmentos, y actúa como un coordinador para delegar operaciones a los fragmentos correctos. El rebalanceo y ruteo se realizan automáticamente […]”.4

                    Utiliza Lucene e intenta hacer todas sus funciones disponibles a través de JSON y Java API. Soporta facetado y percolación,5 que puede ser útil para notificar si nuevos documentos coinciden con consultas registradas.

                    Otra funcionalidad llamada "gateway" maneja la persistencia a largo plazo del índice;6 por ejemplo, se puede recuperar un índice del gateway en caso de una caída del servidor. Elasticsearch soporta peticiones GET en tiempo real, lo que lo hace adecuado como una solución NoSQL,7 pero carece de transacciones distribuidas
                    ''',
            "headers": {
                    "Content-Transfer-Encoding": "7bit",
                    "Content-Type": "text/plain; charset=us-ascii",
                    "Date": "2015-02-02T16:47:00Z",
                    "From": "donna.fulton@enron.com",
                    "Message-ID": "<8147308.1075851042332.JavaMail.evans@thyme>",
                    "Subject": "wiki elasticsearch sumary",
                    "To": [
                            "david.fairley@enron.com",
                            "elizabeth.johnston@enron.com",
                            "bill.rust@enron.com",
                            "edward.baughman@enron.com",
                            "terri.clynes@enron.com",
                            "oscar.dalton@enron.com"
                    ]
            }
         },
        {
            "body": '''
                    El Big Data o Datos masivos es un concepto que hace referencia a la acumulación de grandes cantidades de datos y a los procedimientos usados para encontrar patrones repetitivos dentro de esos datos. El fenómeno del Big Data también es llamado datos a gran escala. En los textos científicos en español con frecuencia se usa directamente el término en inglés Big Data, tal como aparece en el ensayo seminal de Viktor Schönberger Big data: La revolución de los datos masivos.1

                    La disciplina dedicada a los datos masivos se enmarca en el sector de las tecnologías de la información y la comunicación. Esta disciplina se ocupa de todas las actividades relacionadas con los sistemas que manipulan grandes conjuntos de datos. Las dificultades más habituales vinculadas a la gestión de estas cantidades de datos se centran en la recolección y el almacenamiento,2 búsqueda, compartición, análisis,3 y visualización. La tendencia a manipular enormes cantidades de datos se debe a la necesidad en muchos casos de incluir dicha información para la creación de informes estadísticos y modelos predictivos utilizados en diversas materias, como los análisis de negocio, publicitarios, los datos de enfermedades infecciosas, el espionaje y seguimiento a la población o la lucha contra el crimen organizado.4

                    El límite superior de procesamiento ha ido creciendo a lo largo de los años. De esta forma, los límites fijados en 2008 rondaban el orden de petabytes a zettabytes de datos.5 Los científicos con cierta regularidad encuentran limites en el análisis debido a la gran cantidad de datos en ciertas áreas, tales como la meteorología, la genómica,6 la conectómica, las complejas simulaciones de procesos físicos7 y las investigaciones relacionadas con los procesos biológicos y ambientales,8 Las limitaciones también afectan a los motores de búsqueda en internet, a los sistemas finanzas y a la informática de negocios. Los data sets crecen en volumen debido en parte a la recolección masiva de información procedente de los sensores inalámbricos y los dispositivos móviles (por ejemplo las VANETs), del constante crecimiento de los históricos de aplicaciones (por ejemplo de los logs), cámaras (sistemas de teledetección), micrófonos, lectores de radio-frequency identification.9 10 La capacidad tecnológica per-cápita a nivel mundial para almacenar datos se dobla aproximadamente cada cuarenta meses desde los años ochenta.11 Se estima que en 2012 cada día fueron creados cerca de 2,5 trillones de bytes de datos''',
            "headers": {
                    "Content-Transfer-Encoding": "7bit",
                    "Content-Type": "text/plain; charset=us-ascii",
                    "Date": "2015-12-30T10:47:00Z",
                    "From": "donna.fulton@enron.com",
                    "Message-ID": "<8147308.1075851042333.JavaMail.evans@thyme>",
                    "Subject": "wiki big data def",
                    "To": [
                            "steven.kean@enron.com",
                            "oscar.dalton@enron.com",
                            "doug.sewell@enron.com",
                            "larry.valderrama@enron.com",
                            "nick.politis@enron.com"
                    ]
            }
         },
        {
            "body": '''
                    Existen muchísimas herramientas para tratar con Big Data. Nombres como Hadoop, NoSQL, Cassandra, Business Intelligence, Machine Learning, MapReduce… son sólo algunos de los más conocidos. Ellos tratan con algunos de los tres tipos de Big Data:15

                    Datos estructurados (Structured Data): Datos que tienen bien definidos su longitud y su formato, como las fechas, los números o las cadenas de caracteres. Se almacenan en tablas. Un ejemplo son las bases de datos relacionales y las hojas de cálculo.
                    Datos no estructurados (Unstructured Data): Datos en el formato tal y como fueron recolectados, carecen de un formato específico. No se pueden almacenar dentro de una tabla ya que no se puede desgranar su información a tipos básicos de datos. Algunos ejemplos son los PDF, documentos multimedia, e-mails o documentos de texto.
                    Datos semiestructurados (Semistructured Data): Datos que no se limitan a campos determinados, pero que contiene marcadores para separar los diferentes elementos. Es una información poco regular como para ser gestionada de una forma estándar. Estos datos poseen sus propios metadatos semiestructurados16 que describen los objetos y las relaciones entre ellos, y pueden acabar siendo aceptados por convención. Un ejemplo es el HTML, el XML o el JSON.
                    ''',
            "headers": {
                    "Content-Transfer-Encoding": "7bit",
                    "Content-Type": "text/plain; charset=us-ascii",
                    "Date": "2015-12-30T12:47:00Z",
                    "From": "donna.fulton@enron.com",
                    "Message-ID": "<8147308.1075851042334.JavaMail.evans@thyme>",
                    "Subject": "wiki big data tec",
                    "To": [
                            "fletcher.sturm@enron.com",
                            "chris.dorland@enron.com",
                            "jeff.king@enron.com",
                            "john.kinser@enron.com",
                            "matt.lorenz@enron.com",
                            "patrick.hansen@enron.com"
                    ]
            }
         },
        {
            "body": '''
                    ¿De dónde provienen todos estos datos? Los fabricamos directa e indirectamente segundo tras segundo. Un iPhone hoy en día tiene más capacidad de cómputo que la NASA cuando el hombre llegó a la luna17 por lo que la cantidad de datos generados por persona y en unidad de tiempo es muy grande. Catalogamos la procedencia de los datos según las siguientes categorías:18

        Generados por las personas: El hecho de enviar correos electrónicos por e-mail o mensajes por WhatsApp, publicar un estado en Facebook, tuitear contenidos o responder a una encuesta por la calle son cosas que hacemos a diario y que crean nuevos datos y metadatos que pueden ser analizados. Se estima que cada minuto al día se envían más de 200 millones de e-mails, se comparten más de 700.000 piezas de contenido en Facebook, se realizan dos millones de búsquedas en Google o se editan 48 horas de vídeo en YouTube.19 Por otro lado, las trazas de utilización en un sistema ERP, incluir registros en una base de datos o introducir información en una hoja de cálculo son otras formas de generar estos datos.
        Transacciones de datos: La facturación, las llamadas o las transacción entre cuentas generan información que tratada pueden ser datos relevantes. Un ejemplo más claro lo encontraremos en las transacciones bancarias: lo que el usuario conoce como un ingreso de X euros, la computación lo interpretará como una acción llevada a cabo en una fecha y momento determinado, en un lugar concreto, entre unos usuarios registrados, y más metadatos.
        E-marketing y web: Generamos una gran cantidad de datos cuando navegamos por internet. Con la web 2.0 se ha roto el paradigma webmaster-contenido-lector y los mismos usuarios se convierten en creadores de contenido gracias a su interacción con el sitio. Existen muchas herramientas de tracking utilizadas en su mayoría con fines de marketing y análisis de negocio. Los movimientos de ratón quedan grabados en mapas de calor y queda registro de cuánto pasamos en cada página y cuándo las visitamos.
        Machine to Machine (M2M): Son las tecnologías que comparten datos con dispositivos: medidores, sensores de temperatura, de luz, de altura, de presión, de sonido… que transforman las magnitudes físicas o químicas y las convierten en datos. Existen desde hace décadas, pero la llegada de las comunicaciones inalámbricas (Wi-Fi, Bluetooth, RFID…) ha revolucionado el mundo de los sensores. Algunos ejemplos son los GPS en la automoción o los sensores de signos vitales en la medicina.
        Biométrica: Son el conjunto de datos que provienen de la seguridad, defensa y servicios de inteligencia.20 Son cantidades de datos generados por lectores biométricos como escáneres de retina, escáneres de huellas digitales, o lectores de cadenas de ADN. El propósito de estos datos es proporcionar mecanismos de seguridad y suelen estar custodiadas por los ministerios de defensa y departamentos de inteligencia. Un ejemplo de aplicación es el cruce de ADN entre una muestra de un crimen y una muestra en nuestra base de datos.

                    ''',
            "headers": {
                    "Content-Transfer-Encoding": "7bit",
                    "Content-Type": "text/plain; charset=us-ascii",
                    "Date": "2015-12-30T14:47:00Z",
                    "From": "donna.fulton@enron.com",
                    "Message-ID": "<8147308.1075851042335.JavaMail.evans@thyme>",
                    "Subject": "wiki big data cap",
                    "To": [
                            "lloyd.will@enron.com",
                            "dduaran@enron.com",
                            "john.lavorato@enron.com",
                            "louise.kitchen@enron.com",
                            "greg.whalley@enron.com"
                    ]
            }
         }
    ]
