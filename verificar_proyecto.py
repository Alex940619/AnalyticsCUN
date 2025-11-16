"""
Script de Verificación del Proyecto
Verifica que todos los archivos necesarios existen
"""

import os
import sys

def verificar_archivos():
    """Verifica que todos los archivos necesarios existen"""
    
    archivos_requeridos = {
        "Código": [
            "00_analisis_exploratorio.py",
            "01_etl_limpieza.py",
            "02_clustering_kmeans.py",
            "03_dashboard_visualizacion.py",
            "ejecutar_todo.py",
            "requirements.txt"
        ],
        "Datos": [
            "datos_limpios.csv",
            "datos_agregados_pais.csv",
            "resultados_clustering.csv"
        ],
        "Visualizaciones PNG": [
            "01_seleccion_k_optimo.png",
            "02_visualizacion_clusters.png",
            "03_heatmap_clusters.png",
            "04_dashboard_completo.png"
        ],
        "Visualizaciones HTML": [
            "05_dashboard_interactivo.html",
            "06_mapa_clusters_interactivo.html"
        ],
        "Documentación": [
            "README.md",
            "INFORME_CLUSTERING.md",
            "PRESENTACION_RESULTADOS.md",
            "RESUMEN_EJECUTIVO.txt",
            "TIPS_PRESENTACION.md",
            "CHECKLIST_ENTREGA.md",
            "07_reporte_clusters.txt"
        ]
    }
    
    print("="*80)
    print("VERIFICACIÓN DEL PROYECTO - CLUSTERING K-MEANS")
    print("Equipo B")
    print("="*80)
    print()
    
    total_archivos = 0
    archivos_encontrados = 0
    archivos_faltantes = []
    
    for categoria, archivos in archivos_requeridos.items():
        print(f"\n📁 {categoria}:")
        for archivo in archivos:
            total_archivos += 1
            if os.path.exists(archivo):
                print(f"  ✅ {archivo}")
                archivos_encontrados += 1
            else:
                print(f"  ❌ {archivo} - FALTANTE")
                archivos_faltantes.append(archivo)
    
    print("\n" + "="*80)
    print(f"RESUMEN: {archivos_encontrados}/{total_archivos} archivos encontrados")
    print("="*80)
    
    if archivos_faltantes:
        print("\n⚠️  ARCHIVOS FALTANTES:")
        for archivo in archivos_faltantes:
            print(f"  - {archivo}")
        print("\n💡 Ejecuta 'python ejecutar_todo.py' para generar archivos faltantes")
        return False
    else:
        print("\n✅ ¡PROYECTO COMPLETO!")
        print("\n📊 Archivos listos para entregar:")
        print(f"  - {len(archivos_requeridos['Código'])} scripts de Python")
        print(f"  - {len(archivos_requeridos['Datos'])} archivos de datos CSV")
        print(f"  - {len(archivos_requeridos['Visualizaciones PNG'])} visualizaciones PNG")
        print(f"  - {len(archivos_requeridos['Visualizaciones HTML'])} dashboards interactivos")
        print(f"  - {len(archivos_requeridos['Documentación'])} documentos")
        print("\n🎉 ¡Listo para presentar y entregar!")
        return True

def verificar_datos():
    """Verifica estadísticas básicas de los datos"""
    try:
        import pandas as pd
        
        print("\n" + "="*80)
        print("VERIFICACIÓN DE DATOS")
        print("="*80)
        
        # Verificar datos limpios
        if os.path.exists('datos_limpios.csv'):
            df = pd.read_csv('datos_limpios.csv')
            print(f"\n✅ datos_limpios.csv:")
            print(f"  - Registros: {len(df):,}")
            print(f"  - Columnas: {len(df.columns)}")
        
        # Verificar datos agregados
        if os.path.exists('datos_agregados_pais.csv'):
            df_agg = pd.read_csv('datos_agregados_pais.csv')
            print(f"\n✅ datos_agregados_pais.csv:")
            print(f"  - Países: {len(df_agg)}")
            print(f"  - Columnas: {len(df_agg.columns)}")
        
        # Verificar resultados clustering
        if os.path.exists('resultados_clustering.csv'):
            df_clust = pd.read_csv('resultados_clustering.csv')
            print(f"\n✅ resultados_clustering.csv:")
            print(f"  - Países: {len(df_clust)}")
            print(f"  - Clusters: {df_clust['Cluster'].nunique()}")
            print(f"  - Distribución:")
            for cluster in sorted(df_clust['Cluster'].unique()):
                count = len(df_clust[df_clust['Cluster'] == cluster])
                print(f"    Cluster {cluster}: {count} países")
        
        return True
    except Exception as e:
        print(f"\n⚠️  Error al verificar datos: {e}")
        return False

if __name__ == "__main__":
    print()
    archivos_ok = verificar_archivos()
    
    if archivos_ok:
        datos_ok = verificar_datos()
        
        if datos_ok:
            print("\n" + "="*80)
            print("✅ VERIFICACIÓN COMPLETA - TODO OK")
            print("="*80)
            print("\n📋 Próximos pasos:")
            print("  1. Revisar CHECKLIST_ENTREGA.md")
            print("  2. Leer TIPS_PRESENTACION.md")
            print("  3. Abrir archivos HTML en navegador")
            print("  4. Preparar presentación")
            print("\n🚀 ¡Éxito en tu proyecto!")
            sys.exit(0)
        else:
            sys.exit(1)
    else:
        sys.exit(1)
