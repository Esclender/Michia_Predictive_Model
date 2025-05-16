import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Configuración de visualización
plt.style.use('default')
sns.set_theme()
plt.rcParams['figure.figsize'] = (12, 8)

# Carga de datos
df = pd.read_csv('data/chatbot_satisfaction_dataset_utf8.csv')

# Selección de variables numéricas
numeric_columns = df.select_dtypes(include=[np.number]).columns

# Cálculo de correlaciones con la variable objetivo
correlations = df[numeric_columns].corr()['satisfaccion_estudiante'].sort_values(ascending=False)
correlations = correlations.drop('satisfaccion_estudiante')

# Visualización de correlaciones
plt.figure(figsize=(12, 6))
correlations.plot(kind='bar')
plt.title('Correlaciones con Satisfacción del Estudiante')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('correlaciones_satisfaccion.png')
plt.close()

# Matriz de correlaciones
plt.figure(figsize=(12, 10))
sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlaciones')
plt.tight_layout()
plt.savefig('matriz_correlaciones.png')
plt.close()

# Análisis de significancia y formulación de hipótesis
n = len(df)
print("\nHipótesis de Correlación:\n")

for var, corr in correlations.items():
    p_value = stats.pearsonr(df[var], df['satisfaccion_estudiante'])[1]
    significance = "significativa" if p_value < 0.05 else "no significativa"
    direction = "positiva" if corr > 0 else "negativa"
    
    print(f"Variable: {var}")
    print(f"Correlación: {corr:.3f} ({direction})")
    print(f"Significancia: {significance} (p-value: {p_value:.4f})")
    print(f"Hipótesis: Existe una correlación {direction} {significance} entre {var} y la satisfacción del estudiante.")
    print("-" * 80)

# Visualización de relaciones bivariadas para las 5 variables más correlacionadas
top_correlations = correlations.head(5).index
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.ravel()

for idx, var in enumerate(top_correlations):
    sns.regplot(data=df, x=var, y='satisfaccion_estudiante', ax=axes[idx])
    axes[idx].set_title(f'{var} vs Satisfacción')

plt.tight_layout()
plt.savefig('relaciones_bivariadas.png')
plt.close() 