from setuptools import setup, find_packages

setup(
    name="actividad_3",
    version="0.0.1",
    author="leonel Moscoso Yovany Patino",
    author_email="",
    description="",
    py_modules=["actividad_2", "actividad_3"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests", # Páquete separado
        "matplotlib",  # Páquete separado
        "numpy",  # Páquete separado
        "seaborn",
        "kagglehub[pandas-datasets]>=0.3.8",  # Páquete separado
        
    ]
) 
