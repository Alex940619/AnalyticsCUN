"""
Script para ejecutar todo el pipeline de análisis
"""

import subprocess
import sys

def ejecutar_script(nombre_script):
    """Ejecuta un script Python y muestra su salida"""
    print(f"\n{'='*80}")
    print(f"Ejecutando: {nombre_script}")
    print(f"{'='*80}\n")
    
    try:
        resultado = subprocess.run([sys.executable, nombre_script], 
                                  capture_output=False, 
                                  text=True, 
                                  check=True)
        print(f"\n✓ {nombre_script} completado exitosamente\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error ejecutando {nombre_script}")
        print(f"Código de error: {e.returncode}\n")
        return False

if __name__ == "__main__":
    print("="*80)
    print("PIPELINE COMPLETO DE ANÁLISIS - CLUSTERING K-MEANS")
    print("Equipo B - Análisis de Migración Colombiana")
    print("="*80)
    
    scripts = [
        "01_etl_limpieza.py",
        "02_clustering_kmeans.py",
        "03_dashboard_visualizacion.py"
    ]
    
    for script in scripts:
        if not ejecutar_script(script):
            print(f"\nPipeline detenido debido a error en {script}")
            sys.exit(1)
    
    print("\n" + "="*80)
    print("✓ PIPELINE COMPLETADO EXITOSAMENTE")
    print("="*80)
    print("\nArchivos generados:")
    print("  - datos_limpios.csv")
    print("  - datos_agregados_pais.csv")
    print("  - resultados_clustering.csv")
    print("  - 01_seleccion_k_optimo.png")
    print("  - 02_visualizacion_clusters.png")
    print("  - 03_heatmap_clusters.png")
    print("  - 04_dashboard_completo.png")
    print("  - 05_dashboard_interactivo.html")
    print("  - 06_mapa_clusters_interactivo.html")
    print("  - 07_reporte_clusters.txt")
    print("\n¡Abre los archivos .html en tu navegador para ver dashboards interactivos!")
