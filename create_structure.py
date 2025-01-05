
import os

# Definisci la struttura delle directory
structure = {
    "01_basics": [
        "01_variables_and_data_types",
        "02_input_output",
        "03_operators",
        "04_comments"
    ],
    "02_control_structures": [
        "01_if_else",
        "02_loops",
        "03_nested_structures"
    ],
    "03_functions": [
        "01_function_basics",
        "02_arguments_and_return",
        "03_lambda_functions",
        "04_recursion"
    ],
    "04_data_structures": [
        "01_lists",
        "02_tuples",
        "03_dictionaries",
        "04_sets"
    ],
    "05_object_oriented_programming": [
        "01_classes_and_objects",
        "02_inheritance",
        "03_polymorphism",
        "04_encapsulation"
    ],
    "06_modules_and_packages": [
        "01_creating_modules",
        "02_importing_modules",
        "03_python_packages"
    ],
    "07_exceptions_and_error_handling": [
        "01_try_except",
        "02_custom_exceptions",
        "03_debugging"
    ],
    "08_file_handling": [
        "01_reading_files",
        "02_writing_files",
        "03_json_handling",
        "04_csv_handling"
    ],
    "09_standard_libraries": [
        "01_os_module",
        "02_sys_module",
        "03_math_module",
        "04_datetime_module",
        "05_random_module"
    ],
    "10_advanced_topics": [
        "01_decorators",
        "02_generators",
        "03_context_managers",
        "04_metaclasses"
    ],
    "11_testing": [
        "01_unit_testing",
        "02_pytest",
        "03_mocking"
    ],
    "12_projects": [
        "01_mini_projects",
        "02_real_world_projects"
    ],
    "13_data_analysis_and_visualization": [
        "01_numpy_basics",
        "02_pandas_basics",
        "03_matplotlib_basics",
        "04_seaborn_basics"
    ]
}


# Funzione per creare la struttura
def create_structure(base_path, structure):
    for main_folder, subfolders in structure.items():
        main_folder_path = os.path.join(base_path, main_folder)
        os.makedirs(main_folder_path, exist_ok=True)  # Crea la cartella principale
        for subfolder in subfolders:
            subfolder_path = os.path.join(main_folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)  # Crea la sottocartella

            # Crea la cartella "exercises" nella sottocartella
            exercises_path = os.path.join(subfolder_path, "exercises")
            os.makedirs(exercises_path, exist_ok=True)

            # Crea un file Python con il nome della sottocartella
            python_file_path = os.path.join(subfolder_path, f"{subfolder}.py")
            with open(python_file_path, "w") as python_file:
                python_file.write(f"# File per {subfolder}\n")
                python_file.write("# Aggiungi il tuo codice qui\n")


# Percorso base del progetto
base_path = "/Users/alessiopinna/Documents/workspaces/python/python_fundamentals/foundamental"  # Sostituisci con il percorso del tuo progetto PyCharm

# Creazione della struttura
create_structure(base_path, structure)

print("Struttura creata con successo con file Python!")

