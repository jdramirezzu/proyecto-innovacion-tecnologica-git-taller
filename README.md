# Análisis Exploratorio de Datos - Índice de Precios al Consumidor (IPC)

Este proyecto realiza un análisis exploratorio de datos (EDA) sobre el Índice de Precios al Consumidor (IPC) de Colombia, combinando datos de tres archivos CSV que cubren diferentes períodos temporales.

## ✨ Nuevas Características

- **🎯 Menú Interactivo de Gráficos**: Selecciona qué gráfico ver individualmente
- **📊 Modo Automático**: Ve todos los gráficos en una sola ventana
- **🔄 Validación de Entrada**: Manejo robusto de errores y opciones inválidas
- **👋 Salida Flexible**: Sal del programa en cualquier momento

## 📁 Archivos del Proyecto

- `analisis_exploratorio_ipc.py` - Script principal de análisis
- `requirements.txt` - Dependencias de Python
- `ipc_from_2014-09_to_2024-08.csv` - Datos IPC 2014-2024
- `ipc_from_2019-09_to_2024-08.csv` - Datos IPC 2019-2024  
- `ipc_from_2022-09_to_2024-08.csv` - Datos IPC 2022-2024

## 🚀 Instalación y Uso

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar el análisis
```bash
python analisis_exploratorio_ipc.py
```

### 3. Usar el menú interactivo
Una vez ejecutado, el script te preguntará qué tipo de visualización deseas:
- **Opción 1**: Ver todos los gráficos automáticamente
- **Opción 2**: Seleccionar gráficos individualmente (modo interactivo)

En el modo interactivo, podrás elegir entre 9 gráficos diferentes o ver todos juntos.

## 📊 Funcionalidades del Script

### 🔄 Carga y Combinación de Datos
- Carga automática de los tres archivos CSV
- Combinación de todos los datasets
- Limpieza y estandarización de datos

### 📈 Análisis Exploratorio
- **Estadísticas descriptivas** del IPC
- **Análisis por ciudad** y categoría
- **Evolución temporal** del IPC
- **Detección de valores atípicos**
- **Análisis de variabilidad** por región

### 🎯 Menú Interactivo de Gráficos
El script incluye un **menú interactivo** que te permite elegir cómo visualizar los datos:

#### Opciones de Visualización:
1. **📊 Ver todos los gráficos automáticamente** - Muestra los 9 gráficos en una sola ventana
2. **🎯 Seleccionar gráficos individualmente** - Menú interactivo para elegir gráficos específicos

#### Gráficos Disponibles (Modo Individual):
1. **📈 Distribución del IPC** - Histograma de frecuencias
2. **📦 Boxplot del IPC por Ciudad** - Top 10 ciudades
3. **📅 Evolución Temporal del IPC Promedio** - Tendencia temporal
4. **🏷️ IPC Promedio por Categoría** - Comparación entre categorías
5. **🔥 Heatmap IPC por Ciudad y Año** - Mapa de calor temporal
6. **🎻 Violin Plot del IPC por Categoría** - Distribuciones detalladas
7. **📆 IPC Promedio por Mes** - Patrones estacionales
8. **📊 Scatter Plot: IPC vs Año** - Relación temporal
9. **📈 Top 10 Ciudades con Mayor Variabilidad** - Análisis de variabilidad

### 📋 Resumen Estadístico
- Estadísticas descriptivas completas
- Análisis de valores extremos
- Rankings de ciudades y categorías
- Métricas de variabilidad

## 📁 Archivos de Salida

- `analisis_exploratorio_ipc.png` - Visualizaciones del análisis
- `datos_ipc_combinados.csv` - Dataset combinado y limpio

## 🏙️ Ciudades Analizadas

El análisis incluye datos de múltiples ciudades colombianas, incluyendo:
- Bogotá, D.C.
- Medellín
- Barranquilla
- Cartagena de Indias
- Cali
- Bucaramanga
- Y muchas más...

## 📦 Categorías de Productos

- Alimentos y Bebidas No Alcohólicas
- Bebidas Alcohólicas y Tabaco
- Vestuario y Calzado
- Vivienda, Servicios Públicos y Combustibles
- Muebles, Artículos para el Hogar y Mantenimiento
- Salud
- Transporte
- Información y Comunicación
- Recreación y Cultura
- Educación
- Restaurantes y Hoteles
- Bienes y Servicios Diversos

## 🔧 Requisitos del Sistema

- Python 3.7+
- pandas >= 1.5.0
- numpy >= 1.21.0
- matplotlib >= 3.5.0
- seaborn >= 0.11.0

## 📝 Notas Técnicas

- El script maneja automáticamente la limpieza de datos
- Las visualizaciones se guardan en alta resolución (300 DPI)
- Se incluye manejo de errores para archivos faltantes
- El análisis es completamente reproducible
- **Nueva funcionalidad**: Menú interactivo para selección de gráficos
- Validación de entrada y manejo de errores en el modo interactivo
- Opción de salida en cualquier momento (Ctrl+C o '0')

## 🤝 Contribuciones

Este proyecto forma parte del taller de innovación tecnológica. Para contribuir:

1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.
