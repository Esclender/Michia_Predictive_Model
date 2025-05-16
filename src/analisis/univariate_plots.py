import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Configuration ---

# Get the absolute path to the project root directory
# __file__ is the path to the current script (src/analisis/univariate_plots.py)
# os.path.dirname(__file__) is src/analisis
# os.path.join(os.path.dirname(__file__), '..', '..') goes up two levels to the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Construct the absolute path to the data file
DATA_FILE_NAME = 'dataset_correlacion_satisfaccion.csv'
DATA_FILE_PATH = os.path.join(PROJECT_ROOT, 'data', DATA_FILE_NAME)

# Directory to save plots
# PLOTS_OUTPUT_DIR will be PROJECT_ROOT/assets/univariate_plots/
PLOTS_OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'assets', 'univariate_plots')

# Columns for univariate analysis (based on Grupo2_Evidencia2.md)
NUMERICAL_COLUMNS = [
    'tiempo_consulta', 
    'tiempo_espera', 
    'calidad_del_servicio', 
    'satisfaccion_estudiante', 
    'indice_promotor_neto', 
    'puntaje_esfuerzo_cliente'
]

CATEGORICAL_COLUMNS = [
    'derivado', 
    'tipo_consulta', 
    'urgencia', 
    'consulta_resuelta',
    'mes_consulta' # Treating mes_consulta as categorical for count plot
]

# --- Helper Functions ---

def load_data(file_path):
    """Loads data from a CSV file."""
    print(f"Attempting to load data from: {file_path}") # Added print statement
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        print("Please update DATA_FILE_PATH in the script.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def create_output_directory(path):
    """Creates the output directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def save_plot(fig, file_name):
    """Saves the given figure to the specified file name in the PLOTS_OUTPUT_DIR."""
    full_path = os.path.join(PLOTS_OUTPUT_DIR, file_name)
    try:
        fig.savefig(full_path)
        print(f"Saved plot: {full_path}")
    except Exception as e:
        print(f"Error saving plot {full_path}: {e}")
    plt.close(fig) # Close the figure to free memory

# --- Plotting Functions ---

def plot_histogram(df, column):
    """Generates and saves a histogram for a numerical column."""
    if column not in df.columns:
        print(f"Warning: Column '{column}' not found in DataFrame for histogram.")
        return

    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histograma de {column}', fontsize=15)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.grid(axis='y', alpha=0.75)
    save_plot(plt.gcf(), f'histogram_{column}.png')

def plot_boxplot(df, column):
    """Generates and saves a boxplot for a numerical column."""
    if column not in df.columns:
        print(f"Warning: Column '{column}' not found in DataFrame for boxplot.")
        return
        
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=df[column])
    plt.title(f'Diagrama de Caja de {column}', fontsize=15)
    plt.ylabel(column, fontsize=12)
    plt.grid(axis='y', alpha=0.75)
    save_plot(plt.gcf(), f'boxplot_{column}.png')

def plot_barplot_categorical(df, column):
    """Generates and saves a bar plot for a categorical column."""
    if column not in df.columns:
        print(f"Warning: Column '{column}' not found in DataFrame for barplot.")
        return

    plt.figure(figsize=(12, 7) if df[column].nunique() > 5 else (8,5))
    sns.countplot(data=df, x=column, order = df[column].value_counts().index)
    plt.title(f'Distribución de {column}', fontsize=15)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Conteo', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout() # Adjust layout to prevent labels from overlapping
    plt.grid(axis='y', alpha=0.75)
    save_plot(plt.gcf(), f'barchart_{column}.png')

# --- Main Execution ---

if __name__ == "__main__":
    print("Starting univariate plot generation...")
    
    # Create the output directory for plots
    create_output_directory(PLOTS_OUTPUT_DIR)
    
    # Load the data
    data_df = load_data(DATA_FILE_PATH)
    
    if data_df is not None:
        # Generate plots for numerical columns
        print("\n--- Generating plots for numerical variables ---")
        for col in NUMERICAL_COLUMNS:
            if col in data_df.columns:
                plot_histogram(data_df, col)
                plot_boxplot(data_df, col)
            else:
                print(f"Skipping numerical column '{col}': not found in dataset.")
        
        # Generate plots for categorical columns
        print("\n--- Generating plots for categorical variables ---")
        for col in CATEGORICAL_COLUMNS:
            if col in data_df.columns:
                plot_barplot_categorical(data_df, col)
            else:
                print(f"Skipping categorical column '{col}': not found in dataset.")
                
        print("\nUnivariate plot generation complete.")
        print(f"Plots saved in: {os.path.abspath(PLOTS_OUTPUT_DIR)}")
    else:
        print("Halting script due to data loading issues.") 