# Reporte de Ingeniería de Características

## Introducción

Este reporte detalla el proceso de ingeniería de características aplicado al dataset de satisfacción de un chatbot estudiantil, tal como se implementó en el notebook `notebooks/04_feature_engineering.ipynb`. El objetivo de esta fase es transformar y enriquecer el dataset original para mejorar el rendimiento de futuros modelos de aprendizaje automático.

## Pasos Realizados

### 1. Configuración Inicial y Carga de Datos

*   **Librerías Importadas:**
    *   `pandas`: Para la manipulación de datos.
    *   `numpy`: Para operaciones numéricas.
    *   `seaborn` y `matplotlib.pyplot`: Para la creación de visualizaciones.
    *   `datetime` (de `datetime`): Para el manejo de fechas.
    *   `MinMaxScaler` (de `sklearn.preprocessing`): Para la normalización de datos.
*   **Estilo de Gráficas:** Se configuró un estilo por defecto para las visualizaciones (`plt.style.use('default')`, `sns.set_theme()`).
*   **Carga del Dataset:** Se cargó el archivo `../data/chatbot_satisfaction_dataset_utf8.csv` en un DataFrame de pandas.

### 2. Ingeniería de Características Temporales

Se procesó la columna `fecha_consulta` para extraer información temporal relevante:

*   **Conversión a Datetime:** La columna `fecha_consulta` se convirtió al formato datetime de pandas.
*   **Nuevas Características Creadas:**
    *   `año_consulta`: Año de la consulta.
    *   `mes_consulta`: Mes de la consulta (numérico, 1-12).
    *   `dia_semana`: Día de la semana (0 para lunes, 6 para domingo).
    *   `trimestre`: Trimestre del año (1-4).
    *   `es_fin_semana`: Variable binaria (1 si es sábado o domingo, 0 en caso contrario).

### 3. Ingeniería de Características de Tiempo de Servicio

Se crearon nuevas variables para analizar los tiempos asociados al servicio:

*   `tiempo_total_atencion`: Suma de `tiempo_consulta` y `tiempo_espera`.
*   `ratio_tiempo_espera_consulta`: Cociente entre `tiempo_espera` y `tiempo_consulta`.
*   `categoria_tiempo_espera`: Variable categórica creada a partir de `tiempo_espera` usando `pd.qcut` para dividir los tiempos en cuatro cuartiles (etiquetas: 'Muy Bajo', 'Bajo', 'Alto', 'Muy Alto').

### 4. Ingeniería de Características de Calidad y Satisfacción

Se generaron métricas combinadas para evaluar la calidad y la satisfacción:

*   `calidad_resolucion`: Producto de `calidad_del_servicio` y la versión numérica de `consulta_resuelta`.
*   `satisfaccion_general`: Promedio de `satisfaccion_estudiante` e `indice_promotor_neto`.
*   `eficiencia_servicio`: Cociente entre la versión numérica de `consulta_resuelta` y (`tiempo_total_atencion` + 1) (se suma 1 para evitar división por cero).

### 5. Codificación de Variables Categóricas

Se transformaron variables categóricas a formato numérico:

*   **`tipo_consulta`:** Se aplicó codificación one-hot, creando nuevas columnas para cada tipo de consulta (ej. `tipo_consulta_Solicitud de documentos`).
*   **`urgencia`:** Se aplicó codificación ordinal, mapeando 'Baja' a 1, 'Media' a 2, y 'Alta' a 3 en una nueva columna `urgencia_encoded`.
*   **`mes_consulta` (original, en formato texto):** Se aplicó codificación one-hot, creando nuevas columnas para cada mes (ej. `mes_septiembre`).

### 6. Creación de Características de Interacción

Se generaron características de interacción para capturar posibles relaciones no lineales:

*   `urgencia_tiempo_espera`: Producto de `urgencia_encoded` y `tiempo_espera`.
*   `calidad_tiempo_consulta`: Producto de `calidad_del_servicio` y `tiempo_consulta`.
*   `derivado_tiempo_total`: Producto de la versión numérica de `derivado` y `tiempo_total_atencion`.

### 7. Normalización de Variables Numéricas

Se normalizaron varias características numéricas para escalarlas al rango [0, 1] usando `MinMaxScaler`. Esto ayuda a que los algoritmos de aprendizaje automático no se vean sesgados por variables con rangos de valores muy diferentes. Las variables normalizadas fueron:
*   `tiempo_consulta`
*   `tiempo_espera`
*   `tiempo_total_atencion`
*   `ratio_tiempo_espera_consulta`
*   `eficiencia_servicio`

### 8. Guardado del Dataset Procesado

Finalmente, el DataFrame con todas las características nuevas y transformadas se guardó en un nuevo archivo CSV: `../data/chatbot_satisfaction_dataset_engineered.csv`.

## Conclusión

El proceso de ingeniería de características ha enriquecido el dataset original con nuevas variables derivadas de la información temporal, tiempos de servicio, métricas de calidad y satisfacción, interacciones entre variables y codificaciones numéricas de datos categóricos. Estas nuevas características están diseñadas para proporcionar una representación más completa y útil de los datos para el entrenamiento de modelos predictivos. 