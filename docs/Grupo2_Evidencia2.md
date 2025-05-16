# Título del Ensayo: Análisis Exploratorio de Datos para un Modelo de Chatbot Estudiantil

**Nombre del Autor/Autores:** Grupo 2
**Afiliación Institucional:** CERTUS VI
**Nombre del Curso:** Inteligencia Artificial
**Nombre del Instructor:** [Nombre del Instructor]
**Fecha:** [Fecha Actual]

## Resumen

(Este ensayo presenta un análisis exploratorio de datos (AED) como parte de la evaluación de la calidad y relevancia de los datos para entrenar un modelo de inteligencia artificial. Se detalla la estructura del dataset, las librerías utilizadas, la elaboración del diccionario de datos, y los análisis univariado y bivariado, culminando con la formulación de hipótesis y la aplicación de ingeniería de características. El objetivo es asegurar la precisión y efectividad de un futuro modelo de chatbot estudiantil.)

## Introducción

(La inteligencia artificial (IA) ha revolucionado la manera en que las instituciones educativas interactúan con sus estudiantes. Un componente clave en esta transformación son los chatbots, que ofrecen respuestas instantáneas y personalizadas. Para asegurar la efectividad de un chatbot estudiantil, es crucial realizar un riguroso Análisis Exploratorio de Datos (AED) sobre el dataset que se utilizará para su entrenamiento. Este informe detalla el proceso de AED llevado a cabo, enfocado en evaluar la calidad y relevancia de los datos, y aplicar técnicas de pre-procesamiento necesarias. Se abordarán la descripción de las librerías empleadas, la construcción del diccionario de datos, los análisis univariado y bivariado, la formulación de hipótesis y la ingeniería de características.)

## Desarrollo

### Descripción de librerías a utilizar

Para el análisis exploratorio de datos y la preparación del dataset para el modelo de chatbot estudiantil, se utilizarán las siguientes librerías estándar de Python, ampliamente reconocidas en el campo de la ciencia de datos:

*   **Pandas:** Fundamental para la manipulación y análisis de datos. Se empleará para cargar, limpiar, transformar y explorar la estructura del dataset, como la gestión de tablas de datos (DataFrames).
*   **NumPy:** Esencial para el cálculo numérico en Python. Se utilizará para operaciones matemáticas eficientes sobre arrays y matrices, que son la base de muchos análisis estadísticos.
*   **Matplotlib:** Una librería versátil para la creación de visualizaciones estáticas, interactivas y animadas. Se usará para generar gráficos como histogramas, diagramas de dispersión y diagramas de caja, que ayudarán a comprender la distribución de las variables y las relaciones entre ellas.
*   **Seaborn:** Basada en Matplotlib, Seaborn proporciona una interfaz de alto nivel para dibujar gráficos estadísticos atractivos e informativos. Facilitará la creación de visualizaciones más complejas y estéticamente agradables para el análisis univariado y bivariado.
*   **Scikit-learn (sklearn):** Aunque su uso principal será en etapas posteriores para el entrenamiento del modelo de Machine Learning, algunas de sus utilidades, como funciones para el preprocesamiento de datos (escalado, codificación de variables categóricas) o la división de datos, podrían ser referenciadas o anticipadas durante el AED.

Estas librerías en conjunto proveen un ecosistema robusto para llevar a cabo un análisis exhaustivo y eficiente de los datos.

### Elaboración del Diccionario de Datos

A continuación, se presenta el diccionario de datos correspondiente al dataset que se utilizará para entrenar el modelo de ML para un chatbot estudiantil. La variable objetivo principal es la satisfacción del estudiante.

**Variables del Dataset**

| Campo                         | Tipo de Dato        | Descripción                                                                                                                                |
|-------------------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| id_estudiante                 | Alfanumérico/ID     | Identificador único del estudiante. Permite relacionar la interacción con datos de perfil y antecedentes.                                  |
| fecha_consulta                | Fecha               | Fecha de la consulta. Fundamental para analizar tendencias, estacionalidades y picos en solicitudes (por ejemplo, periodos de matrícula).   |
| mes_consulta                  | Numérico/Texto      | Mes de la consulta. Ayuda a identificar patrones temporales en las solicitudes.                                                           |
| derivado                    | Booleano            | Indica si la consulta fue derivada a un asesor (True) o no (False).                                                                        |
| tipo_consulta                 | Categórico          | Tipo de consulta realizada (ej. "Consulta de matrícula", "Consulta de trámites", "Queja").                                                 |
| urgencia                      | Categórico          | Nivel de urgencia de la consulta: "Alta", "Media" o "Baja".                                                                                |
| tiempo_consulta               | Numérico (segundos) | Tiempo total que tarda en completarse la consulta, desde el primer envío hasta la última interacción.                                        |
| tiempo_espera                 | Numérico (segundos) | Tiempo de espera registrado; útil para identificar si la demora se debe al estudiante o al asesor.                                           |
| id_asesor                     | Alfanumérico/ID     | Identificador del asesor que atendió o resolvió la consulta. Puede ser utilizado para análisis de desempeño o asignación de recursos.         |
| calidad_del_servicio          | Numérico            | Calificación de la calidad del servicio basada en encuestas, generalmente en una escala (1 a 3).                                               |
| consulta_resuelta             | Booleano            | Indica si la consulta fue resuelta (True) o no (False).                                                                                    |
| satisfaccion_estudiante       | Numérico            | Valoración cuantitativa de la satisfacción del estudiante, por ejemplo, en una escala de 1 a 5.                                              |
| indice_promotor_neto          | Numérico            | Índice que mide la probabilidad de que el estudiante recomiende el servicio a otros, evaluando fidelidad y experiencia global.                |
| puntaje_esfuerzo_cliente      | Numérico            | Puntaje que indica el esfuerzo percibido por el estudiante para resolver su consulta, reflejando la facilidad de uso del canal de atención.   |

**Recomendaciones y Mejoras a la Estructura (extraídas de `docs/DtaDicctionary.md`)**

1.  **Separación de Fecha y Hora:** Aunque se cuenta con la variable "fecha_consulta", se recomienda registrar también la hora (por ejemplo, "hora_consulta") para análisis más granulares, especialmente en periodos de alta demanda o picos de interacción.
2.  **Consolidación Temporal:** Se plantea mantener tanto "fecha_consulta" como "mes_consulta" por simplicidad analítica. No obstante, al registrar la fecha completa se puede derivar el mes durante el análisis, evitando redundancias.
3.  **Normalización de Variables:**
    *   Es fundamental que las variables categóricas (como "tipo_consulta" y "urgencia") cuenten con un conjunto definido de valores para evitar inconsistencias.
    *   Los campos de tiempo ("tiempo_consulta" y "tiempo_espera") deben estar expresados en la misma unidad (por ejemplo, segundos) para facilitar la comparación y el análisis.
4.  **Validación de Datos:**
    *   Los campos booleanos ("derivado" y "consulta_resuelta") deben controlar posibles valores nulos o inconsistentes.
    *   Es recomendable implementar restricciones o validaciones en la entrada de datos para los identificadores ("id_estudiante", "id_asesor") y así mantener la integridad referencial.

Esta estructura, con nombres de variables estandarizados en español, facilita el entendimiento y manejo de los datos tanto para análisis exploratorios como para el entrenamiento del modelo de ML.

### Análisis Univariado

En esta fase crucial del Análisis Exploratorio de Datos (AED), se procedió a examinar cada variable del dataset de forma individual. El objetivo principal fue comprender en profundidad las características intrínsecas de cada campo, su distribución, la presencia de valores atípicos (outliers), y la cantidad de datos faltantes. Este análisis es fundamental para asegurar la calidad de los datos y para informar las etapas subsecuentes de preprocesamiento y modelado.

**1. Análisis de Variables Numéricas**

Se analizaron las siguientes variables numéricas: `tiempo_consulta` (segundos), `tiempo_espera` (segundos), `calidad_del_servicio` (escala 1-3), `satisfaccion_estudiante` (escala 1-5), `indice_promotor_neto`, `puntaje_esfuerzo_cliente`.

*   **`tiempo_consulta` y `tiempo_espera`**:
    *   **Medidas de Tendencia Central y Dispersión**: Se calcularon la media, mediana, moda, desviación estándar y rango. Se observó que la media de `tiempo_consulta` podría ser mayor que la mediana, sugiriendo una distribución asimétrica a la derecha, posiblemente debido a algunas consultas excepcionalmente largas. Similarmente, `tiempo_espera` podría mostrar picos que influyen en su media.
    *   **Distribución**: Los histogramas y diagramas de caja (boxplots) revelaron las distribuciones de estas variables. Es común que las variables de tiempo muestren sesgos positivos. Los boxplots ayudan a visualizar la dispersión y a identificar outliers, que representarían consultas con tiempos inusualmente largos o cortos.

        `![Distribución de Tiempo de Consulta](assets/univariate_plots/hist_boxplot_tiempo_consulta.png)`
        *Interpretación del gráfico `tiempo_consulta`: El histograma muestra la frecuencia de los diferentes tiempos de consulta, y el boxplot resume estadísticamente la distribución, destacando la mediana, los cuartiles y los posibles outliers.*

        `![Distribución de Tiempo de Espera](assets/univariate_plots/hist_boxplot_tiempo_espera.png)`
        *Interpretación del gráfico `tiempo_espera`: Similar al anterior, este gráfico ilustra la distribución de los tiempos de espera, permitiendo identificar patrones y valores atípicos.*

    *   **Outliers**: Se identificaron outliers que podrían corresponder a consultas que se extendieron mucho o se resolvieron instantáneamente. Se evaluó si estos representan errores de datos o eventos genuinos que requieren consideración especial.
    *   **Valores Faltantes**: Se verificó la presencia de valores nulos, cuya existencia podría indicar fallos en el registro del tiempo.

*   **`calidad_del_servicio`**:
    *   **Medidas y Distribución**: Al ser una variable ordinal en una escala Likert (1-3), se analizaron las frecuencias de cada calificación. Un histograma y un boxplot muestran la proporción de respuestas para cada nivel de calidad.

        `![Distribución de Calidad del Servicio](assets/univariate_plots/hist_boxplot_calidad_del_servicio.png)`
        *Interpretación del gráfico `calidad_del_servicio`: El histograma muestra la frecuencia de cada calificación, y el boxplot ofrece una vista resumida de la tendencia central y dispersión de las calificaciones.*
    *   **Valores Faltantes**: Se cuantificaron los casos sin calificación, ya que esto podría sesgar la percepción de la calidad.

*   **`satisfaccion_estudiante` (Variable Objetivo)**:
    *   **Medidas y Distribución**: Similar a `calidad_del_servicio`, siendo una escala (1-5), se examinaron las frecuencias de cada nivel de satisfacción. El histograma y boxplot muestran la distribución.

        `![Distribución de Satisfacción del Estudiante](assets/univariate_plots/hist_boxplot_satisfaccion_estudiante.png)`
        *Interpretación del gráfico `satisfaccion_estudiante`: Estos gráficos son cruciales para entender la tendencia general de la satisfacción. El histograma muestra cuántos estudiantes dieron cada puntuación, y el boxplot resume esta distribución.*
    *   **Valores Faltantes**: La presencia de valores faltantes en la variable objetivo es crítica y se investigó su origen y manejo.

*   **`indice_promotor_neto` (NPS) y `puntaje_esfuerzo_cliente` (CES)**:
    *   **Medidas y Distribución**: Para el NPS y el CES, se observó la distribución de los puntajes. Histogramas y boxplots son útiles para entender la variabilidad y tendencia central de estas métricas clave.

        `![Distribución de Índice Promotor Neto](assets/univariate_plots/hist_boxplot_indice_promotor_neto.png)`
        *Interpretación del gráfico `indice_promotor_neto`: Visualiza cómo se distribuyen los puntajes que componen el NPS, permitiendo identificar la concentración de promotores, pasivos y detractores.*

        `![Distribución de Puntaje Esfuerzo Cliente](assets/univariate_plots/hist_boxplot_puntaje_esfuerzo_cliente.png)`
        *Interpretación del gráfico `puntaje_esfuerzo_cliente`: Muestra la distribución de los puntajes de esfuerzo, indicando qué tan fácil o difícil perciben los estudiantes la resolución de sus consultas.*
    *   **Outliers y Valores Faltantes**: Se revisaron valores extremos o faltantes.

**2. Análisis de Variables Categóricas**

Se analizaron las siguientes variables categóricas: `derivado` (Booleano), `tipo_consulta`, `urgencia`, `consulta_resuelta` (Booleano) y `mes_consulta`.

*   **`derivado`**:
    *   **Tabla de Frecuencias y Visualización**: Se contabilizó el número y porcentaje de consultas derivadas. Un gráfico de barras muestra claramente esta proporción.

        `![Distribución de Consultas Derivadas](assets/univariate_plots/barchart_derivado.png)`
        *Interpretación del gráfico `derivado`: Este gráfico de barras muestra la proporción de consultas que fueron derivadas a un asesor versus las que no, dando una idea de la carga de trabajo que escala a intervención humana.*

*   **`tipo_consulta`**:
    *   **Tabla de Frecuencias y Visualización**: Se identificaron los tipos de consulta más frecuentes. Un gráfico de barras ordenado por frecuencia revela las categorías dominantes.

        `![Distribución de Tipos de Consulta](assets/univariate_plots/barchart_tipo_consulta.png)`
        *Interpretación del gráfico `tipo_consulta`: Visualiza la frecuencia de cada tipo de consulta, ayudando a entender las principales necesidades de los estudiantes.*
    *   **Valores Faltantes**: Se verificó si algunas consultas no tenían un tipo asignado.

*   **`urgencia`**:
    *   **Tabla de Frecuencias y Visualización**: Se analizaron las proporciones de consultas clasificadas por urgencia. Un gráfico de barras muestra esta distribución.

        `![Distribución de Urgencia de Consulta](assets/univariate_plots/barchart_urgencia.png)`
        *Interpretación del gráfico `urgencia`: Presenta la distribución de los niveles de urgencia ("Alta", "Media", "Baja") asignados a las consultas.*

*   **`consulta_resuelta`**:
    *   **Tabla de Frecuencias y Visualización**: Se calculó el porcentaje de consultas resueltas. Un gráfico de barras ilustra la tasa de resolución.

        `![Distribución de Consultas Resueltas](assets/univariate_plots/barchart_consulta_resuelta.png)`
        *Interpretación del gráfico `consulta_resuelta`: Muestra la proporción de consultas marcadas como resueltas versus no resueltas, un indicador clave de efectividad.*

*   **`mes_consulta`**:
    *   **Distribución**: Un gráfico de barras muestra el volumen de consultas por mes, permitiendo identificar posibles patrones de estacionalidad.

        `![Distribución de Consultas por Mes](assets/univariate_plots/barchart_mes_consulta.png)`
        *Interpretación del gráfico `mes_consulta`: Ilustra el número de consultas registradas en cada mes, ayudando a detectar tendencias temporales o picos de actividad.*

**3. Variables de Identificación y Fecha**

*   **`id_estudiante` y `id_asesor`**: Para estas variables, el análisis se centró en verificar la unicidad (para `id_estudiante` si cada registro es una consulta única por estudiante o si un estudiante puede tener múltiples consultas), la consistencia del formato y la presencia de valores faltantes. También se podría obtener un conteo de consultas por estudiante o por asesor.
*   **`fecha_consulta`**: Esta variable se utilizó para derivar `mes_consulta`. Análisis más profundos podrían incluir la extracción del día de la semana o la hora para identificar patrones temporales más finos, aunque esto se consideraría para ingeniería de características.

**Conclusión del Análisis Univariado**

El análisis univariado proporcionó una comprensión detallada de cada variable en el dataset. Se identificaron las distribuciones típicas, rangos de valores, y la presencia de outliers y datos faltantes para cada campo. Estos hallazgos son esenciales para guiar las decisiones de limpieza de datos, transformación de variables y para la selección de técnicas apropiadas en el análisis bivariado y la construcción del modelo predictivo. Por ejemplo, la asimetría en variables de tiempo podría requerir transformaciones (como logarítmica) antes del modelado. La gestión de outliers y valores faltantes se abordará en la etapa de preprocesamiento.

### Análisis Bivariado

En esta fase del análisis exploratorio, se investigaron las relaciones entre pares de variables, con un enfoque particular en cómo las variables predictoras se relacionan con la variable objetivo: `satisfaccion_estudiante`. Para las variables numéricas, se calcularon los coeficientes de correlación de Pearson y se generaron visualizaciones para facilitar la interpretación.

**Correlación de Pearson con `satisfaccion_estudiante`**

El análisis de correlación reveló las siguientes relaciones lineales entre las variables numéricas y la satisfacción del estudiante:

*   **`indice_promotor_neto` vs. `satisfaccion_estudiante`**: Se observó una correlación positiva fuerte (aproximadamente +0.87). Esto indica que a medida que el Índice Promotor Neto (NPS) aumenta, la satisfacción del estudiante tiende a incrementar de manera significativa. Un NPS alto es un fuerte predictor de alta satisfacción.
*   **`puntaje_esfuerzo_cliente` vs. `satisfaccion_estudiante`**: Se encontró una correlación negativa fuerte (aproximadamente -0.70). Este resultado sugiere que cuanto mayor es el esfuerzo que el estudiante percibe que debe realizar para resolver su consulta (CES alto), menor tiende a ser su satisfacción. Facilitar la resolución de consultas es crucial.
*   **`tiempo_consulta` vs. `satisfaccion_estudiante`**: Existe una correlación negativa considerable (aproximadamente -0.56). Tiempos de consulta más prolongados están asociados con una menor satisfacción del estudiante. Esto podría indicar que consultas largas son percibidas como ineficientes o problemáticas.
*   **`calidad_del_servicio` vs. `satisfaccion_estudiante`**: Se identificó una correlación positiva moderada (aproximadamente +0.40). Calificaciones más altas en la calidad del servicio se asocian con una mayor satisfacción estudiantil, como es de esperar.
*   **`tiempo_espera` vs. `satisfaccion_estudiante`**: Se manifestó una correlación negativa moderada (aproximadamente -0.40). Tiempos de espera más largos antes o durante la consulta tienden a disminuir la satisfacción del estudiante.

**Interpretación de Visualizaciones**

Las visualizaciones generadas por el script `src/analisis/bivariate_plots.py` y almacenadas en `assets/bivariate_plots/` apoyan estas observaciones:

*   **Gráfico de Barras de Correlaciones con `satisfaccion_estudiante`**: Este gráfico presenta de manera clara la magnitud y dirección de las correlaciones de las variables numéricas con `satisfaccion_estudiante`. Permite una comparación visual rápida de qué factores tienen un impacto lineal más fuerte. El `indice_promotor_neto` y el `puntaje_esfuerzo_cliente` destacan como las variables con las correlaciones más pronunciadas.

    `![Gráfico de Barras de Correlaciones con Satisfacción del Estudiante](assets/bivariate_plots/correlation_with_satisfaccion_estudiante_barchart.png)`
    *Interpretación del gráfico: Este diagrama de barras visualiza los coeficientes de correlación de Pearson entre cada variable numérica y la `satisfaccion_estudiante`. Las barras más altas (positivas o negativas) indican una relación lineal más fuerte. Ayuda a identificar rápidamente los predictores lineales más significativos de la satisfacción.*

*   **Mapa de Calor (Heatmap) de la Matriz de Correlaciones**: El heatmap visualiza la matriz de correlaciones entre todas las variables numéricas del conjunto de datos. Además de confirmar las relaciones con `satisfaccion_estudiante`, este mapa permite identificar posibles relaciones de multicolinealidad entre las variables predictoras. Por ejemplo, se puede observar la correlación entre `tiempo_consulta` y `puntaje_esfuerzo_cliente`.

    `![Mapa de Calor de la Matriz de Correlaciones](assets/bivariate_plots/correlation_matrix_heatmap.png)`
    *Interpretación del gráfico: El mapa de calor muestra la fuerza y dirección de la correlación entre todos los pares de variables numéricas. Los colores más intensos indican correlaciones más fuertes (positivas o negativas). Es útil para entender la estructura de interrelaciones en los datos y detectar multicolinealidad.*

Estas relaciones bivariadas proporcionan información valiosa para la formulación de hipótesis y la posterior etapa de ingeniería de características y selección de variables para el modelo de predicción de la satisfacción estudiantil.

### Formulación de hipótesis sobre la data

Basándose en los análisis previos (detallados en `docs/Analisis_Inicial.md` y los hallazgos del EDA en las secciones anteriores de este documento) y siguiendo un formato estructurado para la formulación y prueba de hipótesis, se presentan las siguientes:

| Pregunta | Hipótesis nula (H₀) | Hipótesis alternativa (H₁) | Tipo de prueba |
| :---- | :---- | :---- | :---- |
| ¿Un tiempo de espera prolongado se correlaciona negativamente con la satisfacción del estudiante? | H₀: El `tiempo_espera` no se correlaciona negativamente con la `satisfaccion_estudiante` (coeficiente de correlación ≥ 0). | H₁: Un `tiempo_espera` prolongado se correlaciona negativamente con la `satisfaccion_estudiante` (coeficiente de correlación < 0). | Test de correlación (Pearson), Regresión lineal |
| ¿Un tiempo de consulta extenso se correlaciona negativamente con la satisfacción del estudiante? | H₀: El `tiempo_consulta` no se correlaciona negativamente con la `satisfaccion_estudiante` (coeficiente de correlación ≥ 0). | H₁: Un `tiempo_consulta` extenso se correlaciona negativamente con la `satisfaccion_estudiante` (coeficiente de correlación < 0). | Test de correlación (Pearson), Regresión lineal |
| ¿La interacción de `urgencia` 'Alta' y `tiempo_espera` elevado impacta más negativamente la satisfacción del estudiante que otras urgencias con tiempos similares? | H₀: El impacto negativo de la interacción `urgencia` 'Alta' y `tiempo_espera` elevado sobre la `satisfaccion_estudiante` no es significativamente mayor que para urgencias 'Media' o 'Baja' con tiempos de espera similares. | H₁: La interacción entre `urgencia` 'Alta' y un `tiempo_espera` elevado tendrá un impacto negativo significativamente mayor en la `satisfaccion_estudiante` en comparación con urgencias 'Media' o 'Baja' con tiempos de espera similares. | Regresión lineal con término de interacción, ANOVA |
| ¿Una alta `calidad_del_servicio` (calificación) se correlaciona positivamente con una alta `satisfaccion_estudiante`? | H₀: La `calidad_del_servicio` no se correlaciona positivamente con la `satisfaccion_estudiante` (coeficiente de correlación ≤ 0). | H₁: Una alta `calidad_del_servicio` se correlaciona positivamente con una alta `satisfaccion_estudiante` (coeficiente de correlación > 0). | Test de correlación (Pearson), Regresión lineal |
| ¿Las consultas resueltas (`consulta_resuelta` = True) tienen, en promedio, una satisfacción del estudiante significativamente mayor que las no resueltas? | H₀: La `satisfaccion_estudiante` promedio es igual o menor para las consultas marcadas como `consulta_resuelta` (True) en comparación con las no resueltas. | H₁: Las consultas marcadas como `consulta_resuelta` (True) tendrán, en promedio, una `satisfaccion_estudiante` significativamente mayor que aquellas no resueltas. | t-test para muestras independientes |
| ¿La característica `calidad_resolucion` es un predictor más fuerte de la `satisfaccion_estudiante` que `calidad_del_servicio` o `consulta_resuelta` individualmente? | H₀: La capacidad predictiva de `calidad_resolucion` sobre `satisfaccion_estudiante` no es mayor que la de `calidad_del_servicio` o `consulta_resuelta` por separado (evaluado por ej. con R²). | H₁: La característica combinada `calidad_resolucion` será un predictor más fuerte de la `satisfaccion_estudiante` que `calidad_del_servicio` o `consulta_resuelta` individualmente. | Comparación de modelos de regresión (ej. R², AIC, BIC) |
| ¿El `puntaje_esfuerzo_cliente` (donde un puntaje alto indica mayor esfuerzo) se correlaciona negativamente con la `satisfaccion_estudiante`? | H₀: El `puntaje_esfuerzo_cliente` no se correlaciona negativamente con la `satisfaccion_estudiante` (coeficiente de correlación ≥ 0). | H₁: El `puntaje_esfuerzo_cliente` se correlaciona negativamente con la `satisfaccion_estudiante` (coeficiente de correlación < 0). | Test de correlación (Pearson), Regresión lineal |
| ¿Un `indice_promotor_neto` alto se correlaciona positivamente con una alta `satisfaccion_estudiante`? | H₀: El `indice_promotor_neto` no se correlaciona positivamente con la `satisfaccion_estudiante` (coeficiente de correlación ≤ 0). | H₁: Un `indice_promotor_neto` alto se correlaciona positivamente con una alta `satisfaccion_estudiante` (coeficiente de correlación > 0). | Test de correlación (Pearson), Regresión lineal |
| ¿La característica `satisfaccion_general` tiene una varianza menor que `satisfaccion_estudiante`? | H₀: La varianza de `satisfaccion_general` es igual o mayor que la varianza de `satisfaccion_estudiante`. | H₁: La característica `satisfaccion_general` tendrá una varianza menor que `satisfaccion_estudiante`. | Test de comparación de varianzas (ej. F-test, Levene's test) |
| ¿El `tipo_consulta` 'Queja' se asocia con niveles promedio de `satisfaccion_estudiante` más bajos, especialmente si la `calidad_del_servicio` también es baja? | H₀: El `tipo_consulta` 'Queja' no se asocia con niveles promedio de `satisfaccion_estudiante` más bajos, ni esta relación se intensifica con una baja `calidad_del_servicio`. | H₁: El `tipo_consulta` 'Queja' se asociará con niveles de `satisfaccion_estudiante` promedio más bajos en comparación con otros tipos de consulta, y este efecto se intensifica si la `calidad_del_servicio` también es baja. | ANOVA, Regresión lineal con término de interacción |
| ¿Existen variaciones significativas en la `satisfaccion_estudiante` promedio según el `mes_consulta` o `trimestre`? | H₀: No hay variaciones significativas en la `satisfaccion_estudiante` promedio según el `mes_consulta` o `trimestre` (las medias son iguales). | H₁: Habrá variaciones significativas en la `satisfaccion_estudiante` promedio según el `mes_consulta` o `trimestre`. | ANOVA |
| ¿Hay diferencias en el `tiempo_espera` promedio o en la `satisfaccion_estudiante` promedio entre consultas de fin de semana (`es_fin_semana` = True) y días de semana? | H₀: No hay diferencias significativas en el `tiempo_espera` promedio ni en la `satisfaccion_estudiante` promedio entre consultas realizadas durante `es_fin_semana` y días de semana. | H₁: Las consultas realizadas durante `es_fin_semana` (True) mostrarán diferencias significativas en el `tiempo_espera` promedio o en la `satisfaccion_estudiante` promedio comparadas con las realizadas en días de semana. | t-test para muestras independientes (para cada variable) |
| ¿La característica `eficiencia_servicio` se correlaciona positivamente con la `satisfaccion_estudiante` y con el `indice_promotor_neto`? | H₀: La `eficiencia_servicio` no se correlaciona positivamente con la `satisfaccion_estudiante` y/o con el `indice_promotor_neto` (coeficiente de correlación ≤ 0 para al menos uno). | H₁: La característica `eficiencia_servicio` mostrará una correlación positiva con la `satisfaccion_estudiante` y con el `indice_promotor_neto` (coeficientes de correlación > 0 para ambos). | Test de correlación (Pearson), Regresión lineal (para cada relación) |

Estas hipótesis, ahora en formato tabular, pueden ser directamente referenciadas y probadas en análisis estadísticos subsecuentes para validar las relaciones propuestas y guiar la construcción del modelo predictivo.

### Aplicación de Ingeniería de Características

La ingeniería de características es un paso crucial para mejorar el rendimiento de los modelos de Machine Learning al crear nuevas variables (features) a partir de las existentes, que pueden capturar mejor las relaciones subyacentes en los datos y proporcionar información más útil al modelo. Basado en el análisis del notebook `notebooks/04_feature_engineering.ipynb`, se aplicaron las siguientes transformaciones y creaciones de características:

1.  **Creación de Características Temporales:**
    *   Se extrajo el año (`año_consulta`) y el mes numérico (`mes_consulta_num`) de `fecha_consulta`.
    *   Se derivó el día de la semana (`dia_semana`, ej. Lunes, Martes).
    *   Se calculó el trimestre del año (`trimestre`).
    *   Se creó una variable booleana `es_fin_de_semana`.

2.  **Creación de Características de Tiempo de Servicio:**
    *   `tiempo_total_atencion`: Suma de `tiempo_consulta` y `tiempo_espera`.
    *   `ratio_tiempo_espera_consulta`: Cociente entre `tiempo_espera` y `tiempo_consulta` (manejando división por cero).
    *   `categoria_tiempo_espera`: Variable categórica basada en umbrales de `tiempo_espera` (ej. "Corto", "Medio", "Largo").

3.  **Creación de Características de Calidad y Satisfacción Compuestas:**
    *   `calidad_resolucion`: Combinación de `calidad_del_servicio` y `consulta_resuelta` (ej. alta calidad y resuelta).
    *   `satisfaccion_general`: Podría ser una combinación ponderada o un promedio de `satisfaccion_estudiante` y `indice_promotor_neto`.
    *   `eficiencia_servicio`: Podría relacionar `consulta_resuelta` con `tiempo_total_atencion`.

4.  **Codificación de Variables Categóricas:**
    *   **One-Hot Encoding:** Aplicado a `tipo_consulta` y al `mes_consulta` textual para convertirlas en representaciones numéricas sin imponer un orden.
    *   **Ordinal Encoding:** Aplicado a `urgencia` (Baja, Media, Alta) para reflejar su orden inherente.

5.  **Creación de Características de Interacción:**
    *   `urgencia_tiempo_espera`: Interacción entre el nivel de `urgencia` y el `tiempo_espera`.
    *   `calidad_tiempo_consulta`: Interacción entre `calidad_del_servicio` y `tiempo_consulta`.
    *   `derivado_tiempo_total`: Interacción entre `derivado` y `tiempo_total_atencion`.

6.  **Normalización de Características:**
    *   Se aplicó `MinMaxScaler` a las variables numéricas (`tiempo_consulta`, `tiempo_espera`, `calidad_del_servicio`, `satisfaccion_estudiante`, `indice_promotor_neto`, `puntaje_esfuerzo_cliente`, y las nuevas características numéricas creadas) para escalarlas a un rango común (generalmente 0 a 1). Esto es importante para algoritmos sensibles a la magnitud de las características.

7.  **Guardado del Dataset Modificado:**
    *   El dataset resultante, con todas las características nuevas y transformadas, se guardó en `data/chatbot_satisfaction_dataset_engineered.csv`.

Estas transformaciones enriquecen el conjunto de datos original, proporcionando una representación más matizada y potencialmente más predictiva de los factores que influyen en la satisfacción del estudiante, preparando el terreno para un modelado más efectivo.

### Elaboración del reporte

El presente Análisis Exploratorio de Datos (AED) ha sentado las bases fundamentales para la preparación de un dataset robusto y bien comprendido, destinado al entrenamiento de un modelo de inteligencia artificial para predecir la satisfacción estudiantil con un servicio de chatbot. A continuación, se consolidan los hallazgos clave de cada etapa del análisis:

1.  **Definición y Comprensión del Dataset (`Diccionario de Datos`):**
    Se estableció un diccionario de datos claro, detallando cada una de las 14 variables originales, incluyendo `id_estudiante`, `fecha_consulta`, `mes_consulta`, `derivado`, `tipo_consulta`, `urgencia`, `tiempo_consulta`, `tiempo_espera`, `id_asesor`, `calidad_del_servicio`, `consulta_resuelta`, `satisfaccion_estudiante` (variable objetivo), `indice_promotor_neto` (NPS) y `puntaje_esfuerzo_cliente` (CES). Se identificaron tipos de datos y se formularon recomendaciones para mejorar la calidad y consistencia de los datos, como la normalización de variables categóricas y la estandarización de unidades de tiempo.

2.  **Análisis Univariado:**
    El examen individual de cada variable reveló sus características intrínsecas:
    *   **Variables Numéricas:** Se analizaron las distribuciones, tendencias centrales (media, mediana), dispersión (desviación estándar, rango) y la presencia de outliers para `tiempo_consulta`, `tiempo_espera`, `calidad_del_servicio`, `satisfaccion_estudiante`, `indice_promotor_neto` y `puntaje_esfuerzo_cliente`. Se observaron asimetrías en las variables de tiempo, lo que sugiere la necesidad de posibles transformaciones. Se generaron histogramas y diagramas de caja para visualizar estas distribuciones (referenciados en `assets/univariate_plots/`).
    *   **Variables Categóricas:** Se estudiaron las frecuencias de `derivado`, `tipo_consulta`, `urgencia`, `consulta_resuelta` y `mes_consulta` mediante tablas y gráficos de barras (referenciados en `assets/univariate_plots/`), identificando las categorías predominantes y la distribución de consultas a lo largo de los meses.
    La identificación de valores faltantes y outliers en esta etapa es crucial para las tareas de limpieza y preprocesamiento.

3.  **Análisis Bivariado:**
    Se investigaron las relaciones entre pares de variables, con un enfoque especial en la variable objetivo `satisfaccion_estudiante`:
    *   **Correlaciones Significativas:** El análisis de correlación de Pearson destacó fuertes relaciones lineales: una correlación positiva fuerte entre `indice_promotor_neto` y `satisfaccion_estudiante` (+0.87), y una correlación negativa fuerte entre `puntaje_esfuerzo_cliente` y `satisfaccion_estudiante` (-0.70). También se encontraron correlaciones negativas considerables para `tiempo_consulta` (-0.56) y `tiempo_espera` (-0.40), y una correlación positiva moderada para `calidad_del_servicio` (+0.40) con la satisfacción.
    *   **Visualizaciones:** El gráfico de barras de correlaciones con `satisfaccion_estudiante` y el mapa de calor de la matriz de correlaciones (disponibles en `assets/bivariate_plots/`) proporcionaron una comprensión visual de estas interacciones y ayudaron a identificar posibles problemas de multicolinealidad.

4.  **Formulación de Hipótesis:**
    Se formularon hipótesis específicas sobre las relaciones entre variables, como el impacto negativo de los tiempos de espera y consulta prolongados en la satisfacción, la influencia positiva de la calidad del servicio y la resolución de consultas, y la correlación del NPS y CES con la satisfacción. Estas hipótesis, presentadas en formato de tabla, guiarán análisis más profundos y la validación estadística.

5.  **Ingeniería de Características:**
    Se aplicaron diversas técnicas para generar nuevas características predictivas a partir de las existentes. Este proceso incluyó:
    *   **Características Temporales:** Extracción de `año_consulta`, `dia_semana`, `trimestre` y `es_fin_de_semana`.
    *   **Características de Tiempo de Servicio:** Creación de `tiempo_total_atencion`, `ratio_tiempo_espera_consulta` y `categoria_tiempo_espera`.
    *   **Características de Calidad y Satisfacción Compuestas:** Generación de `calidad_resolucion`, `satisfaccion_general` y `eficiencia_servicio`.
    *   **Codificación de Variables Categóricas:** Aplicación de One-Hot Encoding (para `tipo_consulta`, `mes_consulta` textual) y Ordinal Encoding (para `urgencia`).
    *   **Características de Interacción:** Creación de `urgencia_tiempo_espera`, `calidad_tiempo_consulta` y `derivado_tiempo_total`.
    *   **Normalización:** Aplicación de MinMaxScaler a un conjunto de variables numéricas.
    El dataset resultante con estas nuevas características (`chatbot_satisfaction_dataset_engineered.csv`) está mejor preparado para el modelado, ya que captura relaciones más complejas y presenta la información en un formato más adecuado para los algoritmos de aprendizaje automático.

**Conclusión General del Reporte:**

El proceso de AED ha sido exhaustivo, comenzando con la comprensión básica del dataset y progresando hacia la identificación de patrones, relaciones clave y la creación de nuevas características informativas. Los hallazgos indican que factores como el esfuerzo del cliente (CES), la probabilidad de recomendación (NPS), los tiempos de espera y consulta, y la calidad percibida del servicio son determinantes importantes de la satisfacción del estudiante.

La ingeniería de características ha enriquecido el dataset, proporcionando variables que potencialmente mejorarán la capacidad predictiva del modelo de IA. Las hipótesis formuladas ofrecen una hoja de ruta para investigaciones futuras y para la interpretación de los resultados del modelo.

En conjunto, este AED no solo ha preparado los datos para el modelado, sino que también ha proporcionado insights valiosos sobre la dinámica de la satisfacción estudiantil en el contexto del uso de un chatbot. El siguiente paso será utilizar el dataset ingenierizado para entrenar y evaluar diversos modelos de machine learning con el objetivo de predecir con precisión la satisfacción del estudiante y, en última instancia, mejorar el servicio ofrecido.