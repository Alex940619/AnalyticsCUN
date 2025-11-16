"""
Script de Análisis Exploratorio de Datos (EDA)
Equipo B - Análisis previo al clustering
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analisis_exploratorio():
    """Realiza análisis exploratorio básico"""
    print("="*80)
    print("ANÁLISIS EXPLORATORIO DE DATOS")
    print("="*80)
    
    # Cargar datos limpios
    print("\nCargando datos limpios...")
    df = pd.read_csv('datos_limpios.csv')
    
    print(f"\n INFORMACIÓN GENERAL")
    print(f"Total de registros: {len(df):,}")
    print(f"Total de columnas: {len(df.columns)}")
    print(f"Período: {df['Año Registro'].min()} - {df['Año Registro'].max()}")
    
    # Análisis por país
    print(f"\n ANÁLISIS POR PAÍS")
    print(f"Total de países: {df['País'].nunique()}")
    print(f"\nTop 10 países:")
    top_paises = df['País'].value_counts().head(10)
    for i, (pais, count) in enumerate(top_paises.items(), 1):
        porcentaje = (count / len(df)) * 100
        print(f"  {i}. {pais}: {count:,} ({porcentaje:.1f}%)")
    
    # Análisis demográfico
    print(f"\n ANÁLISIS DEMOGRÁFICO")
    print(f"\nDistribución por género:")
    genero = df['Género'].value_counts()
    for gen, count in genero.items():
        porcentaje = (count / len(df)) * 100
        print(f"  {gen}: {count:,} ({porcentaje:.1f}%)")
    
    print(f"\nEstadísticas de edad:")
    print(f"  Edad promedio: {df['Edad (años)'].mean():.1f} años")
    print(f"  Edad mediana: {df['Edad (años)'].median():.1f} años")
    print(f"  Rango: {df['Edad (años)'].min():.0f} - {df['Edad (años)'].max():.0f} años")
    
    # Análisis educativo
    print(f"\n ANÁLISIS EDUCATIVO")
    print(f"Top 5 niveles académicos:")
    nivel = df['Nivel Académico'].value_counts().head(5)
    for niv, count in nivel.items():
        porcentaje = (count / len(df)) * 100
        print(f"  {niv}: {count:,} ({porcentaje:.1f}%)")
    
    # Análisis temporal
    print(f"\n ANÁLISIS TEMPORAL")
    print(f"Registros por año:")
    años = df['Año Registro'].value_counts().sort_index()
    for año, count in años.items():
        print(f"  {año}: {count:,}")
    
    # Calidad de datos
    print(f"\n CALIDAD DE DATOS")
    print(f"Valores nulos por columna:")
    nulos = df.isnull().sum()
    nulos_pct = (nulos / len(df)) * 100
    for col in nulos[nulos > 0].index:
        print(f"  {col}: {nulos[col]:,} ({nulos_pct[col]:.1f}%)")
    
    print("\n" + "="*80)
    print("✓ Análisis exploratorio completado")
    print("="*80)

if __name__ == "__main__":
    analisis_exploratorio()
