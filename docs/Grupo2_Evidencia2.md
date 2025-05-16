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

(Presentación y discusión del análisis univariado realizado para cada variable relevante del dataset. Incluir distribuciones, medidas de tendencia central, dispersión, identificación de outliers y valores faltantes.)

### Análisis Bivariado

(Presentación y discusión del análisis bivariado para explorar relaciones entre pares de variables, especialmente con la variable objetivo `satisfaccion_estudiante`. Incluir correlaciones, tablas de contingencia, y visualizaciones comparativas.)

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