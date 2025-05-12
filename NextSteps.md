# Avance AA2 - Indicaciones

## Punto 1 - Encontrar Un dataset que contenga las siguientes caracteristicas

- *Historial de Consultas y Respuestas*
    - *Qué necesito*: Registros completos de interacciones previas entre los estudiantes y el servicio de atención al cliente, incluyendo tanto las preguntas o mensajes de los usuarios como las respuestas dadas por el personal.
    - *Por qué*: Estos datos son la base para entrenar el modelo en la clasificación de intenciones y la generación de respuestas. Si ya están etiquetados, facilitarán el proceso de aprendizaje supervisado.
- *Categorías o Etiquetas de Intenciones*
    - *Qué necesito*: Una lista de las categorías o tipos de consultas más comunes que reciben (por ejemplo, "consulta sobre horarios", "solicitud de documentos", "queja").
    - *Por qué*: Estas etiquetas permitirán al modelo identificar automáticamente qué quiere el usuario con cada mensaje, un paso clave para dar respuestas relevantes.
- *Datos de Contexto Adicional (si están disponibles)*
    - *Qué necesito*: Información extra sobre los usuarios o las consultas, como la carrera del estudiante, el año de estudio o el canal de comunicación usado (correo, chat, etc.).
    - *Por qué*: Esto ayudará a personalizar las respuestas del chatbot según el perfil del usuario o el contexto, mejorando su utilidad.
- *Preguntas Frecuentes (FAQs) y Respuestas Estándar*
    - *Qué necesito*: Documentos o bases de conocimiento con preguntas comunes y sus respuestas predefinidas.
    - *Por qué*: Sirven como datos adicionales para entrenar el modelo o como base para respuestas automáticas a consultas simples.
- *Feedback de Usuarios (si existe)*
    - *Qué necesito*: Calificaciones, comentarios o encuestas de satisfacción sobre las respuestas dadas por el servicio de atención al cliente.
    - *Por qué*: Este feedback nos permitirá evaluar y mejorar las respuestas del chatbot, identificando áreas donde las respuestas actuales no son suficientes.
- *Datos de Interacciones en Múltiples Canales*
    - *Qué necesito*: Registros de consultas hechas a través de diferentes plataformas (WhatsApp, web, aplicaciones móviles, etc.).
    - *Por qué*: Queremos que el chatbot sea consistente y efectivo sin importar el canal que use el usuario.
- *Datos Temporales*
    - *Qué necesito*: Fechas y horas de las consultas registradas.
    - *Por qué*: Nos ayudará a analizar patrones (como picos de consultas en ciertos momentos) y a preparar el modelo para variaciones estacionales.


## Punto 2 - Generacion de un diccionario de datos segun las caracteristicas del dataset descrito

** Apartir de la informacion dada en el punto 1, acerca de las caracteristicas que necesito para mi dataset.
** Realiza un diccionario de datos base que me de todas los campos necesarios para poder comenzar con una analisis de datos.
** Considera que este diccionario de datos tendra como proposito entrenar un modelo de ML para un chatbot estudiantil.
** Considera como variable objetivo, la satisfaccion del estudiante.



## Punto 3 - Puntos que necesitariamos en el dataset

** Id del estudiante para tener en el contexto con que estudiante estamos hablando
** Fecha y mes, esto para el tema de cuando toque matricula, mayor trafico de consultas
** isDerived, booleano para saber si fue derivado a un asesor.
** tipoConsulta, "Consulta de matricula", "Consulta de tramites", "Queja"
** urgencia, "Alta", "Media", "Baja"
** tiempoConsulta, El tiempo que tarda en completarse una consulta desde que envio la primera vez.
** tiempoEspera, con propositos de analis indentificamos quien tarda mas en realizar la consulta, el asesor o el estudiante.
** idAsesor, asesor que resolvio la consulta
** calidadDelServicio, esto desde la informacion de la encuesta determina si la calidad del servicio fue buena o no (1 - 3)
** isResolved, booleano para saber la consulta fue resuelta o no.
** customer_satisfaction_score, Valoración cuantitativa (por ejemplo, de 1 a 5) que el estudiante otorga al servicio recibido, ampliamente utilizado en servicios de atención al client
** net_promoter_score, Índice que mide la probabilidad de que el estudiante recomiende el servicio a otros, clave para evaluar fidelidad y experiencia globa
** customer_effort_score, Puntaje de esfuerzo percibido por el estudiante para resolver su consulta, útil para dimensionar la facilidad de uso del canal 


## Punto 4 - Aproach

** Consideremos esto como una ayuda para el estudiante donde segun las opciones que elija, podamos ayudarlo facilitando su atencion y brindadole respuestas de manera mas rapida.