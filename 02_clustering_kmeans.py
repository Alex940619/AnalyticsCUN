"""
Script de Clustering K-Means
Equipo B - Análisis de Migración Colombiana
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_datos_agregados(ruta='datos_agregados_pais.csv'):
    """Carga los datos agregados por país"""
    print("Cargando datos agregados...")
    df = pd.read_csv(ruta)
    print(f"Países cargados: {len(df)}")
    return df

def seleccionar_variables(df):
    """Selecciona y prepara variables para clustering"""
    print("\nSeleccionando variables para clustering...")
    
    # Variables para clustering
    variables = ['Porcentaje_Mujeres', 'Porcentaje_18_35', 'Total_Personas']
    
    X = df[variables].copy()
    
    print(f"Variables seleccionadas: {variables}")
    print(f"\nEstadísticas descriptivas:\n{X.describe()}")
    
    return X, variables

def normalizar_datos(X):
    """Normaliza las variables usando StandardScaler"""
    print("\nNormalizando datos...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, scaler

def encontrar_k_optimo(X_scaled, max_k=10):
    """Encuentra el número óptimo de clusters usando método del codo y silhouette"""
    print("\nBuscando número óptimo de clusters...")
    
    inertias = []
    silhouette_scores = []
    K_range = range(2, min(max_k + 1, len(X_scaled)))
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))
    
    # Visualizar
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Método del codo
    ax1.plot(K_range, inertias, 'bo-')
    ax1.set_xlabel('Número de Clusters (k)')
    ax1.set_ylabel('Inercia')
    ax1.set_title('Método del Codo')
    ax1.grid(True)
    
    # Silhouette score
    ax2.plot(K_range, silhouette_scores, 'ro-')
    ax2.set_xlabel('Número de Clusters (k)')
    ax2.set_ylabel('Silhouette Score')
    ax2.set_title('Silhouette Score por k')
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('01_seleccion_k_optimo.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado: 01_seleccion_k_optimo.png")
    
    # Recomendar k
    k_optimo = K_range[np.argmax(silhouette_scores)]
    print(f"\nk recomendado (mayor silhouette): {k_optimo}")
    print(f"Silhouette scores: {dict(zip(K_range, [f'{s:.3f}' for s in silhouette_scores]))}")
    
    return k_optimo, silhouette_scores

def aplicar_kmeans(X_scaled, n_clusters=3):
    """Aplica K-Means con el número de clusters especificado"""
    print(f"\nAplicando K-Means con {n_clusters} clusters...")
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    
    # Calcular métricas
    silhouette_avg = silhouette_score(X_scaled, labels)
    silhouette_vals = silhouette_samples(X_scaled, labels)
    
    print(f"Silhouette Score: {silhouette_avg:.4f}")
    
    return kmeans, labels, silhouette_avg, silhouette_vals

def analizar_clusters(df, labels, variables):
    """Analiza las características de cada cluster"""
    print("\nAnalizando clusters...")
    
    df_resultado = df.copy()
    df_resultado['Cluster'] = labels
    
    # Estadísticas por cluster
    print("\nCaracterísticas promedio por cluster:")
    cluster_stats = df_resultado.groupby('Cluster')[variables + ['Pais']].agg({
        'Porcentaje_Mujeres': 'mean',
        'Porcentaje_18_35': 'mean',
        'Total_Personas': ['mean', 'sum'],
        'Pais': 'count'
    })
    print(cluster_stats)
    
    # Países por cluster
    print("\nPaíses por cluster:")
    for cluster in sorted(df_resultado['Cluster'].unique()):
        paises = df_resultado[df_resultado['Cluster'] == cluster]['Pais'].tolist()
        print(f"\nCluster {cluster} ({len(paises)} países):")
        print(", ".join(paises[:10]) + ("..." if len(paises) > 10 else ""))
    
    return df_resultado

def visualizar_clusters(df_resultado, X_scaled, labels, silhouette_vals, variables):
    """Crea visualizaciones de los clusters"""
    print("\nGenerando visualizaciones...")
    
    # 1. Scatter plot 2D (primeras 2 variables)
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))
    
    # Scatter: % Mujeres vs % 18-35
    ax1 = axes[0, 0]
    scatter = ax1.scatter(df_resultado['Porcentaje_Mujeres'], 
                         df_resultado['Porcentaje_18_35'],
                         c=labels, cmap='viridis', s=100, alpha=0.6, edgecolors='black')
    ax1.set_xlabel('% Mujeres')
    ax1.set_ylabel('% Edad 18-35')
    ax1.set_title('Clusters: % Mujeres vs % 18-35 años')
    plt.colorbar(scatter, ax=ax1, label='Cluster')
    
    # Scatter: Total Personas vs % Mujeres
    ax2 = axes[0, 1]
    scatter2 = ax2.scatter(df_resultado['Total_Personas'], 
                          df_resultado['Porcentaje_Mujeres'],
                          c=labels, cmap='viridis', s=100, alpha=0.6, edgecolors='black')
    ax2.set_xlabel('Total Personas')
    ax2.set_ylabel('% Mujeres')
    ax2.set_title('Clusters: Total Personas vs % Mujeres')
    ax2.set_xscale('log')
    plt.colorbar(scatter2, ax=ax2, label='Cluster')
    
    # Silhouette plot
    ax3 = axes[1, 0]
    y_lower = 10
    n_clusters = len(np.unique(labels))
    
    for i in range(n_clusters):
        cluster_silhouette_vals = silhouette_vals[labels == i]
        cluster_silhouette_vals.sort()
        
        size_cluster_i = cluster_silhouette_vals.shape[0]
        y_upper = y_lower + size_cluster_i
        
        color = plt.cm.viridis(float(i) / n_clusters)
        ax3.fill_betweenx(np.arange(y_lower, y_upper),
                         0, cluster_silhouette_vals,
                         facecolor=color, edgecolor=color, alpha=0.7)
        
        ax3.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10
    
    ax3.set_xlabel('Coeficiente Silhouette')
    ax3.set_ylabel('Cluster')
    ax3.set_title('Silhouette Plot por Cluster')
    ax3.axvline(x=silhouette_score(X_scaled, labels), color="red", linestyle="--", label='Promedio')
    ax3.legend()
    
    # Distribución de países por cluster
    ax4 = axes[1, 1]
    cluster_counts = df_resultado['Cluster'].value_counts().sort_index()
    ax4.bar(cluster_counts.index, cluster_counts.values, color='skyblue', edgecolor='black')
    ax4.set_xlabel('Cluster')
    ax4.set_ylabel('Número de Países')
    ax4.set_title('Distribución de Países por Cluster')
    ax4.set_xticks(cluster_counts.index)
    
    plt.tight_layout()
    plt.savefig('02_visualizacion_clusters.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado: 02_visualizacion_clusters.png")
    
    # 2. Heatmap de características por cluster
    fig, ax = plt.subplots(figsize=(10, 6))
    cluster_means = df_resultado.groupby('Cluster')[variables].mean()
    sns.heatmap(cluster_means.T, annot=True, fmt='.2f', cmap='YlOrRd', ax=ax, cbar_kws={'label': 'Valor'})
    ax.set_title('Características Promedio por Cluster')
    ax.set_xlabel('Cluster')
    ax.set_ylabel('Variable')
    plt.tight_layout()
    plt.savefig('03_heatmap_clusters.png', dpi=300, bbox_inches='tight')
    print("Gráfico guardado: 03_heatmap_clusters.png")

def guardar_resultados(df_resultado, ruta='resultados_clustering.csv'):
    """Guarda los resultados del clustering"""
    df_resultado.to_csv(ruta, index=False, encoding='utf-8-sig')
    print(f"\nResultados guardados en: {ruta}")

if __name__ == "__main__":
    # Cargar datos
    df = cargar_datos_agregados()
    
    # Seleccionar variables
    X, variables = seleccionar_variables(df)
    
    # Normalizar
    X_scaled, scaler = normalizar_datos(X)
    
    # Encontrar k óptimo
    k_optimo, silhouette_scores = encontrar_k_optimo(X_scaled)
    
    # Aplicar K-Means (puedes cambiar n_clusters si prefieres otro valor)
    n_clusters = 3  # Cambia esto si quieres probar con 2 o 4 clusters
    kmeans, labels, silhouette_avg, silhouette_vals = aplicar_kmeans(X_scaled, n_clusters)
    
    # Analizar clusters
    df_resultado = analizar_clusters(df, labels, variables)
    
    # Visualizar
    visualizar_clusters(df_resultado, X_scaled, labels, silhouette_vals, variables)
    
    # Guardar
    guardar_resultados(df_resultado)
    
    print("\n✓ Clustering completado exitosamente")
    print(f"\nMétrica final - Silhouette Score: {silhouette_avg:.4f}")
