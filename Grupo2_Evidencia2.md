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

(Basado en los análisis previos, formular hipótesis específicas sobre las relaciones entre las variables y su impacto en la satisfacción del estudiante. Por ejemplo: "Se hipotetiza que un mayor `tiempo_espera` se correlaciona negativamente con `satisfaccion_estudiante`".)

### Aplicación de Ingeniería de Características

(Descripción de las técnicas de ingeniería de características que se podrían aplicar para mejorar la calidad del dataset y la predictibilidad del modelo. Por ejemplo: creación de nuevas variables a partir de las existentes, transformación de variables, etc.)

### Elaboración del reporte

(Esta sección consolida los hallazgos de los análisis anteriores, presentando una visión integral de la calidad y relevancia de los datos. Se discutirán los patrones identificados, las relaciones clave y cómo estos insights informarán las siguientes etapas del desarrollo del modelo de IA.)

## Conclusión

(Resumen de los principales hallazgos del Análisis Exploratorio de Datos. Reiterar la importancia de este proceso para la construcción de un modelo de chatbot estudiantil efectivo. Mencionar los próximos pasos, como el preprocesamiento final y el entrenamiento del modelo.)

## Referencias

(Listado de todas las fuentes citadas en el ensayo, en formato APA 7. Incluir referencias a las librerías si se considera apropiado, o a metodologías de AED consultadas.) 