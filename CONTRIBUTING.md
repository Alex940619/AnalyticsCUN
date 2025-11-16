# Guía de Contribución

## Cómo Clonar el Proyecto

```bash
git clone https://github.com/Alex940619/AnalyticsCUN.git
cd AnalyticsCUN
```

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar el Proyecto

```bash
# Opción 1: Pipeline completo
python ejecutar_todo.py

# Opción 2: Paso a paso
python 00_analisis_exploratorio.py
python 01_etl_limpieza.py
python 02_clustering_kmeans.py
python 03_dashboard_visualizacion.py
```

## Verificar Instalación

```bash
python verificar_proyecto.py
```

## Estructura del Proyecto

```
AnalyticsCUN/
├── codigo/
│   ├── 00_analisis_exploratorio.py
│   ├── 01_etl_limpieza.py
│   ├── 02_clustering_kmeans.py
│   ├── 03_dashboard_visualizacion.py
│   └── ejecutar_todo.py
├── datos/
│   ├── datos_limpios.csv
│   ├── datos_agregados_pais.csv
│   └── resultados_clustering.csv
├── visualizaciones/
│   ├── *.png
│   └── *.html
├── documentacion/
│   ├── README.md
│   ├── INFORME_CLUSTERING.md
│   └── PRESENTACION_RESULTADOS.md
└── requirements.txt
```

## Reportar Problemas

Si encuentras algún problema, por favor abre un issue en GitHub.

## Equipo

Equipo B - Proyecto de Clustering K-Means
