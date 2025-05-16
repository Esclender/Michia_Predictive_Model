# Formulación de Hipótesis Basada en el Análisis Inicial y EDA

## Introducción

Este documento presenta una serie de hipótesis formuladas a partir del `Analisis_Inicial.md` y enriquecidas con los hallazgos del Análisis Exploratorio de Datos (EDA) detallado en `Grupo2_Evidencia2.md`. Las hipótesis se centran en las relaciones entre diversas variables y su impacto potencial en la `satisfaccion_estudiante`.

## Hipótesis Generadas

Basándose en las "Relaciones Lógicas Potenciales" identificadas en `Analisis_Inicial.md` y los resultados de los análisis univariado y bivariado documentados en `Grupo2_Evidencia2.md`, se plantean las siguientes hipótesis:

1.  **Hipótesis sobre Tiempos y Satisfacción:**
    *   **H1.1:** Un `tiempo_espera` prolongado se correlaciona negativamente con la `satisfaccion_estudiante`.
        *   *Justificación:* `Analisis_Inicial.md` sugiere esta relación. El análisis bivariado en `Grupo2_Evidencia2.md` confirmó una correlación negativa moderada (aprox. -0.40) entre `tiempo_espera` y `satisfaccion_estudiante`.
    *   **H1.2:** Un `tiempo_consulta` extenso se correlaciona negativamente con la `satisfaccion_estudiante`.
        *   *Justificación:* `Analisis_Inicial.md` lo considera un indicador de eficiencia. El análisis bivariado en `Grupo2_Evidencia2.md` mostró una correlación negativa considerable (aprox. -0.56).
    *   **H1.3:** La interacción entre `urgencia` 'Alta' y un `tiempo_espera` elevado tendrá un impacto negativo significativamente mayor en la `satisfaccion_estudiante` en comparación con urgencias 'Media' o 'Baja' con tiempos de espera similares.
        *   *Justificación:* Sugerido en `Analisis_Inicial.md`. Esta hipótesis busca profundizar en la interacción entre estas dos variables, utilizando la característica de interacción `urgencia_tiempo_espera` creada en la fase de ingeniería de características (mencionada en `Grupo2_Evidencia2.md`).

2.  **Hipótesis sobre Calidad, Resolución y Satisfacción:**
    *   **H2.1:** Una alta `calidad_del_servicio` (calificación) se correlaciona positivamente con una alta `satisfaccion_estudiante`.
        *   *Justificación:* Lógica común y sugerida en `Analisis_Inicial.md`. El análisis bivariado en `Grupo2_Evidencia2.md` encontró una correlación positiva moderada (aprox. +0.40).
    *   **H2.2:** Las consultas marcadas como `consulta_resuelta` (True) tendrán, en promedio, una `satisfaccion_estudiante` significativamente mayor que aquellas no resueltas.
        *   *Justificación:* Indicado como crucial en `Analisis_Inicial.md`. El análisis univariado de `consulta_resuelta` y `satisfaccion_estudiante` (en `Grupo2_Evidencia2.md`) puede ofrecer una base, y un análisis bivariado comparando la satisfacción promedio entre los dos grupos de `consulta_resuelta` lo confirmaría.
    *   **H2.3:** La característica combinada `calidad_resolucion` (producto de `calidad_del_servicio` y `consulta_resuelta`) será un predictor más fuerte de la `satisfaccion_estudiante` que `calidad_del_servicio` o `consulta_resuelta` individualmente.
        *   *Justificación:* Esta hipótesis se basa en la idea de que tanto la calidad percibida como la resolución efectiva son necesarias para la satisfacción. La variable `calidad_resolucion` fue creada durante la ingeniería de características (descrita en `Grupo2_Evidencia2.md`).

3.  **Hipótesis sobre Esfuerzo, Promoción y Satisfacción:**
    *   **H3.1:** Un `puntaje_esfuerzo_cliente` bajo se correlaciona positivamente con una alta `satisfaccion_estudiante`.
        *   *Justificación:* `Analisis_Inicial.md` sugiere esta relación. El análisis bivariado en `Grupo2_Evidencia2.md` confirmó una fuerte correlación negativa (aprox. -0.70) entre `puntaje_esfuerzo_cliente` y `satisfaccion_estudiante` (lo que implica que bajo esfuerzo se asocia con alta satisfacción).
    *   **H3.2:** Un `indice_promotor_neto` alto se correlaciona positivamente con una alta `satisfaccion_estudiante`.
        *   *Justificación:* `Analisis_Inicial.md` lo considera un reflejo de la satisfacción general. El análisis bivariado en `Grupo2_Evidencia2.md` mostró una fuerte correlación positiva (aprox. +0.87).
    *   **H3.3:** La característica `satisfaccion_general` (promedio de `satisfaccion_estudiante` e `indice_promotor_neto`) tendrá una varianza menor y podría ser una métrica de satisfacción más estable que `satisfaccion_estudiante` sola para ciertos análisis predictivos.
        *   *Justificación:* Esta es una hipótesis exploratoria basada en la creación de `satisfaccion_general` durante la ingeniería de características (descrita en `Grupo2_Evidencia2.md`), con la idea de suavizar posibles variaciones extremas en una sola métrica.

4.  **Hipótesis sobre Tipo de Consulta y Satisfacción:**
    *   **H4.1:** El `tipo_consulta` 'Queja' se asociará con niveles de `satisfaccion_estudiante` promedio más bajos en comparación con otros tipos de consulta, especialmente si la `calidad_del_servicio` también es baja.
        *   *Justificación:* Sugerido en `Analisis_Inicial.md`. Se puede investigar comparando la `satisfaccion_estudiante` promedio entre diferentes `tipo_consulta` y analizando la interacción con `calidad_del_servicio`.

5.  **Hipótesis sobre Características Temporales y Satisfacción:**
    *   **H5.1:** Habrá variaciones significativas en la `satisfaccion_estudiante` promedio según el `mes_consulta` o `trimestre`, reflejando posibles impactos de ciclos académicos o carga de trabajo institucional.
        *   *Justificación:* `Analisis_Inicial.md` menciona el análisis de tendencias temporales. La ingeniería de características (`Grupo2_Evidencia2.md`) creó `año_consulta`, `mes_consulta`, `dia_semana`, `trimestre`, que pueden ser usadas para probar esta hipótesis.
    *   **H5.2:** Las consultas realizadas durante `es_fin_semana` (True) podrían mostrar diferencias en `tiempo_espera` o `satisfaccion_estudiante` comparadas con las realizadas en días de semana, debido a variaciones en la disponibilidad de personal o tipos de consulta predominantes.
        *   *Justificación:* Hipótesis exploratoria basada en la creación de la característica `es_fin_semana` (descrita en `Grupo2_Evidencia2.md`).

6.  **Hipótesis sobre la Eficiencia del Servicio:**
    *   **H6.1:** La característica `eficiencia_servicio` (calculada durante la ingeniería de características) mostrará una correlación positiva con la `satisfaccion_estudiante` y el `indice_promotor_neto`.
        *   *Justificación:* Se espera que un servicio más eficiente (consulta resuelta en menor tiempo total) conduzca a mayor satisfacción y lealtad. Esta característica fue creada en la fase de ingeniería de características (mencionada en `Grupo2_Evidencia2.md`).

## Próximos Pasos

Estas hipótesis servirán como guía para análisis más profundos y para la selección de características en el desarrollo del modelo predictivo de satisfacción estudiantil. Cada hipótesis puede ser probada utilizando técnicas estadísticas apropiadas y análisis de datos adicionales sobre el dataset enriquecido. 