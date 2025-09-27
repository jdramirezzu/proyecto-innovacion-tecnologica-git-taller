#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análisis Exploratorio de Datos (EDA) - Índice de Precios al Consumidor (IPC)
Autor: Proyecto de Innovación Tecnológica
Fecha: 2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configuración para visualizaciones
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

def cargar_y_combinar_datos():
    """
    Carga y combina los tres archivos CSV de IPC
    """
    print("🔄 Cargando archivos CSV...")
    
    # Lista de archivos CSV
    archivos = [
        'ipc_from_2014-09_to_2024-08.csv',
        'ipc_from_2019-09_to_2024-08.csv', 
        'ipc_from_2022-09_to_2024-08.csv'
    ]
    
    # Lista para almacenar los DataFrames
    dataframes = []
    
    for archivo in archivos:
        try:
            df = pd.read_csv(archivo)
            print(f"✅ {archivo}: {len(df)} registros cargados")
            dataframes.append(df)
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo {archivo}")
            return None
    
    # Combinar todos los DataFrames
    df_combinado = pd.concat(dataframes, ignore_index=True)
    print(f"📊 Total de registros combinados: {len(df_combinado)}")
    
    return df_combinado

def limpiar_datos(df):
    """
    Limpia y prepara los datos para el análisis
    """
    print("\n🧹 Limpiando datos...")
    
    # Crear una copia para no modificar el original
    df_limpio = df.copy()
    
    # Información inicial
    print(f"📋 Dimensiones originales: {df_limpio.shape}")
    print(f"📋 Columnas: {list(df_limpio.columns)}")
    
    # Verificar valores nulos
    print("\n🔍 Valores nulos por columna:")
    nulos = df_limpio.isnull().sum()
    print(nulos[nulos > 0] if nulos.sum() > 0 else "✅ No hay valores nulos")
    
    # Limpiar nombres de ciudades (remover comillas y espacios extra)
    df_limpio['city'] = df_limpio['city'].str.replace('"', '').str.strip()
    
    # Crear columna de fecha
    df_limpio['fecha'] = pd.to_datetime(df_limpio[['year', 'month']].assign(day=1))
    
    # Verificar tipos de datos
    print(f"\n📊 Tipos de datos:")
    print(df_limpio.dtypes)
    
    return df_limpio

def analisis_exploratorio_basico(df):
    """
    Realiza análisis exploratorio básico
    """
    print("\n📈 ANÁLISIS EXPLORATORIO BÁSICO")
    print("=" * 50)
    
    # Estadísticas descriptivas
    print("\n📊 Estadísticas descriptivas del IPC:")
    print(df['ipc'].describe())
    
    # Información sobre ciudades
    print(f"\n🏙️ Número de ciudades únicas: {df['city'].nunique()}")
    print("🏙️ Ciudades incluidas:")
    ciudades = df['city'].unique()
    for i, ciudad in enumerate(sorted(ciudades), 1):
        print(f"   {i:2d}. {ciudad}")
    
    # Información sobre categorías
    print(f"\n📦 Número de categorías únicas: {df['category'].nunique()}")
    print("📦 Categorías incluidas:")
    categorias = df['category'].unique()
    for i, categoria in enumerate(sorted(categorias), 1):
        print(f"   {i:2d}. {categoria}")
    
    # Rango temporal
    print(f"\n📅 Rango temporal:")
    print(f"   Desde: {df['fecha'].min().strftime('%Y-%m')}")
    print(f"   Hasta: {df['fecha'].max().strftime('%Y-%m')}")
    print(f"   Total de meses: {df['fecha'].nunique()}")
    
    # Análisis por ciudad
    print(f"\n🏙️ IPC promedio por ciudad (top 10):")
    ipc_por_ciudad = df.groupby('city')['ipc'].agg(['mean', 'std', 'count']).round(3)
    ipc_por_ciudad = ipc_por_ciudad.sort_values('mean', ascending=False)
    print(ipc_por_ciudad.head(10))
    
    # Análisis por categoría
    print(f"\n📦 IPC promedio por categoría:")
    ipc_por_categoria = df.groupby('category')['ipc'].agg(['mean', 'std', 'count']).round(3)
    ipc_por_categoria = ipc_por_categoria.sort_values('mean', ascending=False)
    print(ipc_por_categoria)

def crear_visualizaciones(df):
    """
    Crea visualizaciones del análisis exploratorio
    """
    print("\n📊 Creando visualizaciones...")
    
    # Configurar el estilo
    plt.style.use('seaborn-v0_8')
    
    # Crear figura con subplots
    fig = plt.figure(figsize=(20, 16))
    
    # 1. Distribución del IPC
    plt.subplot(3, 3, 1)
    plt.hist(df['ipc'], bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Distribución del IPC', fontsize=14, fontweight='bold')
    plt.xlabel('Valor del IPC')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3)
    
    # 2. Boxplot del IPC por ciudad (top 10)
    plt.subplot(3, 3, 2)
    top_ciudades = df.groupby('city')['ipc'].mean().nlargest(10).index
    df_top_ciudades = df[df['city'].isin(top_ciudades)]
    sns.boxplot(data=df_top_ciudades, x='ipc', y='city')
    plt.title('Distribución del IPC por Ciudad (Top 10)', fontsize=14, fontweight='bold')
    plt.xlabel('Valor del IPC')
    
    # 3. Evolución temporal del IPC promedio
    plt.subplot(3, 3, 3)
    ipc_temporal = df.groupby('fecha')['ipc'].mean()
    plt.plot(ipc_temporal.index, ipc_temporal.values, linewidth=2, color='red')
    plt.title('Evolución Temporal del IPC Promedio', fontsize=14, fontweight='bold')
    plt.xlabel('Fecha')
    plt.ylabel('IPC Promedio')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # 4. IPC por categoría
    plt.subplot(3, 3, 4)
    ipc_categoria = df.groupby('category')['ipc'].mean().sort_values(ascending=True)
    ipc_categoria.plot(kind='barh', color='lightgreen')
    plt.title('IPC Promedio por Categoría', fontsize=14, fontweight='bold')
    plt.xlabel('IPC Promedio')
    
    # 5. Heatmap de IPC por ciudad y año
    plt.subplot(3, 3, 5)
    pivot_data = df.pivot_table(values='ipc', index='city', columns='year', aggfunc='mean')
    # Seleccionar solo algunas ciudades para mejor visualización
    ciudades_seleccionadas = df['city'].value_counts().head(8).index
    pivot_subset = pivot_data.loc[ciudades_seleccionadas]
    sns.heatmap(pivot_subset, annot=True, fmt='.2f', cmap='YlOrRd', cbar_kws={'label': 'IPC Promedio'})
    plt.title('Heatmap IPC por Ciudad y Año', fontsize=14, fontweight='bold')
    plt.xlabel('Año')
    plt.ylabel('Ciudad')
    
    # 6. Violin plot del IPC por categoría
    plt.subplot(3, 3, 6)
    sns.violinplot(data=df, x='ipc', y='category')
    plt.title('Distribución del IPC por Categoría', fontsize=14, fontweight='bold')
    plt.xlabel('Valor del IPC')
    
    # 7. IPC mensual promedio
    plt.subplot(3, 3, 7)
    ipc_mensual = df.groupby('month')['ipc'].mean()
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
             'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    plt.bar(range(1, 13), [ipc_mensual.get(i, 0) for i in range(1, 13)], 
            color='orange', alpha=0.7)
    plt.title('IPC Promedio por Mes', fontsize=14, fontweight='bold')
    plt.xlabel('Mes')
    plt.ylabel('IPC Promedio')
    plt.xticks(range(1, 13), meses, rotation=45)
    plt.grid(True, alpha=0.3)
    
    # 8. Scatter plot: IPC vs Año
    plt.subplot(3, 3, 8)
    plt.scatter(df['year'], df['ipc'], alpha=0.5, color='purple')
    plt.title('Relación IPC vs Año', fontsize=14, fontweight='bold')
    plt.xlabel('Año')
    plt.ylabel('Valor del IPC')
    plt.grid(True, alpha=0.3)
    
    # 9. Top 10 ciudades con mayor variabilidad
    plt.subplot(3, 3, 9)
    variabilidad = df.groupby('city')['ipc'].std().nlargest(10)
    variabilidad.plot(kind='bar', color='coral')
    plt.title('Top 10 Ciudades con Mayor Variabilidad', fontsize=14, fontweight='bold')
    plt.xlabel('Ciudad')
    plt.ylabel('Desviación Estándar del IPC')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('analisis_exploratorio_ipc.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✅ Visualizaciones guardadas como 'analisis_exploratorio_ipc.png'")

def generar_resumen_estadistico(df):
    """
    Genera un resumen estadístico detallado
    """
    print("\n📋 RESUMEN ESTADÍSTICO DETALLADO")
    print("=" * 50)
    
    # Estadísticas generales
    print(f"📊 Total de observaciones: {len(df):,}")
    print(f"📊 Período analizado: {df['fecha'].min().strftime('%Y-%m')} a {df['fecha'].max().strftime('%Y-%m')}")
    print(f"📊 Ciudades analizadas: {df['city'].nunique()}")
    print(f"📊 Categorías analizadas: {df['category'].nunique()}")
    
    # Estadísticas del IPC
    print(f"\n📈 Estadísticas del IPC:")
    print(f"   Media: {df['ipc'].mean():.3f}")
    print(f"   Mediana: {df['ipc'].median():.3f}")
    print(f"   Desviación estándar: {df['ipc'].std():.3f}")
    print(f"   Mínimo: {df['ipc'].min():.3f}")
    print(f"   Máximo: {df['ipc'].max():.3f}")
    print(f"   Rango: {df['ipc'].max() - df['ipc'].min():.3f}")
    
    # Análisis de valores extremos
    q1 = df['ipc'].quantile(0.25)
    q3 = df['ipc'].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    
    outliers = df[(df['ipc'] < limite_inferior) | (df['ipc'] > limite_superior)]
    print(f"\n🔍 Análisis de valores extremos:")
    print(f"   Valores atípicos detectados: {len(outliers)} ({len(outliers)/len(df)*100:.1f}%)")
    print(f"   Límite inferior: {limite_inferior:.3f}")
    print(f"   Límite superior: {limite_superior:.3f}")
    
    # Top 5 ciudades con mayor IPC promedio
    print(f"\n🏆 Top 5 ciudades con mayor IPC promedio:")
    top_ciudades = df.groupby('city')['ipc'].mean().nlargest(5)
    for i, (ciudad, ipc) in enumerate(top_ciudades.items(), 1):
        print(f"   {i}. {ciudad}: {ipc:.3f}")
    
    # Top 5 categorías con mayor IPC promedio
    print(f"\n📦 Top 5 categorías con mayor IPC promedio:")
    top_categorias = df.groupby('category')['ipc'].mean().nlargest(5)
    for i, (categoria, ipc) in enumerate(top_categorias.items(), 1):
        print(f"   {i}. {categoria}: {ipc:.3f}")

def main():
    """
    Función principal que ejecuta todo el análisis
    """
    print("🚀 INICIANDO ANÁLISIS EXPLORATORIO DE DATOS - IPC")
    print("=" * 60)
    
    # Cargar y combinar datos
    df = cargar_y_combinar_datos()
    if df is None:
        print("❌ Error al cargar los datos. Verifica que los archivos CSV estén presentes.")
        return
    
    # Limpiar datos
    df_limpio = limpiar_datos(df)
    
    # Análisis exploratorio básico
    analisis_exploratorio_basico(df_limpio)
    
    # Generar resumen estadístico
    generar_resumen_estadistico(df_limpio)
    
    # Crear visualizaciones
    crear_visualizaciones(df_limpio)
    
    # Guardar datos combinados
    df_limpio.to_csv('datos_ipc_combinados.csv', index=False)
    print(f"\n💾 Datos combinados guardados como 'datos_ipc_combinados.csv'")
    
    print("\n✅ ANÁLISIS COMPLETADO EXITOSAMENTE")
    print("=" * 60)
    print("📁 Archivos generados:")
    print("   - analisis_exploratorio_ipc.png (visualizaciones)")
    print("   - datos_ipc_combinados.csv (datos combinados)")

if __name__ == "__main__":
    main()
