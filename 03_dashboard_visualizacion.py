"""
Script de Visualización y Dashboard
Equipo B - Análisis de Migración Colombiana
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def cargar_datos():
    """Carga todos los datos necesarios"""
    df_limpio = pd.read_csv('datos_limpios.csv')
    df_clustering = pd.read_csv('resultados_clustering.csv')
    return df_limpio, df_clustering

def crear_dashboard_estatico(df_limpio, df_clustering):
    """Crea un dashboard estático con matplotlib"""
    print("Creando dashboard estático...")
    
    fig = plt.figure(figsize=(20, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 1. Distribución por género
    ax1 = fig.add_subplot(gs[0, 0])
    genero_counts = df_limpio['Género'].value_counts()
    ax1.pie(genero_counts.values, labels=genero_counts.index, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Distribución por Género', fontsize=14, fontweight='bold')
    
    # 2. Top 10 países
    ax2 = fig.add_subplot(gs[0, 1:])
    top_paises = df_limpio['País'].value_counts().head(10)
    ax2.barh(range(len(top_paises)), top_paises.values, color='steelblue')
    ax2.set_yticks(range(len(top_paises)))
    ax2.set_yticklabels(top_paises.index)
    ax2.set_xlabel('Número de Registros')
    ax2.set_title('Top 10 Países de Residencia', fontsize=14, fontweight='bold')
    ax2.invert_yaxis()
    
    # 3. Distribución de edad
    ax3 = fig.add_subplot(gs[1, 0])
    df_limpio['Edad (años)'].dropna().hist(bins=50, ax=ax3, color='coral', edgecolor='black')
    ax3.set_xlabel('Edad (años)')
    ax3.set_ylabel('Frecuencia')
    ax3.set_title('Distribución de Edad', fontsize=14, fontweight='bold')
    
    # 4. Nivel académico
    ax4 = fig.add_subplot(gs[1, 1])
    nivel_counts = df_limpio['Nivel Académico'].value_counts().head(8)
    ax4.bar(range(len(nivel_counts)), nivel_counts.values, color='lightgreen', edgecolor='black')
    ax4.set_xticks(range(len(nivel_counts)))
    ax4.set_xticklabels(nivel_counts.index, rotation=45, ha='right', fontsize=8)
    ax4.set_ylabel('Frecuencia')
    ax4.set_title('Nivel Académico', fontsize=14, fontweight='bold')
    
    # 5. Registros por año
    ax5 = fig.add_subplot(gs[1, 2])
    registros_año = df_limpio['Año Registro'].value_counts().sort_index()
    ax5.plot(registros_año.index, registros_año.values, marker='o', linewidth=2, color='purple')
    ax5.set_xlabel('Año')
    ax5.set_ylabel('Número de Registros')
    ax5.set_title('Registros por Año', fontsize=14, fontweight='bold')
    ax5.grid(True, alpha=0.3)
    
    # 6. Clusters - Mapa de países
    ax6 = fig.add_subplot(gs[2, :])
    for cluster in sorted(df_clustering['Cluster'].unique()):
        cluster_data = df_clustering[df_clustering['Cluster'] == cluster]
        ax6.scatter(cluster_data['Porcentaje_Mujeres'], 
                   cluster_data['Total_Personas'],
                   label=f'Cluster {cluster}', s=150, alpha=0.6, edgecolors='black')
    ax6.set_xlabel('% Mujeres')
    ax6.set_ylabel('Total Personas')
    ax6.set_yscale('log')
    ax6.set_title('Clusters de Países por Características Demográficas', fontsize=14, fontweight='bold')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    plt.suptitle('Dashboard - Análisis de Migración Colombiana', fontsize=18, fontweight='bold', y=0.995)
    plt.savefig('04_dashboard_completo.png', dpi=300, bbox_inches='tight')
    print("Dashboard guardado: 04_dashboard_completo.png")

def crear_dashboard_interactivo(df_limpio, df_clustering):
    """Crea un dashboard interactivo con Plotly"""
    print("Creando dashboard interactivo...")
    
    # Dashboard con subplots
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=('Top 15 Países', 'Distribución por Género',
                       'Nivel Académico', 'Registros por Año',
                       'Clusters 3D', 'Estado Civil'),
        specs=[[{"type": "bar"}, {"type": "pie"}],
               [{"type": "bar"}, {"type": "scatter"}],
               [{"type": "scatter3d"}, {"type": "pie"}]],
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )
    
    # 1. Top países
    top_paises = df_limpio['País'].value_counts().head(15)
    fig.add_trace(
        go.Bar(x=top_paises.values, y=top_paises.index, orientation='h',
               marker_color='steelblue', name='Países'),
        row=1, col=1
    )
    
    # 2. Género
    genero_counts = df_limpio['Género'].value_counts()
    fig.add_trace(
        go.Pie(labels=genero_counts.index, values=genero_counts.values, name='Género'),
        row=1, col=2
    )
    
    # 3. Nivel académico
    nivel_counts = df_limpio['Nivel Académico'].value_counts().head(10)
    fig.add_trace(
        go.Bar(x=nivel_counts.index, y=nivel_counts.values,
               marker_color='lightgreen', name='Nivel'),
        row=2, col=1
    )
    
    # 4. Registros por año
    registros_año = df_limpio['Año Registro'].value_counts().sort_index()
    fig.add_trace(
        go.Scatter(x=registros_año.index, y=registros_año.values,
                  mode='lines+markers', marker_color='purple', name='Registros'),
        row=2, col=2
    )
    
    # 5. Clusters 3D
    for cluster in sorted(df_clustering['Cluster'].unique()):
        cluster_data = df_clustering[df_clustering['Cluster'] == cluster]
        fig.add_trace(
            go.Scatter3d(
                x=cluster_data['Porcentaje_Mujeres'],
                y=cluster_data['Porcentaje_18_35'],
                z=cluster_data['Total_Personas'],
                mode='markers',
                marker=dict(size=8),
                name=f'Cluster {cluster}',
                text=cluster_data['Pais'],
                hovertemplate='<b>%{text}</b><br>% Mujeres: %{x:.1f}<br>% 18-35: %{y:.1f}<br>Total: %{z}'
            ),
            row=3, col=1
        )
    
    # 6. Estado civil
    estado_counts = df_limpio['Estado civil'].value_counts().head(5)
    fig.add_trace(
        go.Pie(labels=estado_counts.index, values=estado_counts.values, name='Estado Civil'),
        row=3, col=2
    )
    
    # Actualizar layout
    fig.update_layout(
        title_text="Dashboard Interactivo - Análisis de Migración Colombiana",
        title_font_size=20,
        showlegend=True,
        height=1400
    )
    
    fig.update_xaxes(title_text="Registros", row=1, col=1)
    fig.update_xaxes(title_text="Nivel Académico", row=2, col=1, tickangle=45)
    fig.update_xaxes(title_text="Año", row=2, col=2)
    
    fig.update_yaxes(title_text="País", row=1, col=1)
    fig.update_yaxes(title_text="Frecuencia", row=2, col=1)
    fig.update_yaxes(title_text="Registros", row=2, col=2)
    
    fig.write_html('05_dashboard_interactivo.html')
    print("Dashboard interactivo guardado: 05_dashboard_interactivo.html")

def crear_mapa_clusters(df_clustering):
    """Crea un mapa interactivo de clusters"""
    print("Creando mapa de clusters...")
    
    fig = px.scatter(df_clustering, 
                     x='Porcentaje_Mujeres', 
                     y='Porcentaje_18_35',
                     size='Total_Personas',
                     color='Cluster',
                     hover_name='Pais',
                     hover_data={
                         'Porcentaje_Mujeres': ':.1f',
                         'Porcentaje_18_35': ':.1f',
                         'Total_Personas': ':,',
                         'Cluster': True
                     },
                     title='Clusters de Países - Análisis Demográfico',
                     labels={
                         'Porcentaje_Mujeres': '% Mujeres',
                         'Porcentaje_18_35': '% Edad 18-35 años',
                         'Total_Personas': 'Total Registros'
                     },
                     color_continuous_scale='viridis')
    
    fig.update_layout(height=600, width=1000)
    fig.write_html('06_mapa_clusters_interactivo.html')
    print("Mapa de clusters guardado: 06_mapa_clusters_interactivo.html")

def generar_reporte_clusters(df_clustering):
    """Genera un reporte detallado de los clusters"""
    print("\nGenerando reporte de clusters...")
    
    reporte = []
    reporte.append("=" * 80)
    reporte.append("REPORTE DE CLUSTERING K-MEANS")
    reporte.append("Análisis de Migración Colombiana por País")
    reporte.append("=" * 80)
    reporte.append("")
    
    for cluster in sorted(df_clustering['Cluster'].unique()):
        cluster_data = df_clustering[df_clustering['Cluster'] == cluster]
        
        reporte.append(f"\n{'='*80}")
        reporte.append(f"CLUSTER {cluster}")
        reporte.append(f"{'='*80}")
        reporte.append(f"Número de países: {len(cluster_data)}")
        reporte.append(f"Total de personas: {cluster_data['Total_Personas'].sum():,.0f}")
        reporte.append("")
        reporte.append("Características promedio:")
        reporte.append(f"  - % Mujeres: {cluster_data['Porcentaje_Mujeres'].mean():.2f}%")
        reporte.append(f"  - % Edad 18-35: {cluster_data['Porcentaje_18_35'].mean():.2f}%")
        reporte.append(f"  - Edad promedio: {cluster_data['Edad_Promedio'].mean():.2f} años")
        reporte.append(f"  - % Educación superior: {cluster_data['Porcentaje_Educacion_Superior'].mean():.2f}%")
        reporte.append("")
        reporte.append("Países principales:")
        top_paises = cluster_data.nlargest(10, 'Total_Personas')[['Pais', 'Total_Personas']]
        for idx, row in top_paises.iterrows():
            reporte.append(f"  - {row['Pais']}: {row['Total_Personas']:,.0f} personas")
    
    reporte.append(f"\n{'='*80}")
    reporte.append("FIN DEL REPORTE")
    reporte.append(f"{'='*80}")
    
    reporte_texto = "\n".join(reporte)
    
    with open('07_reporte_clusters.txt', 'w', encoding='utf-8') as f:
        f.write(reporte_texto)
    
    print(reporte_texto)
    print("\nReporte guardado: 07_reporte_clusters.txt")

if __name__ == "__main__":
    # Cargar datos
    df_limpio, df_clustering = cargar_datos()
    
    # Crear visualizaciones
    crear_dashboard_estatico(df_limpio, df_clustering)
    crear_dashboard_interactivo(df_limpio, df_clustering)
    crear_mapa_clusters(df_clustering)
    generar_reporte_clusters(df_clustering)
    
    print("\n✓ Dashboard y visualizaciones completadas")
