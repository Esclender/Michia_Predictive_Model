# Diccionario de Datos para Modelo de Chatbot Estudiantil

Este documento presenta la estructura base del dataset a utilizar para entrenar un modelo de ML para un chatbot estudiantil, considerando que la variable objetivo es la satisfacción del estudiante.

## Variables del Dataset

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

## Recomendaciones y Mejoras a la Estructura

1. **Separación de Fecha y Hora:**  
   Aunque se cuenta con la variable "fecha_consulta", se recomienda registrar también la hora (por ejemplo, "hora_consulta") para análisis más granulares, especialmente en periodos de alta demanda o picos de interacción.

2. **Consolidación Temporal:**  
   Se plantea mantener tanto "fecha_consulta" como "mes_consulta" por simplicidad analítica. No obstante, al registrar la fecha completa se puede derivar el mes durante el análisis, evitando redundancias.

3. **Normalización de Variables:**  
   - Es fundamental que las variables categóricas (como "tipo_consulta" y "urgencia") cuenten con un conjunto definido de valores para evitar inconsistencias.  
   - Los campos de tiempo ("tiempo_consulta" y "tiempo_espera") deben estar expresados en la misma unidad (por ejemplo, segundos) para facilitar la comparación y el análisis.

4. **Validación de Datos:**  
   - Los campos booleanos ("derivado" y "consulta_resuelta") deben controlar posibles valores nulos o inconsistentes.  
   - Es recomendable implementar restricciones o validaciones en la entrada de datos para los identificadores ("id_estudiante", "id_asesor") y así mantener la integridad referencial.

Esta estructura, con nombres de variables estandarizados en español, facilita el entendimiento y manejo de los datos tanto para análisis exploratorios como para el entrenamiento del modelo de ML.