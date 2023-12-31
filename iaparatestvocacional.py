import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import os  # Importa la librería os para manipular rutas de archivos

# Define la ruta de la carpeta para la retroalimentación
carpeta_retroalimentacion = 'retroalimentacion'

# Asegúrate de que la carpeta exista; si no, créala
if not os.path.exists(carpeta_retroalimentacion):
    os.makedirs(carpeta_retroalimentacion)

# Definir las preguntas y respuestas de muestra
preguntas = [
"¿Te gustan las matemáticas?",
"¿Disfrutas resolviendo problemas de programación?",
"¿Eres bueno/a en ciencias?",
"¿Te interesan las artes visuales?",
"¿Disfrutas trabajando con personas?",
"¿Prefieres trabajar en equipo o individualmente?",
"¿Te sientes atraído por la idea de analizar datos y tomar decisiones importantes para una organización?",
 "¿Disfrutas de la creatividad y la planificación para diseñar proyectos o resolver problemas?",
 "¿Eres bueno en el manejo de números y la interpretación de datos financieros?",
 "¿Sientes curiosidad por comprender cómo funcionan los procesos biológicos a nivel molecular?",
 "¿Te interesa la aplicación de la tecnología para mejorar la vida de las personas?",
 "¿Eres bueno en la resolución de problemas técnicos y mecánicos?",
 "¿Te atrae la idea de trabajar con circuitos electrónicos y sistemas de comunicación?",
 "¿Eres un amante de la tecnología y disfrutas programando o trabajando en desarrollo de software?",
 "¿Te interesa el manejo de sistemas de información y la seguridad informática?",
 "¿Eres bueno en la optimización de procesos y la mejora de la eficiencia?",
 "¿Disfrutas del trabajo en laboratorios y la investigación científica?",
 "¿Te preocupa la sostenibilidad y el impacto ambiental de las actividades humanas?",
 "¿Tienes habilidades para el diseño y la planificación de proyectos a gran escala?",
 "¿Eres bueno en la gestión de recursos y presupuestos?",
 "¿Te atrae la idea de diseñar y supervisar la construcción de estructuras físicas?",
 "¿Eres bueno en el análisis de materiales y estructuras?",
 "¿Tienes interés en el diseño y operación de procesos químicos?",
 "¿Disfrutas de la programación y el diseño de sistemas de software?",
 "¿Te sientes cómodo trabajando en equipo y liderando proyectos?",
 "¿Eres bueno en el análisis de costos y presupuestos?",
 "¿Te preocupa la ética y la integridad en el trabajo?",
 "¿Eres hábil en la gestión de proyectos y equipos?",
 "¿Te interesa el diseño y la planificación de espacios y edificios?",
 "¿Disfrutas de la investigación y el desarrollo en ciencias biológicas?",
 "¿Eres bueno en el diseño y optimización de procesos químicos y biológicos?",
 "¿Te preocupas por la seguridad y la regulación en la industria química y biotecnológica?",
 "¿Eres hábil en la integración de sistemas eléctricos y mecánicos?",
 "¿Te sientes atraído por la electrónica y el diseño de circuitos?",
 "¿Eres bueno en la resolución de problemas algorítmicos y el desarrollo de software?",
 "¿Tienes interés en la gestión empresarial y la toma de decisiones basadas en datos?",
 "¿Te atrae la idea de trabajar en la gestión de recursos humanos y financieros de una empresa?",
 "¿Eres bueno en la planificación estratégica y el desarrollo organizacional?",
 "¿Disfrutas analizando el mercado y desarrollando estrategias de marketing?",
 "¿Sientes una inclinación natural hacia el liderazgo y la gestión de equipos?",
 "¿Te ves resolviendo problemas empresariales de manera efectiva en el futuro?",
 "¿Tienes interés en conocer la legislación comercial y laboral?",
 "¿Valoras la importancia de la comunicación efectiva en la gestión empresarial?",
 "¿Te ves aplicando principios éticos en tu carrera profesional?",
 "¿Tienes habilidades para diseñar espacios y edificios de manera creativa?",
 "¿Eres hábil en el uso de software de modelado arquitectónico?",
 "¿Te interesa aprender sobre diversos estilos arquitectónicos?",
 "¿Valoras la sostenibilidad en la planificación urbana?",
 "¿Sientes curiosidad por los materiales de construcción y las tecnologías modernas?",
 "¿Te ves trabajando en el cumplimiento de regulaciones y normativas de construcción?",
 "¿Eres capaz de combinar estética y funcionalidad en tus diseños?",
 "¿Tienes un fuerte sentido de responsabilidad en la supervisión de proyectos?",
 "¿Te atrae la idea de evaluar el impacto ambiental de tus proyectos?",
 "¿Eres bueno en la gestión de recursos y presupuestos de construcción?",
 "¿Disfrutas de la ingeniería electromecánica y la integración de sistemas?",
 "¿Sientes una pasión por el diseño y mantenimiento de equipos industriales?"
]

respuestas_usuario = []

# Supongamos que estas son algunas carreras relacionadas con las preguntas
carreras_tec_tijuana = [
 "ingenieria-en-sistemas-computacionales",
 "licenciatura-en-administracion-de-empresas",
 "Administración",
 "Arquitectura",
 "Contador Público",
 "Ingeniería Bioquímica",
 "Ingeniería Civil",
 "Ingeniería Electromecánica",
 "Ingeniería Electrónica",
 "Ingeniería en Gestión Empresarial",
 "Ingeniería en Logística",
 "Ingeniería en Nanotecnología",
 "Ingeniería en Sistemas Computacionales",
 "Ingeniería en Tecnologías de la Información y Comunicación",
 "Ingeniería Industrial",
 "Ingeniería Química",
 "ingenieria-en-sistemas-computacionales",
 "licenciatura-en-administracion-de-empresas",
 "Administración",
 "Arquitectura",
 "Contador Público",
 "Ingeniería Bioquímica",
 "Ingeniería Civil",
 "Ingeniería Electromecánica",
 "Ingeniería Electrónica",
 "Ingeniería en Gestión Empresarial",
 "Ingeniería en Logística",
 "Ingeniería en Nanotecnología",
 "Ingeniería en Sistemas Computacionales",
 "Ingeniería en Tecnologías de la Información y Comunicación",
 "Ingeniería Industrial",
 "Ingeniería Química",
 "ingenieria-en-sistemas-computacionales",
 "licenciatura-en-administracion-de-empresas",
 "Administración",
 "Arquitectura",
 "Contador Público",
 "Ingeniería Bioquímica",
 "Ingeniería Civil",
 "Ingeniería Electromecánica",
 "Ingeniería Electrónica",
 "Ingeniería en Gestión Empresarial",
 "Ingeniería en Logística",
 "Ingeniería en Nanotecnología",
 "Ingeniería en Sistemas Computacionales",
 "Ingeniería en Tecnologías de la Información y Comunicación",
 "Ingeniería Industrial",
 "Ingeniería Química",
 "ingenieria-en-sistemas-computacionales",
 "licenciatura-en-administracion-de-empresas",
"ingenieria-en-sistemas-computacionales",
"licenciatura-en-administracion-de-empresas",
"Administración",
"Arquitectura",
"Contador Público",
"Ingeniería Bioquímica",


    # ... (otras carreras) ...
]
# Crear una base de datos de características de carrera (como se mencionó anteriormente)
caracteristicas_carrera ={
    "Administración": [
        "Enfoque en la toma de decisiones empresariales.",
        "Gestión de recursos humanos y financieros.",
        "Planificación estratégica y desarrollo organizacional.",
        "Análisis de mercado y estrategias de marketing.",
        "Habilidades de liderazgo y gestión.",
        "Evaluación de riesgos empresariales.",
        "Conocimiento de la legislación comercial y laboral.",
        "Habilidad para resolver problemas empresariales.",
        "Comunicación efectiva y trabajo en equipo.",
        "Aplicación de principios éticos en la gestión empresarial."
    ],
    "Arquitectura": [
        "Diseño de espacios y edificios.",
        "Utilización de software de modelado arquitectónico.",
        "Conocimiento de estilos arquitectónicos.",
        "Planificación urbana y sostenibilidad.",
        "Uso de materiales de construcción y tecnologías modernas.",
        "Comunicación con clientes y equipos de construcción.",
        "Cumplimiento de regulaciones y normativas de construcción.",
        "Habilidad para combinar estética y funcionalidad.",
        "Diseño y supervisión de proyectos arquitectónicos.",
        "Consideración de factores ambientales y culturales en el diseño."
    ],
    "Contador Público": [
        "Llevar registros contables y financieros.",
        "Auditoría y verificación de estados financieros.",
        "Cumplimiento de normativas fiscales y contables.",
        "Análisis de costos y presupuestos.",
        "Asesoramiento financiero a individuos y empresas.",
        "Resolución de problemas fiscales y financieros.",
        "Gestión de riesgos financieros.",
        "Utilización de software contable.",
        "Énfasis en la ética y la integridad profesional.",
        "Comunicación efectiva de información financiera."
    ],
    "Ingeniería Bioquímica": [
        "Estudio de procesos biológicos a nivel molecular.",
        "Desarrollo de productos farmacéuticos y biotecnológicos.",
        "Investigación y desarrollo en biotecnología.",
        "Diseño y optimización de procesos químicos y biológicos.",
        "Análisis de biomoléculas y genómica.",
        "Énfasis en la seguridad y la regulación en la industria química y biotecnológica.",
        "Uso de tecnologías avanzadas, como la ingeniería genética.",
        "Trabajo en laboratorios de investigación y desarrollo.",
        "Sostenibilidad y consideraciones medioambientales.",
        "Aplicación de principios éticos en la investigación y desarrollo bioquímico."
    ],
    "Ingeniería Civil": [
        "Diseño y construcción de infraestructuras civiles.",
        "Planificación y gestión de proyectos de construcción.",
        "Análisis de estructuras y materiales de construcción.",
        "Estudio de la mecánica de suelos y cimentaciones.",
        "Gestión de recursos y presupuestos de construcción.",
        "Cumplimiento de normativas de seguridad y construcción.",
        "Ingeniería de transporte y tráfico.",
        "Diseño de puentes, carreteras y edificios.",
        "Evaluación de impacto ambiental.",
        "Gestión de proyectos de gran envergadura."
    ],
    "Ingeniería Electromecánica": [
        "Integración de sistemas eléctricos y mecánicos.",
        "Diseño y mantenimiento de maquinaria y equipos industriales.",
        "Control de automatización y sistemas de control.",
        "Estudio de la energía y la eficiencia energética.",
        "Aplicaciones en sectores como la manufactura y la energía.",
        "Solución de problemas técnicos en equipos electromecánicos.",
        "Uso de software de diseño y simulación.",
        "Consideraciones de seguridad en el diseño de sistemas.",
        "Mantenimiento preventivo y predictivo.",
        "Optimización de procesos industriales."
    ],
    "Ingeniería Electrónica": [
        "Diseño y desarrollo de circuitos electrónicos.",
        "Tecnologías de comunicación y sistemas de telecomunicaciones.",
        "Electrónica de potencia y control.",
        "Uso de microcontroladores y sistemas embebidos.",
        "Desarrollo de dispositivos electrónicos y sensores.",
        "Electrónica de consumo y entretenimiento.",
        "Robótica y automatización industrial.",
        "Mantenimiento y reparación de equipos electrónicos.",
        "Investigación en nuevas tecnologías electrónicas.",
        "Diseño de sistemas de seguridad electrónica."
    ],
    "Ingeniería en Gestión Empresarial": [
        "Integración de conocimientos de ingeniería y gestión.",
        "Planificación estratégica empresarial.",
        "Gestión de proyectos y equipos de trabajo.",
        "Análisis de procesos y mejora continua.",
        "Toma de decisiones basadas en datos.",
        "Estudio de la cadena de suministro y logística.",
        "Comunicación empresarial y negociación.",
        "Desarrollo de habilidades de liderazgo.",
        "Énfasis en la innovación y la adaptabilidad.",
        "Gestión de riesgos empresariales."
    ],
    "Ingeniería en Logística": [
        "Optimización de la cadena de suministro.",
        "Gestión de inventarios y almacenes.",
        "Planificación de rutas de transporte.",
        "Uso de sistemas de información logística.",
        "Análisis de costos logísticos.",
        "Eficiencia en la distribución de productos.",
        "Gestión de operaciones de importación y exportación.",
        "Seguimiento y control de entregas.",
        "Consideraciones de sostenibilidad en logística.",
        "Adaptación a cambios en la demanda y el mercado."
    ],
    "Ingeniería en Nanotecnología": [
        "Manipulación de materiales a nivel nanométrico.",
        "Desarrollo de nanomateriales y nanodispositivos.",
        "Aplicaciones en electrónica, medicina y energía.",
        "Investigación en propiedades de nanoestructuras.",
        "Énfasis en la seguridad y ética en nanotecnología.",
        "Uso de tecnologías avanzadas de microfabricación.",
        "Aplicaciones en la medicina, como la nanomedicina.",
        "Diseño de sistemas y sensores nanotecnológicos.",
        "Potencial para revolucionar múltiples industrias.",
        "Colaboración interdisciplinaria con otras áreas de la ciencia."
    ],
    "Ingeniería en Sistemas Computacionales": [
        "Diseño y desarrollo de software y sistemas.",
        "Programación en múltiples lenguajes.",
        "Redes de computadoras y seguridad informática.",
        "Administración de bases de datos.",
        "Desarrollo de aplicaciones web y móviles.",
        "Análisis de requisitos y diseño de arquitectura.",
        "Resolución de problemas algorítmicos.",
        "Uso de metodologías ágiles de desarrollo.",
        "Colaboración en equipos de desarrollo.",
        "Actualización constante debido a la evolución tecnológica."
    ],
    "Ingeniería en Tecnologías de la Información y Comunicación": [
        "Enfoque en la convergencia de tecnologías.",
        "Redes de comunicación y telecomunicaciones.",
        "Desarrollo de soluciones TIC.",
        "Administración de sistemas y servicios de TI.",
        "Seguridad de la información y ciberseguridad.",
        "Aplicaciones en la nube y virtualización.",
        "Gestión de proyectos TIC.",
        "Integración de voz, datos y multimedia.",
        "Innovación en comunicaciones móviles y IoT.",
        "Adaptación a las demandas cambiantes de la comunicación digital."
    ],
    "Ingeniería Industrial": [
        "Optimización de procesos y sistemas.",
        "Análisis de la productividad y eficiencia.",
        "Diseño de sistemas de producción.",
        "Gestión de la cadena de suministro.",
        "Calidad y control de calidad.",
        "Investigación de operaciones y estadísticas.",
        "Ergonomía y diseño de lugares de trabajo.",
        "Gestión de proyectos industriales.",
        "Énfasis en la mejora continua.",
        "Aplicación de técnicas de gestión empresarial en entornos industriales."
    ]
}

# Crear un DataFrame para los datos
data = pd.DataFrame({'Pregunta': preguntas, 'Carrera': carreras_tec_tijuana})

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data['Pregunta'], data['Carrera'], test_size=0.2, random_state=42)

# Vectorización de texto usando TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Entrenar un modelo de clasificación más avanzado (por ejemplo, Random Forest)
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train_tfidf, y_train)

# Realizar una nueva predicción basada en las respuestas del usuario
for pregunta in preguntas:
    respuesta = input(f"{pregunta} (Si/No/Quiza/Me es indiferente): ").strip().lower()
    respuestas_usuario.append(respuesta)

# Verificar que la longitud de preguntas y respuestas_usuario sea la misma
if len(preguntas) != len(respuestas_usuario):
    print("El número de respuestas proporcionadas no coincide con el número de preguntas.")
else:
    # Continuar con el cálculo de similitud y recomendación de carreras
    nuevas_respuestas_tfidf = vectorizer.transform(respuestas_usuario)

    # Calcular la similitud entre las respuestas del usuario y las características de carrera
    similitud_carreras = {}
    for carrera, caracteristicas in caracteristicas_carrera.items():
        similitud = cosine_similarity(nuevas_respuestas_tfidf, vectorizer.transform(caracteristicas))
        similitud_carreras[carrera] = similitud.mean()

    # Ordenar las carreras por similitud en orden descendente
    carreras_recomendadas = sorted(similitud_carreras.keys(), key=lambda x: similitud_carreras[x], reverse=True)

    # Mostrar las carreras recomendadas
    print("\nCarreras recomendadas:")
    for carrera in carreras_recomendadas:
        print(carrera, "- Similitud:", similitud_carreras[carrera])


