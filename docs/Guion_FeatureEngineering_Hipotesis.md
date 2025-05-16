# Guion: Feature Engineering y Elaboración de Hipótesis para el Modelo de Satisfacción del Chatbot

## Introducción

¡Hola a todos! En el marco de nuestro proyecto para desarrollar un modelo de inteligencia artificial capaz de predecir la satisfacción estudiantil con un servicio de chatbot, hemos completado una fase crucial: el Análisis Exploratorio de Datos (AED).

Hoy nos centraremos en dos componentes esenciales de este AED que son vitales para preparar nuestros datos antes de entrenar cualquier modelo:
1.  La **Ingeniería de Características** (Feature Engineering).
2.  La **Elaboración de Hipótesis**.

Estas etapas nos permiten no solo comprender mejor nuestros datos, sino también transformarlos para maximizar su potencial predictivo.

## 1. Ingeniería de Características: Potenciando Nuestros Datos

### ¿Para qué sirve la Ingeniería de Características?

La ingeniería de características es el proceso de utilizar el conocimiento del dominio y técnicas estadísticas para transformar datos crudos en variables (o "features") que representen de manera más efectiva el problema subyacente que queremos resolver. En nuestro caso, buscamos predecir la satisfacción estudiantil.

**El enfoque principal de la ingeniería de características es:**

*   **Mejorar el rendimiento de los modelos de Machine Learning:** Algoritmos bien alimentados con características relevantes y bien diseñadas suelen aprender mejor y generar predicciones más precisas.
*   **Crear variables más informativas:** A menudo, las variables originales no capturan directamente las relaciones complejas que influyen en el resultado. La ingeniería de características nos permite construir nuevas variables que sí lo hagan.
*   **Adaptar los datos al modelo:** Algunos algoritmos requieren que los datos estén en un formato específico (por ejemplo, numérico, normalizado).
*   **Extraer el máximo valor predictivo:** Queremos asegurarnos de que estamos utilizando toda la información útil disponible en nuestro dataset para entender y predecir la satisfacción del estudiante con el chatbot.

### Pasos Realizados en la Ingeniería de Características

Basándonos en nuestro análisis previo y el conocimiento del dataset del chatbot, llevamos a cabo los siguientes pasos clave (detallados en el notebook `notebooks/04_feature_engineering.ipynb` y resumidos en nuestro ensayo principal):

1.  **Creación de Características Temporales:**
    *   A partir de la `fecha_consulta`, extrajimos componentes como el `año_consulta`, `mes_consulta_num` (mes numérico), `dia_semana`, `trimestre` y una variable booleana `es_fin_de_semana`. Esto nos permite analizar patrones temporales en la satisfacción.

2.  **Creación de Características de Tiempo de Servicio:**
    *   `tiempo_total_atencion`: Calculado como la suma de `tiempo_consulta` y `tiempo_espera`.
    *   `ratio_tiempo_espera_consulta`: El cociente entre `tiempo_espera` y `tiempo_consulta`, para entender la proporción del tiempo que un estudiante espera en relación con el tiempo que interactúa. **Por ejemplo, un ratio alto (ej. 2.0) significaría que un estudiante esperó el doble del tiempo que duró su consulta efectiva, lo cual podría ser un fuerte indicador de frustración, incluso si el tiempo de consulta en sí fue breve. Un ratio bajo (ej. 0.1) indicaría una espera mínima en comparación con la duración de la interacción.**
    *   `categoria_tiempo_espera`: Clasificamos el `tiempo_espera` en categorías (ej. "Corto", "Medio", "Largo") para simplificar su análisis.

3.  **Creación de Características de Calidad y Satisfacción Compuestas:**
    *   `calidad_resolucion`: Una variable que combina la `calidad_del_servicio` reportada con si la `consulta_resuelta`. **Por ejemplo, un estudiante podría tener una alta `calidad_resolucion` si calificó el servicio como 'Bueno' (alta `calidad_del_servicio`) Y su consulta fue marcada como `resuelta` (True). Sería baja si la calidad fue 'Mala' aunque estuviese resuelta, o si no fue resuelta.**
    *   `satisfaccion_general`: Una posible métrica combinada, por ejemplo, promediando `satisfaccion_estudiante` e `indice_promotor_neto`. **Por ejemplo, si un estudiante otorga una `satisfaccion_estudiante` de 5/5 y un `indice_promotor_neto` de 10 (en una escala de 0-10), la `satisfaccion_general` reflejaría un alto nivel combinado. Por el contrario, una satisfacción de 1/5 y un NPS de 2 indicaría una baja satisfacción general.** (Esto asumiría que ambas métricas están en escalas comparables o han sido normalizadas antes de promediar).
    *   `eficiencia_servicio`: Una variable que podría relacionar si la `consulta_resuelta` con el `tiempo_total_atencion`. **Por ejemplo, una consulta resuelta (`consulta_resuelta` = True) en un `tiempo_total_atencion` de solo 5 minutos se consideraría de alta eficiencia. En cambio, una consulta que toma 30 minutos y no se resuelve (`consulta_resuelta` = False) indicaría baja eficiencia.**

4.  **Codificación de Variables Categóricas:**
    *   **One-Hot Encoding:** Lo aplicamos a variables como `tipo_consulta` y `mes_consulta` (en su forma textual original). Esto crea nuevas columnas binarias para cada categoría, permitiendo que el modelo las utilice sin asumir un orden entre ellas.
    *   **Ordinal Encoding:** Para la variable `urgencia` (con niveles como "Baja", "Media", "Alta"), usamos codificación ordinal para convertirla a números que reflejen su jerarquía inherente.

5.  **Creación de Características de Interacción:**
    *   Exploramos cómo diferentes variables interactúan entre sí, por ejemplo: `urgencia_tiempo_espera` (interacción entre urgencia y tiempo de espera) o `calidad_tiempo_consulta`.

6.  **Normalización de Características:**
    *   Aplicamos `MinMaxScaler` a un conjunto de variables numéricas (incluyendo las recién creadas). Esto escala los valores a un rango común (generalmente entre 0 y 1), lo cual es importante para muchos algoritmos de Machine Learning que son sensibles a las diferentes escalas de las características.

Como resultado de este proceso, generamos un nuevo dataset, `data/chatbot_satisfaction_dataset_engineered.csv`. Este dataset enriquecido contiene tanto las variables originales como las nuevas características diseñadas, y está mucho mejor preparado para el entrenamiento de nuestro modelo de IA.

## 2. Elaboración de Hipótesis: Guiando Nuestro Análisis

### ¿Por qué formulamos hipótesis?

Paralelamente a la transformación de los datos, es crucial formular hipótesis. Las hipótesis son suposiciones informadas sobre las posibles relaciones entre diferentes variables en nuestro dataset, especialmente en relación con nuestra variable objetivo: la `satisfaccion_estudiante`.

**Formular hipótesis nos ayuda a:**

*   **Estructurar nuestro pensamiento:** Nos obliga a pensar críticamente sobre qué factores podrían ser importantes.
*   **Definir preguntas claras:** Cada hipótesis se traduce en una pregunta específica que podemos intentar responder con los datos.
*   **Guiar el análisis estadístico:** Las hipótesis nos indican qué pruebas estadísticas podrían ser apropiadas para validar (o refutar) nuestras suposiciones.
*   **Interpretar los resultados:** Una vez que tenemos los resultados del modelo o de los análisis, las hipótesis proporcionan un marco para entender lo que significan.

### Proceso de Formulación y Ejemplos de Hipótesis

Nuestras hipótesis se basaron en el análisis exploratorio inicial, el diccionario de datos y el conocimiento general sobre la atención al cliente y la satisfacción. Las estructuramos claramente con:

*   Una **Pregunta** de investigación.
*   Una **Hipótesis nula (H₀)**: Generalmente establece que no hay efecto o relación.
*   Una **Hipótesis alternativa (H₁)**: Establece que sí hay un efecto o relación.
*   Un **Tipo de prueba** sugerido para investigarla.

Aquí algunos ejemplos de las hipótesis que formulamos (la lista completa está en nuestro ensayo):

*   **Pregunta:** ¿Un tiempo de espera prolongado se correlaciona negativamente con la satisfacción del estudiante?
    *   **H₁:** Un `tiempo_espera` prolongado se correlaciona negativamente con la `satisfaccion_estudiante`.
*   **Pregunta:** ¿Una alta `calidad_del_servicio` se correlaciona positivamente con una alta `satisfaccion_estudiante`?
    *   **H₁:** Una alta `calidad_del_servicio` se correlaciona positivamente con una alta `satisfaccion_estudiante`.
*   **Pregunta:** ¿Las consultas resueltas (`consulta_resuelta` = True) tienen, en promedio, una satisfacción del estudiante significativamente mayor que las no resueltas?
    *   **H₁:** Las consultas marcadas como `consulta_resuelta` (True) tendrán, en promedio, una `satisfaccion_estudiante` significativamente mayor.
*   **Pregunta:** ¿El `puntaje_esfuerzo_cliente` (CES) se correlaciona negativamente con la `satisfaccion_estudiante`?
    *   **H₁:** El `puntaje_esfuerzo_cliente` se correlaciona negativamente con la `satisfaccion_estudiante`.
*   **Pregunta:** ¿Un `indice_promotor_neto` (NPS) alto se correlaciona positivamente con una alta `satisfaccion_estudiante`?
    *   **H₁:** Un `indice_promotor_neto` alto se correlaciona positivamente con una alta `satisfaccion_estudiante`.

Estas hipótesis ahora guiarán nuestros análisis estadísticos más profundos y nos ayudarán a interpretar los resultados del modelo de predicción.

## Conclusión del Guion

En resumen, la **Ingeniería de Características** nos ha permitido transformar y enriquecer nuestro dataset, creando variables más significativas. Por otro lado, la **Elaboración de Hipótesis** nos ha proporcionado un marco estructurado para investigar las relaciones dentro de nuestros datos.

Ambas etapas son fundamentales y nos dejan en una excelente posición para el siguiente paso: utilizar nuestro dataset ingenierizado y nuestras hipótesis para entrenar, evaluar y validar un modelo de inteligencia artificial que pueda predecir eficazmente la satisfacción estudiantil con el servicio de chatbot, con el objetivo final de mejorarlo.

¡Gracias! 