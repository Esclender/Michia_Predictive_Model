# Bivariate Analysis Report: Chatbot Student Satisfaction

**Date:** [Insert Date Here]

## 1. Introduction

This report summarizes the findings of the bivariate analysis conducted on the chatbot student satisfaction dataset. The primary objective of this analysis was to explore the relationships between various features and the target variable, `satisfaccion_estudiante`, as well as the relationships among the features themselves. Understanding these relationships is crucial for feature selection and model building in predicting student satisfaction.

## 2. Data and Setup

- **Data Source:** The analysis utilized the `chatbot_satisfaction_dataset_utf8.csv` dataset.
- **Key Variables Examined (Numeric for Correlation):** 
    - `tiempo_consulta` (Consultation Time)
    - `tiempo_espera` (Waiting Time)
    - `calidad_del_servicio` (Service Quality Rating)
    - `indice_promotor_neto` (Net Promoter Score - NPS)
    - `puntaje_esfuerzo_cliente` (Customer Effort Score - CES)
- **Target Variable:** `satisfaccion_estudiante` (Student Satisfaction Score)
- **Libraries Used:** Python libraries including `pandas` for data manipulation, `numpy` for numerical operations, `seaborn` and `matplotlib.pyplot` for visualization, and `scipy.stats` for statistical functions.

## 3. Methodology

The primary method for bivariate analysis in this phase was the calculation of Pearson correlation coefficients between numeric features and the target variable (`satisfaccion_estudiante`). A correlation matrix heatmap was also generated to visualize linear relationships among all numeric variables.

## 4. Key Findings

### 4.1. Correlation with Student Satisfaction (`satisfaccion_estudiante`)

The Pearson correlation analysis revealed **very weak linear relationships** between the examined numeric features and the student satisfaction score. The calculated correlation coefficients are as follows:

- **Puntaje Esfuerzo Cliente (CES) vs. Satisfacción del Estudiante:** `0.002890`
- **Índice Promotor Neto (NPS) vs. Satisfacción del Estudiante:** `0.000974`
- **Tiempo Espera vs. Satisfacción del Estudiante:** `-0.001505`
- **Calidad del Servicio vs. Satisfacción del Estudiante:** `-0.005397`
- **Tiempo Consulta vs. Satisfacción del Estudiante:** `-0.006359`

**Interpretation:**

- All correlation values are very close to zero, indicating that there is no significant linear trend (either positive or negative) between these specific numeric predictors and student satisfaction.
- For instance, a longer `tiempo_consulta` (consultation time) or `tiempo_espera` (waiting time) does not show a clear linear tendency to increase or decrease student satisfaction based on this metric. Similarly, higher or lower `calidad_del_servicio`, `indice_promotor_neto`, or `puntaje_esfuerzo_cliente` do not linearly predict student satisfaction.

### 4.2. Visualization

- A **bar chart** was used to visually represent the weak correlations between the numeric features and `satisfaccion_estudiante`. This further emphasized the lack of strong linear associations.
- A **heatmap of the correlation matrix** was generated for all numeric variables. While the detailed interpretation of inter-feature correlations (excluding the target variable) isn't the focus here, this visualization helps in identifying potential multicollinearity if strong correlations were observed between predictor variables.

## 5. Discussion and Implications

The results of the Pearson correlation analysis suggest that the selected numeric features, when considered in a linear fashion, are not strong individual predictors of student satisfaction.

**Possible Reasons for Weak Linear Correlations:**

- **Non-Linear Relationships:** The relationship between these features and student satisfaction might be non-linear (e.g., U-shaped, exponential). Pearson correlation only captures linear trends.
- **Importance of Categorical Variables:** Categorical features not included in this specific correlation analysis (e.g., `tipo_consulta`, `urgencia`, `derivado`, `consulta_resuelta`) might have a more significant impact on satisfaction.
- **Interaction Effects:** The effect of one variable on satisfaction might depend on the level of another variable (interaction effects), which are not captured by simple bivariate correlations.
- **Data Quality or Range:** The range or distribution of the data for these numeric features might limit the observable correlation.
- **Complexity of Satisfaction:** Student satisfaction is likely a multifaceted construct influenced by a complex interplay of various factors, not just a few numeric indicators in isolation.

## 6. Recommendations and Next Steps

Based on these findings, the following steps are recommended:

- **Explore Non-Linear Relationships:** Utilize visualization techniques like scatter plots (with an added LOESS curve, for example) or statistical tests designed for non-linear associations.
- **Analyze Categorical Variables:** Conduct bivariate analysis between categorical features and `satisfaccion_estudiante`. Techniques like chi-squared tests, or comparing mean satisfaction scores across different categories (e.g., using box plots or ANOVA if satisfaction is treated as continuous-like for this purpose) would be appropriate.
- **Feature Engineering:** Consider creating new features from existing ones (e.g., ratios, interaction terms, binning numeric features) that might reveal stronger relationships.
- **Advanced Modeling Techniques:** Employ machine learning models that can capture non-linear relationships and interactions (e.g., decision trees, random forests, gradient boosting machines) rather than relying solely on linear models if prediction is the goal.
- **Qualitative Insights:** Supplement quantitative analysis with qualitative data (e.g., student feedback, comments) to gain a deeper understanding of what drives satisfaction.

## 7. Conclusion

The bivariate analysis using Pearson correlation indicates that `tiempo_consulta`, `tiempo_espera`, `calidad_del_servicio`, `indice_promotor_neto`, and `puntaje_esfuerzo_cliente` do not exhibit strong linear relationships with `satisfaccion_estudiante` in this dataset. Further investigation into non-linear relationships and the impact of categorical variables is essential for a comprehensive understanding of the drivers of student satisfaction. 