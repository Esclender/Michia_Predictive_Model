# Análisis Inicial del Dataset de Satisfacción del Chatbot Estudiantil

## Variables Irrelevantes o Redundantes

- **id_estudiante**: Es un identificador único del estudiante y no aporta información predictiva directa sobre la satisfacción.
- **id_asesor**: Similar al id del estudiante, este identificador no contribuye directamente al modelo predictivo de satisfacción.

## Variables Potencialmente Útiles

### Datos de la Consulta
- **fecha_consulta**: Permite analizar tendencias temporales y estacionalidades en las consultas.
- **mes_consulta**: Ayuda a identificar patrones mensuales en las solicitudes.
- **tipo_consulta**: El tipo de consulta puede influir en la satisfacción del estudiante.
- **urgencia**: El nivel de urgencia podría estar relacionado con la satisfacción y la calidad percibida del servicio.
- **tiempo_consulta**: El tiempo total de la consulta puede ser un indicador de eficiencia y satisfacción.
- **tiempo_espera**: Un tiempo de espera prolongado podría afectar negativamente la satisfacción del estudiante.

### Datos de Satisfacción
- **calidad_del_servicio**: Calificación directa de la calidad del servicio, relevante para predecir la satisfacción.
- **consulta_resuelta**: Indica si la consulta fue resuelta, lo cual es crucial para la satisfacción.
- **satisfaccion_estudiante**: Variable objetivo que mide la satisfacción del estudiante.
- **indice_promotor_neto**: Mide la probabilidad de que el estudiante recomiende el servicio, reflejando la satisfacción general.
- **puntaje_esfuerzo_cliente**: Indica el esfuerzo percibido por el estudiante, lo que puede influir en su satisfacción.

## Variables que Podrían Confundir al Modelo

- **mes_consulta**: Aunque útil, podría ser redundante si ya se considera la fecha completa.
- **derivado**: La derivación a un asesor podría no ser un factor determinante de satisfacción si no se contextualiza adecuadamente.
- **tiempo_espera y tiempo_consulta**: Si no se normalizan, podrían introducir sesgos debido a su escala.

## Relaciones Lógicas Potenciales

- Consultas con **alta urgencia** y **tiempos de espera prolongados** podrían correlacionarse con una menor satisfacción.
- Un **alto puntaje de calidad del servicio** y **consulta resuelta** suelen indicar una mayor satisfacción del estudiante.
- Estudiantes con **bajo puntaje de esfuerzo** y **alto índice de promotor neto** podrían ser más propensos a recomendar el servicio.
- Consultas de **tipo queja** con **baja calidad del servicio** podrían predecir una menor satisfacción y un menor índice de promotor neto. 