# Archivos de Datos Grandes

## ⚠️ Archivos No Incluidos en el Repositorio

Debido a las limitaciones de tamaño de GitHub, los siguientes archivos **NO** están incluidos en este repositorio:

### 1. Dataset Original
- **Archivo**: `02_dataset_limpio_equipoB (1).xlsx`
- **Tamaño**: ~71 MB
- **Descripción**: Dataset original de Excel con 579,388 registros

### 2. Datos Limpios Completos
- **Archivo**: `datos_limpios.csv`
- **Tamaño**: ~123 MB
- **Descripción**: Dataset completo limpio en formato CSV

## ✅ Archivos Incluidos

Los siguientes archivos SÍ están en el repositorio y son suficientes para reproducir el análisis:

- ✓ `datos_agregados_pais.csv` (~5 KB) - Datos agregados por país (53 países)
- ✓ `resultados_clustering.csv` (~3 KB) - Resultados del clustering con etiquetas
- ✓ Todas las visualizaciones PNG y HTML
- ✓ Todo el código Python

## 🔄 Cómo Obtener los Archivos Grandes

### Opción 1: Descargar desde Google Drive (Recomendado) ⭐
Los archivos grandes están disponibles en Google Drive:

**📁 [Clustering_total - Google Drive](https://drive.google.com/drive/folders/Clustering_total)**

Archivos disponibles:
- `02_dataset_limpio_equipoB (1).xlsx` - Dataset original (71 MB)
- `datos_limpios.csv` - Datos limpios completos (123 MB)

### Opción 2: Ejecutar el ETL
Si tienes el archivo Excel original, puedes generar `datos_limpios.csv`:

```bash
python 01_etl_limpieza.py
```

### Opción 3: Usar Solo los Datos Agregados
Puedes trabajar directamente con los archivos incluidos en el repo:

```bash
# Saltar el ETL y ejecutar directamente el clustering
python 02_clustering_kmeans.py

# O ejecutar las visualizaciones
python 03_dashboard_visualizacion.py
```

### Opción 4: Contactar al Equipo
Si tienes problemas para acceder a los archivos, contacta a:
- Equipo B
- Repositorio: https://github.com/Alex940619/AnalyticsCUN.git

## 📊 Alternativas

### Usar Git LFS (Git Large File Storage)
Si quieres versionar archivos grandes, considera usar Git LFS:

```bash
# Instalar Git LFS
git lfs install

# Rastrear archivos grandes
git lfs track "*.xlsx"
git lfs track "datos_limpios.csv"

# Commit y push
git add .gitattributes
git commit -m "Configurar Git LFS"
git push
```

### Usar Servicios de Almacenamiento
Alternativas para compartir archivos grandes:
- Google Drive
- Dropbox
- OneDrive
- AWS S3
- Kaggle Datasets

## 💡 Nota Importante

El proyecto está diseñado para funcionar **sin necesidad de los archivos grandes**. Los archivos agregados (`datos_agregados_pais.csv` y `resultados_clustering.csv`) contienen toda la información necesaria para:

- ✓ Ejecutar el clustering
- ✓ Generar visualizaciones
- ✓ Reproducir el análisis
- ✓ Crear dashboards

Solo necesitas los archivos grandes si quieres:
- Volver a ejecutar el ETL desde cero
- Explorar los datos individuales (579k registros)
- Modificar la agregación de datos

## 📝 Resumen

| Archivo | Tamaño | Incluido | Necesario |
|---------|--------|----------|-----------|
| `02_dataset_limpio_equipoB (1).xlsx` | 71 MB | ❌ | Solo para ETL |
| `datos_limpios.csv` | 123 MB | ❌ | Solo para ETL |
| `datos_agregados_pais.csv` | 5 KB | ✅ | ✅ Sí |
| `resultados_clustering.csv` | 3 KB | ✅ | ✅ Sí |
| Código Python | < 1 MB | ✅ | ✅ Sí |
| Visualizaciones | ~3 MB | ✅ | ✅ Sí |

---

**¿Preguntas?** Abre un issue en el repositorio.
