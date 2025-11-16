"""
Script de ETL y Limpieza de Datos
Equipo B - Clustering K-Means
"""

import pandas as pd
import numpy as np

def cargar_datos(ruta_archivo):
    """Carga el archivo Excel"""
    print("Cargando datos...")
    df = pd.read_excel(ruta_archivo)
    print(f"Datos cargados: {len(df)} registros, {len(df.columns)} columnas")
    return df

def limpiar_datos(df):
    """Limpia y prepara los datos"""
    print("\nLimpiando datos...")
    
    # Crear copia para no modificar original
    df_clean = df.copy()
    
    # Eliminar duplicados
    df_clean = df_clean.drop_duplicates()
    print(f"Duplicados eliminados: {len(df) - len(df_clean)}")
    
    # Limpiar valores nulos en columnas clave
    print(f"Valores nulos por columna:\n{df_clean.isnull().sum()}")
    
    # Convertir edad a numérico
    df_clean['Edad (años)'] = pd.to_numeric(df_clean['Edad (años)'], errors='coerce')
    
    # Convertir estatura a numérico
    df_clean['Estatura (CM)'] = pd.to_numeric(df_clean['Estatura (CM)'], errors='coerce')
    df_clean['Estatura (CM)'] = df_clean['Estatura (CM)'].replace(0, np.nan)
    
    # Convertir fecha de registro
    df_clean['Fecha de Registro'] = pd.to_datetime(df_clean['Fecha de Registro'], format='%d/%m/%Y', errors='coerce')
    
    # Extraer año de registro
    df_clean['Año Registro'] = df_clean['Fecha de Registro'].dt.year
    
    print(f"\nDatos limpios: {len(df_clean)} registros")
    return df_clean

def agregar_por_pais(df):
    """Agrega datos por país para clustering"""
    print("\nAgregando datos por país...")
    
    # Calcular métricas por país
    agg_pais = df.groupby('País').agg({
        'Cantidad de personas': 'sum',
        'Género': lambda x: (x == 'FEMENINO').sum() / len(x) * 100,  # % mujeres
        'Edad (años)': ['mean', lambda x: ((x >= 18) & (x <= 35)).sum() / len(x) * 100],  # edad promedio y % 18-35
        'Nivel Académico': lambda x: (x.isin(['PREGRADO - UNIVERSITARIO', 'POSGRADO - ESPECIALIZACIÓN', 
                                               'POSGRADO - MAESTRÍA', 'POSGRADO - DOCTORADO'])).sum() / len(x) * 100,  # % educación superior
        'Estado civil': lambda x: (x == 'SOLTERO').sum() / len(x) * 100,  # % solteros
        'Código ISO país': 'first'
    }).reset_index()
    
    # Renombrar columnas
    agg_pais.columns = ['Pais', 'Total_Personas', 'Porcentaje_Mujeres', 'Edad_Promedio', 
                        'Porcentaje_18_35', 'Porcentaje_Educacion_Superior', 
                        'Porcentaje_Solteros', 'Codigo_ISO']
    
    # Filtrar países con al menos 100 registros para análisis más robusto
    agg_pais = agg_pais[agg_pais['Total_Personas'] >= 100].reset_index(drop=True)
    
    print(f"Países para clustering: {len(agg_pais)}")
    print(f"\nPrimeros registros:\n{agg_pais.head()}")
    
    return agg_pais

def guardar_datos(df, df_agregado, ruta_limpio='datos_limpios.csv', ruta_agregado='datos_agregados_pais.csv'):
    """Guarda los datos procesados"""
    print("\nGuardando datos...")
    df.to_csv(ruta_limpio, index=False, encoding='utf-8-sig')
    df_agregado.to_csv(ruta_agregado, index=False, encoding='utf-8-sig')
    print(f"Datos guardados en:\n- {ruta_limpio}\n- {ruta_agregado}")

if __name__ == "__main__":
    # Ejecutar ETL
    ruta_excel = "02_dataset_limpio_equipoB (1).xlsx"
    
    # Cargar y limpiar
    df_original = cargar_datos(ruta_excel)
    df_limpio = limpiar_datos(df_original)
    
    # Agregar por país
    df_pais = agregar_por_pais(df_limpio)
    
    # Guardar
    guardar_datos(df_limpio, df_pais)
    
    print("\n✓ ETL completado exitosamente")
