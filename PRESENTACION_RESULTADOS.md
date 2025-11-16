# Presentación de Resultados - Clustering K-Means
## Equipo B - Análisis de Migración Colombiana

---

## 🎯 Objetivo del Proyecto

Aplicar clustering K-Means para identificar patrones demográficos en la migración colombiana a nivel global, utilizando datos de más de 500,000 registros.

---

## 📊 Dataset

- **Total registros**: 579,388
- **Países analizados**: 53 (con mínimo 100 registros)
- **Período**: 2013-2025
- **Variables principales**: Género, Edad, País de residencia, Nivel académico

---

## 🔬 Metodología

### 1. ETL y Limpieza
- Eliminación de duplicados
- Tratamiento de valores nulos
- Conversión de tipos de datos
- Agregación por país

### 2. Selección de Variables
**3 variables normalizadas:**
- % Mujeres (distribución de género)
- % Edad 18-35 años (población joven)
- Total de personas (volumen migratorio)

**¿Por qué estas variables?**
- Alta calidad de datos (pocos nulos)
- Relevancia demográfica
- Diferenciación clara entre países

### 3. Clustering K-Means
- Normalización con StandardScaler
- Evaluación de k=2 a k=10
- Selección de k=3 (balance interpretabilidad/calidad)
- Métrica: Silhouette Score

---

## 📈 Resultados Principales

### Silhouette Score: 0.334
- Indica clusters **moderadamente definidos**
- k=2 tuvo mejor score (0.674) pero menos información
- k=3 ofrece mejor balance para análisis práctico

### 3 Clusters Identificados

#### 🟦 Cluster 0: "Migración Equilibrada" (34 países)
**Perfil:**
- 56.6% mujeres (mayor proporción)
- 61.3% edad 18-35
- 153,904 personas

**Países clave:**
- Chile, Argentina, Canadá, Australia
- Europa occidental, Oceanía

**Interpretación:**
Destinos con migración balanceada, perfil profesional/familiar, mayor presencia femenina.

---

#### 🟩 Cluster 1: "Destinos Principales" (2 países)
**Perfil:**
- 52.7% mujeres (equilibrado)
- 66.9% edad 18-35 (más jóvenes)
- 353,376 personas (67% del total)

**Países:**
- España (187,243)
- Estados Unidos (166,133)

**Interpretación:**
Principales destinos migratorios, población más joven, oportunidades laborales/educativas.

---

#### 🟨 Cluster 2: "Migración Masculina" (17 países)
**Perfil:**
- 42.8% mujeres (predominio masculino)
- 64.9% edad 18-35
- 72,954 personas

**Países clave:**
- Ecuador, Brasil, Perú, Costa Rica
- América Latina principalmente

**Interpretación:**
Migración predominantemente masculina, posiblemente laboral, países vecinos.

---

## 🔍 Hallazgos Clave

### 1. Concentración Geográfica
- **67% de registros** en solo 2 países (España y USA)
- España es el destino #1 con 32.1% del total
- Top 10 países concentran 85% de la migración

### 2. Diferenciación por Género
- Cluster 0: Mayor presencia femenina (56.6%)
- Cluster 1: Equilibrado (52.7%)
- Cluster 2: Mayor presencia masculina (57.2%)

### 3. Población Joven
- Todos los clusters tienen 60-67% entre 18-35 años
- Edad promedio: 33 años
- Perfil migratorio joven y activo

### 4. Diversificación
- 164 países con presencia colombiana
- 53 países con comunidades significativas (>100 personas)
- Presencia global en todos los continentes

---

## ⚠️ Limitaciones del Estudio

### 1. Datos Agregados
- Análisis a nivel país, no individual
- Se pierde granularidad de patrones locales

### 2. Sesgos Potenciales
- **Sesgo de registro**: Solo personas que se registran
- **Sesgo geográfico**: Más datos donde hay más oficinas consulares
- **Sesgo temporal**: Solo desde 2013

### 3. Variables Limitadas
- Solo 3 variables demográficas
- Nivel educativo tiene 38% "NO INDICA"
- Estatura tiene 89% valores nulos

### 4. Ausencia de Series Temporales
- No se analiza evolución en el tiempo
- No se detectan tendencias o cambios

### 5. Calidad del Clustering
- Silhouette Score moderado (0.334)
- Indica solapamiento entre clusters
- Trade-off entre calidad métrica e interpretabilidad

---

## 💡 Conclusiones

### Principales Insights

1. **España y USA son excepcionales**: Concentran 2/3 de la migración registrada

2. **Género como diferenciador**: América Latina atrae más hombres, otros destinos más equilibrados

3. **Perfil joven predominante**: 60-67% entre 18-35 años en todos los clusters

4. **Diversificación global**: Presencia significativa en 53 países

### Aplicaciones Prácticas

**Para política consular:**
- Priorizar recursos en España y USA
- Adaptar servicios según perfil demográfico del cluster

**Para investigación:**
- Estudiar causas de migración masculina en América Latina
- Analizar factores de atracción en cada cluster

**Para programas de apoyo:**
- Diseñar servicios específicos por perfil demográfico
- Considerar diferencias de género en políticas

---

## 📁 Entregables

### Código
- `01_etl_limpieza.py`: ETL y limpieza
- `02_clustering_kmeans.py`: Clustering K-Means
- `03_dashboard_visualizacion.py`: Visualizaciones
- `ejecutar_todo.py`: Pipeline completo

### Datos
- `datos_limpios.csv`: 579k registros limpios
- `datos_agregados_pais.csv`: 53 países agregados
- `resultados_clustering.csv`: Resultados con clusters

### Visualizaciones
- `01_seleccion_k_optimo.png`: Método del codo
- `02_visualizacion_clusters.png`: Scatter plots
- `03_heatmap_clusters.png`: Heatmap
- `04_dashboard_completo.png`: Dashboard estático
- `05_dashboard_interactivo.html`: Dashboard interactivo
- `06_mapa_clusters_interactivo.html`: Mapa interactivo

### Reportes
- `07_reporte_clusters.txt`: Reporte detallado
- `INFORME_CLUSTERING.md`: Informe completo
- `PRESENTACION_RESULTADOS.md`: Este documento

---

## 🎓 Aspectos Técnicos

### Tecnologías
- Python 3.11
- pandas, numpy, scikit-learn
- matplotlib, seaborn, plotly

### Métricas
- **Silhouette Score**: 0.334
- **Inercia**: Evaluada para k=2 a k=10
- **Normalización**: StandardScaler

### Validación
- Método del codo
- Silhouette analysis
- Visualización de clusters

---

## 🚀 Próximos Pasos Sugeridos

1. **Análisis temporal**: Estudiar evolución de clusters en el tiempo
2. **Variables adicionales**: Incluir nivel educativo (mejorar calidad)
3. **Clustering jerárquico**: Comparar con otros algoritmos
4. **Análisis por ciudad**: Mayor granularidad en países grandes
5. **Validación externa**: Comparar con datos oficiales de migración

---

## 📞 Contacto

**Equipo B**  
Proyecto de Clustering K-Means  
Análisis de Migración Colombiana  
Noviembre 2024

---

## 🙏 Agradecimientos

Datos proporcionados por la universidad para análisis académico.

---

**Nota**: Todos los archivos HTML son interactivos. Ábrelos en tu navegador para explorar los datos dinámicamente.
