# Informe de Clustering K-Means
## Análisis de Migración Colombiana - Equipo B

---

## 📊 Resumen Ejecutivo

Se realizó un análisis de clustering K-Means sobre datos de migración colombiana, agrupando 53 países según características demográficas. Se identificaron **3 clusters principales** con un **Silhouette Score de 0.334**.

---

## 🎯 Metodología

### Variables Utilizadas (Normalizadas)
1. **Porcentaje de Mujeres**: % de registros femeninos por país
2. **Porcentaje 18-35 años**: % de población joven adulta
3. **Total de Personas**: Cantidad total de registros por país

### Proceso
1. **ETL**: Limpieza de 500k+ registros, eliminación de duplicados y valores nulos
2. **Agregación**: Datos agrupados por país (filtro: mínimo 100 registros)
3. **Normalización**: StandardScaler para equiparar escalas
4. **Clustering**: K-Means con k=3 (evaluado k=2 a k=10)
5. **Validación**: Silhouette Score como métrica de calidad

---

## 🔍 Resultados

### Cluster 0: "Países de Migración Equilibrada" (34 países)
**Características:**
- 56.6% mujeres (mayor proporción)
- 61.3% edad 18-35 años
- 153,904 personas totales
- Edad promedio: 33.7 años

**Países principales:**
- Chile (22,500), Argentina (19,233), Canadá (17,851), Australia (17,681)
- Incluye: Europa occidental, América del Sur, Oceanía

**Interpretación:** Destinos con migración balanceada de género, ligeramente más mujeres, perfil profesional/familiar.

---

### Cluster 1: "Destinos Principales" (2 países)
**Características:**
- 52.7% mujeres (equilibrado)
- 66.9% edad 18-35 años (más jóvenes)
- 353,376 personas (67% del total)
- Edad promedio: 33.0 años

**Países:**
- España (187,243) y Estados Unidos (166,133)

**Interpretación:** Principales destinos migratorios, población más joven, oportunidades laborales/educativas.

---

### Cluster 2: "Países de Migración Masculina" (17 países)
**Características:**
- 42.8% mujeres (menor proporción - más hombres)
- 64.9% edad 18-35 años
- 72,954 personas totales
- Edad promedio: 33.2 años

**Países principales:**
- Ecuador (36,431), Brasil (15,424), Perú (6,216), Costa Rica (5,236)
- Incluye: América Latina, algunos países asiáticos y europeos

**Interpretación:** Migración predominantemente masculina, posiblemente laboral/económica, países vecinos o con vínculos culturales.

---

## 📈 Métricas de Calidad

### Silhouette Score: 0.334
- **Rango**: -1 (mal) a 1 (excelente)
- **Interpretación**: Clusters moderadamente definidos
- **Análisis**: 
  - k=2 obtuvo mejor score (0.674) pero menos granularidad
  - k=3 ofrece mejor balance entre interpretabilidad y separación
  - Clusters 0 y 2 bien diferenciados por género
  - Cluster 1 separado por volumen de migración

### Comparación de k:
- k=2: Silhouette 0.674 (España/USA vs resto)
- k=3: Silhouette 0.334 (seleccionado - mejor interpretación)
- k=4-10: Silhouette 0.31-0.39 (fragmentación excesiva)

---

## ⚠️ Riesgos y Limitaciones

### 1. Datos Agregados
- **Limitación**: Análisis a nivel país, se pierde información individual
- **Impacto**: No se pueden analizar patrones dentro de cada país
- **Mitigación**: Filtro de mínimo 100 registros por país para robustez

### 2. Posibles Sesgos
- **Sesgo de registro**: Datos dependen de quién se registra (no toda la población migrante)
- **Sesgo geográfico**: Países con más oficinas de registro tienen más datos
- **Sesgo temporal**: Registros desde 2015, no refleja migración histórica
- **Sesgo socioeconómico**: Personas con acceso a oficinas consulares

### 3. Ausencia de Series Temporales
- **Limitación**: No se analiza evolución temporal de la migración
- **Impacto**: No se pueden identificar tendencias o cambios en patrones
- **Alternativa**: Se agregó variable "Año Registro" pero no se usó en clustering

### 4. Variables Limitadas
- **Limitación**: Solo 3 variables demográficas básicas
- **Variables no incluidas**: 
  - Nivel educativo (muchos "NO INDICA")
  - Estatura (muchos valores 0 o nulos)
  - Área de conocimiento (alta proporción "NO INDICA")
- **Justificación**: Variables seleccionadas tienen mejor calidad de datos

### 5. Normalización y Escala
- **Limitación**: Total de personas tiene escala muy diferente (104 a 187,243)
- **Mitigación**: StandardScaler normaliza pero puede reducir importancia de volumen
- **Consideración**: Cluster 1 se define principalmente por volumen alto

### 6. Interpretabilidad vs Calidad
- **Trade-off**: k=2 tiene mejor silhouette pero menos información
- **Decisión**: k=3 ofrece mejor balance para análisis práctico
- **Riesgo**: Score moderado indica solapamiento entre clusters

---

## 💡 Conclusiones

### Hallazgos Principales
1. **España y Estados Unidos** son destinos excepcionales (67% de registros)
2. **Diferenciación por género** es un factor clave: países latinoamericanos atraen más hombres
3. **Edad joven** predomina en todos los clusters (60-67% entre 18-35 años)
4. **Diversificación geográfica**: 53 países con presencia significativa

### Recomendaciones
1. **Para análisis futuro**: Incluir series temporales para detectar tendencias
2. **Mejorar calidad de datos**: Reducir "NO INDICA" en variables educativas
3. **Análisis complementario**: Clustering por ciudad o región dentro de países grandes
4. **Validación**: Comparar con datos oficiales de migración

### Aplicaciones Prácticas
- **Política consular**: Priorizar recursos en España y USA
- **Programas de apoyo**: Adaptar servicios según perfil demográfico del cluster
- **Investigación**: Estudiar causas de migración masculina en Cluster 2

---

## 📁 Archivos Generados

### Datos
- `datos_limpios.csv`: Dataset completo limpio (500k+ registros)
- `datos_agregados_pais.csv`: Datos agregados por país (53 países)
- `resultados_clustering.csv`: Resultados con etiquetas de cluster

### Visualizaciones
- `01_seleccion_k_optimo.png`: Método del codo y silhouette por k
- `02_visualizacion_clusters.png`: Scatter plots y silhouette plot
- `03_heatmap_clusters.png`: Características promedio por cluster
- `04_dashboard_completo.png`: Dashboard estático completo
- `05_dashboard_interactivo.html`: Dashboard interactivo (Plotly)
- `06_mapa_clusters_interactivo.html`: Mapa de clusters interactivo

### Reportes
- `07_reporte_clusters.txt`: Reporte detallado de clusters
- `INFORME_CLUSTERING.md`: Este documento

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.11**
- **pandas**: Manipulación de datos
- **scikit-learn**: K-Means y métricas
- **matplotlib/seaborn**: Visualizaciones estáticas
- **plotly**: Visualizaciones interactivas
- **openpyxl**: Lectura de Excel

---

**Fecha de análisis**: Noviembre 2024  
**Equipo**: Equipo B  
**Dataset**: 500k+ registros de migración colombiana
