import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Configuration ---
# Get the absolute path to the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Construct the absolute path to the data file
DATA_FILE_NAME = 'dataset_correlacion_satisfaccion.csv' # Same as univariate
DATA_FILE_PATH = os.path.join(PROJECT_ROOT, 'data', DATA_FILE_NAME)

# Directory to save plots
PLOTS_OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'assets', 'bivariate_plots')

TARGET_VARIABLE = 'satisfaccion_estudiante'

# Columns for bivariate analysis (primarily numerical for correlation)
# We'll select these dynamically, but you can predefine if needed
# NUMERICAL_COLUMNS = [
# 'tiempo_consulta',
# 'tiempo_espera',
# 'calidad_del_servicio',
# 'satisfaccion_estudiante',
# 'indice_promotor_neto',
# 'puntaje_esfuerzo_cliente'
# ]

# --- Helper Functions (similar to univariate_plots.py) ---

def load_data(file_path):
    """Loads data from a CSV file."""
    print(f"Attempting to load data from: {file_path}")
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        print("Please ensure DATA_FILE_NAME and its location in the /data directory are correct.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def create_output_directory(path):
    """Creates the output directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def save_plot(fig_or_plt, file_name, is_figure_object=True):
    """Saves the given figure or current plt state to the specified file name."""
    full_path = os.path.join(PLOTS_OUTPUT_DIR, file_name)
    try:
        if is_figure_object:
            fig_or_plt.savefig(full_path)
        else: # Assuming it's plt that needs saving
            fig_or_plt.savefig(full_path)
        print(f"Saved plot: {full_path}")
    except Exception as e:
        print(f"Error saving plot {full_path}: {e}")
    if is_figure_object:
        plt.close(fig_or_plt) # Close the figure object to free memory
    else:
        plt.close() # Close the current plt figure

# --- Plotting Functions ---

def plot_correlation_with_target(df, numerical_cols, target_col):
    """Generates and saves a bar chart of correlations with the target variable."""
    if target_col not in df.columns:
        print(f"Error: Target column '{target_col}' not found in DataFrame.")
        return
    if not pd.api.types.is_numeric_dtype(df[target_col]):
        print(f"Error: Target column '{target_col}' must be numeric for correlation.")
        return

    correlations = df[numerical_cols].corr()[target_col].sort_values(ascending=False)
    # Drop the correlation of the target with itself
    correlations_filtered = correlations.drop(target_col, errors='ignore') 

    if correlations_filtered.empty:
        print("No numerical columns found to correlate with the target, or only target itself.")
        return

    plt.figure(figsize=(10, 7))
    sns.barplot(x=correlations_filtered.index, y=correlations_filtered.values, palette="coolwarm")
    plt.title(f'Correlación de Pearson con {target_col}', fontsize=16)
    plt.xlabel('Variables Numéricas', fontsize=12)
    plt.ylabel('Coeficiente de Correlación', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    save_plot(plt.gcf(), f'correlation_with_{target_col}_barchart.png')

def plot_correlation_heatmap(df, numerical_cols):
    """Generates and saves a heatmap of the correlation matrix for numerical columns."""
    if not numerical_cols:
        print("No numerical columns provided for heatmap.")
        return
        
    correlation_matrix = df[numerical_cols].corr()
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Mapa de Calor de la Matriz de Correlaciones Numéricas', fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    save_plot(plt.gcf(), 'correlation_matrix_heatmap.png')

# --- Main Execution ---

if __name__ == "__main__":
    print("Starting bivariate plot generation...")
    
    create_output_directory(PLOTS_OUTPUT_DIR)
    data_df = load_data(DATA_FILE_PATH)
    
    if data_df is not None:
        # Dynamically select numerical columns, excluding any known ID columns if necessary
        # For now, select_dtypes will get all numbers. Adjust if ID columns are numeric.
        numerical_cols_for_analysis = data_df.select_dtypes(include=np.number).columns.tolist()
        
        if not numerical_cols_for_analysis:
            print("No numerical columns found in the dataset.")
        else:
            print(f"\nNumerical columns identified for analysis: {numerical_cols_for_analysis}")

            # Plot 1: Correlation with target variable
            print("\n--- Generating bar chart of correlations with target variable ---")
            if TARGET_VARIABLE in numerical_cols_for_analysis:
                plot_correlation_with_target(data_df, numerical_cols_for_analysis, TARGET_VARIABLE)
            else:
                print(f"Target variable '{TARGET_VARIABLE}' not found in numerical columns or dataset.")

            # Plot 2: Correlation heatmap for all numerical variables
            print("\n--- Generating correlation heatmap for numerical variables ---")
            # Ensure there's more than one numerical column for a meaningful heatmap
            if len(numerical_cols_for_analysis) > 1:
                plot_correlation_heatmap(data_df, numerical_cols_for_analysis)
            else:
                print("Not enough numerical columns to generate a meaningful correlation heatmap.")
                
        print("\nBivariate plot generation complete.")
        print(f"Plots saved in: {os.path.abspath(PLOTS_OUTPUT_DIR)}")
    else:
        print("Halting script due to data loading issues.") 