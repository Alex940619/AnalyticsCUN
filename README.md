# Proyecto Clustering K-Means - Análisis de Migración Colombiana
## Equipo B

Este proyecto realiza un análisis de clustering K-Means sobre datos de migración colombiana a nivel global.

## 📋 Estructura del Proyecto

```
.
├── 02_dataset_limpio_equipoB (1).xlsx  # Dataset original
├── requirements.txt                     # Dependencias Python
├── 01_etl_limpieza.py                  # Script de ETL y limpieza
├── 02_clustering_kmeans.py             # Script de clustering
├── 03_dashboard_visualizacion.py       # Script de visualización
└── README.md                           # Este archivo
```

## 🚀 Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Alex940619/AnalyticsCUN.git
cd AnalyticsCUN
```

2. **Descargar archivos grandes (opcional):**
Los archivos de datos grandes están en Google Drive:
📁 [Clustering_total - Google Drive](https://drive.google.com/drive/folders/Clustering_total)

**Nota:** No es necesario descargarlos para ejecutar el clustering y visualizaciones.

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

## 📊 Ejecución

### Opción A: Ejecutar Todo el Pipeline (Recomendado)
```bash
python ejecutar_todo.py
```
Este script ejecuta automáticamente todos los pasos en orden.

### Opción B: Ejecutar Paso a Paso

#### Paso 0 (Opcional): Análisis Exploratorio
```bash
python 00_analisis_exploratorio.py
```
**Salidas:** Estadísticas descriptivas en consola

#### Paso 1: ETL y Limpieza de Datos
```bash
python 01_etl_limpieza.py
```
**Salidas:**
- `datos_limpios.csv`: Dataset completo limpio (579k registros)
- `datos_agregados_pais.csv`: Datos agregados por país (53 países)

#### Paso 2: Clustering K-Means
```bash
python 02_clustering_kmeans.py
```
**Salidas:**
- `01_seleccion_k_optimo.png`: Gráficos para seleccionar k óptimo
- `02_visualizacion_clusters.png`: Visualización de clusters
- `03_heatmap_clusters.png`: Heatmap de características
- `resultados_clustering.csv`: Resultados con etiquetas de cluster

#### Paso 3: Dashboard y Visualizaciones
```bash
python 03_dashboard_visualizacion.py
```
**Salidas:**
- `04_dashboard_completo.png`: Dashboard estático
- `05_dashboard_interactivo.html`: Dashboard interactivo (abrir en navegador)
- `06_mapa_clusters_interactivo.html`: Mapa de clusters interactivo
- `07_reporte_clusters.txt`: Reporte detallado de clusters

## 🎯 Variables Utilizadas para Clustering

1. **Porcentaje de Mujeres**: % de registros femeninos por país
2. **Porcentaje 18-35 años**: % de población joven adulta
3. **Total de Personas**: Cantidad total de registros por país

Todas las variables son normalizadas usando StandardScaler antes del clustering.

## 📈 Métricas

- **Silhouette Score**: Mide la calidad de los clusters (rango: -1 a 1)
  - Valores cercanos a 1: clusters bien definidos
  - Valores cercanos a 0: clusters superpuestos
  - Valores negativos: asignaciones incorrectas

## ⚠️ Riesgos y Limitaciones

1. **Datos agregados**: Análisis a nivel país, se pierde granularidad individual
2. **Posibles sesgos**: 
   - Sesgos de selección en el registro
   - Países con pocos registros pueden distorsionar resultados
3. **Ausencia de series temporales**: No se analiza evolución en el tiempo
4. **Variables limitadas**: Solo 3 variables para clustering (simplificación)
5. **Normalización**: Países con muy pocos registros fueron filtrados (< 100)

## 🔧 Personalización

Para cambiar el número de clusters, edita en `02_clustering_kmeans.py`:
```python
n_clusters = 3  # Cambia a 2, 4, etc.
```

## 📝 Notas

- El script filtra países con menos de 100 registros para mayor robustez
- Los gráficos interactivos se abren en el navegador web
- Todos los archivos CSV usan codificación UTF-8 con BOM para compatibilidad con Excel
