# GRÁFICAS DE FUNCIONES DE PERTENENCIA - SISTEMA EXPERTO BURNOUT
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import os

# Crear directorio para gráficas
os.makedirs('graficas', exist_ok=True)

# Universos de discurso
x_horas_ded = np.arange(0, 17, 1)
x_carga = np.arange(1, 11, 1)
x_horas_sueno = np.arange(0, 15, 1)
x_cal_sueno = np.arange(1, 11, 1)
x_estres = np.arange(1, 11, 1)
x_mbi = np.arange(0, 7, 1)
x_riesgo = np.arange(0, 101, 1)

# Función auxiliar para generar y guardar gráficas
def plot_membership(x, conjuntos, labels, colores, titulo, xlabel, filename):
    fig, ax = plt.subplots(figsize=(8, 4))
    for mf, label, color in zip(conjuntos, labels, colores):
        ax.plot(x, mf, color, linewidth=2, label=label)
        ax.fill_between(x, mf, alpha=0.15, color=color)
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel('Grado de Pertenencia', fontsize=11)
    ax.legend(loc='best', fontsize=10)
    ax.set_ylim([-0.05, 1.1])
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'graficas/{filename}.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {filename}.png guardada")

print("Generando gráficas de funciones de pertenencia...\n")

# 1. Horas de dedicación
plot_membership(x_horas_ded,
    [fuzz.trimf(x_horas_ded, [0, 0, 5]),
     fuzz.trimf(x_horas_ded, [4, 7, 10]),
     fuzz.trapmf(x_horas_ded, [9, 12, 16, 16])],
    ['Reducida', 'Estándar', 'Excesiva'],
    ['#2196F3', '#FF9800', '#F44336'],
    'Horas de Dedicación Diaria (Estudio/Trabajo)',
    'Horas', '01_horas_dedicacion')

# 2. Carga de trabajo
plot_membership(x_carga,
    [fuzz.trimf(x_carga, [1, 1, 4]),
     fuzz.trimf(x_carga, [3, 5, 7]),
     fuzz.trapmf(x_carga, [6, 8, 10, 10])],
    ['Ligera', 'Manejable', 'Abrumadora'],
    ['#4CAF50', '#FF9800', '#F44336'],
    'Carga de Trabajo Percibida',
    'Nivel (1-10)', '02_carga_trabajo')

# 3. Horas de sueño
plot_membership(x_horas_sueno,
    [fuzz.trimf(x_horas_sueno, [0, 0, 5]),
     fuzz.trimf(x_horas_sueno, [5, 7, 9]),
     fuzz.trapmf(x_horas_sueno, [8, 10, 14, 14])],
    ['Insuficiente', 'Saludable', 'Prolongada'],
    ['#F44336', '#4CAF50', '#2196F3'],
    'Horas de Sueño Diarias',
    'Horas', '03_horas_sueno')

# 4. Calidad del sueño
plot_membership(x_cal_sueno,
    [fuzz.trimf(x_cal_sueno, [1, 1, 3]),
     fuzz.trimf(x_cal_sueno, [2, 4, 6]),
     fuzz.trimf(x_cal_sueno, [5, 7, 9]),
     fuzz.trapmf(x_cal_sueno, [8, 9, 10, 10])],
    ['Insuficiente', 'Pobre', 'Aceptable', 'Excelente'],
    ['#F44336', '#FF9800', '#FFC107', '#4CAF50'],
    'Calidad del Sueño',
    'Nivel (1-10)', '04_calidad_sueno')

# 5. Estrés diario
plot_membership(x_estres,
    [fuzz.trimf(x_estres, [1, 1, 3]),
     fuzz.trimf(x_estres, [2, 4, 6]),
     fuzz.trimf(x_estres, [5, 7, 9]),
     fuzz.trapmf(x_estres, [8, 9, 10, 10])],
    ['Bajo', 'Moderado', 'Alto', 'Crónico'],
    ['#4CAF50', '#FFC107', '#FF9800', '#F44336'],
    'Nivel de Estrés Diario',
    'Nivel (1-10)', '05_estres')

# 6. Agotamiento emocional
plot_membership(x_mbi,
    [fuzz.trimf(x_mbi, [0, 0, 2]),
     fuzz.trimf(x_mbi, [1, 2.5, 4]),
     fuzz.trimf(x_mbi, [3, 4, 5]),
     fuzz.trapmf(x_mbi, [4, 5, 6, 6])],
    ['Raro/Nunca', 'Ocasional', 'Frecuente', 'Persistente'],
    ['#4CAF50', '#FFC107', '#FF9800', '#F44336'],
    'Agotamiento Emocional (MBI)',
    'Frecuencia (0-6)', '06_agotamiento_emocional')

# 7. Fatiga anticipatoria
plot_membership(x_mbi,
    [fuzz.trimf(x_mbi, [0, 0, 2]),
     fuzz.trimf(x_mbi, [1, 3, 5]),
     fuzz.trapmf(x_mbi, [4, 5, 6, 6])],
    ['Nula', 'Leve', 'Severa'],
    ['#4CAF50', '#FF9800', '#F44336'],
    'Fatiga Anticipatoria (MBI)',
    'Frecuencia (0-6)', '07_fatiga_anticipatoria')

# 8. Saturación mental
plot_membership(x_mbi,
    [fuzz.trimf(x_mbi, [0, 0, 2]),
     fuzz.trimf(x_mbi, [1, 3, 5]),
     fuzz.trapmf(x_mbi, [4, 5, 6, 6])],
    ['Controlado', 'Al límite', 'Desbordado'],
    ['#4CAF50', '#FF9800', '#F44336'],
    'Saturación Mental (MBI)',
    'Frecuencia (0-6)', '08_saturacion_mental')

# 9. Despersonalización / Cinismo
plot_membership(x_mbi,
    [fuzz.trimf(x_mbi, [0, 0, 2]),
     fuzz.trimf(x_mbi, [1, 3, 5]),
     fuzz.trapmf(x_mbi, [4, 5, 6, 6])],
    ['Empático/Cercano', 'Distante', 'Indiferente/Cínico'],
    ['#4CAF50', '#FF9800', '#F44336'],
    'Despersonalización / Cinismo (MBI)',
    'Frecuencia (0-6)', '09_despersonalizacion')

# 10. Indiferencia
plot_membership(x_mbi,
    [fuzz.trimf(x_mbi, [0, 0, 2]),
     fuzz.trimf(x_mbi, [1, 3, 5]),
     fuzz.trapmf(x_mbi, [4, 5, 6, 6])],
    ['Comprometido', 'Despegado', 'Indiferente'],
    ['#4CAF50', '#FF9800', '#F44336'],
    'Indiferencia ante el Entorno (MBI)',
    'Frecuencia (0-6)', '10_indiferencia')

# 11. Deshumanización
plot_membership(x_mbi,
    [fuzz.trimf(x_mbi, [0, 0, 2]),
     fuzz.trimf(x_mbi, [1, 3, 5]),
     fuzz.trapmf(x_mbi, [4, 5, 6, 6])],
    ['Humano/Empático', 'Distante', 'Deshumanizado'],
    ['#4CAF50', '#FF9800', '#F44336'],
    'Deshumanización en el Trato (MBI)',
    'Frecuencia (0-6)', '11_deshumanizacion')

# 12. Percepción de utilidad (INVERTIDA)
plot_membership(x_mbi,
    [fuzz.trimf(x_mbi, [0, 0, 2]),
     fuzz.trimf(x_mbi, [1, 3, 5]),
     fuzz.trapmf(x_mbi, [4, 5, 6, 6])],
    ['Inútil/Nulo', 'Productivo', 'Muy Valioso'],
    ['#F44336', '#FF9800', '#4CAF50'],
    'Percepción de Utilidad (MBI - Invertida)',
    'Frecuencia (0-6)', '12_utilidad')

# 13. Autorrealización (INVERTIDA)
plot_membership(x_mbi,
    [fuzz.trimf(x_mbi, [0, 0, 2]),
     fuzz.trimf(x_mbi, [1, 3, 5]),
     fuzz.trapmf(x_mbi, [4, 5, 6, 6])],
    ['Frustrado', 'Satisfecho', 'Plenamente Realizado'],
    ['#F44336', '#FF9800', '#4CAF50'],
    'Autorrealización (MBI - Invertida)',
    'Frecuencia (0-6)', '13_autorrealizacion')

# 14. Competencia percibida (INVERTIDA)
plot_membership(x_mbi,
    [fuzz.trimf(x_mbi, [0, 0, 2]),
     fuzz.trimf(x_mbi, [1, 3, 5]),
     fuzz.trapmf(x_mbi, [4, 5, 6, 6])],
    ['Nula', 'Adecuada', 'Destacada'],
    ['#F44336', '#FF9800', '#4CAF50'],
    'Competencia Percibida (MBI - Invertida)',
    'Frecuencia (0-6)', '14_competencia')

# 15. Variable de SALIDA: Riesgo de Burnout
plot_membership(x_riesgo,
    [fuzz.trimf(x_riesgo, [0, 0, 20]),
     fuzz.trimf(x_riesgo, [10, 25, 40]),
     fuzz.trimf(x_riesgo, [30, 50, 70]),
     fuzz.trimf(x_riesgo, [60, 75, 90]),
     fuzz.trapmf(x_riesgo, [80, 90, 100, 100])],
    ['Muy Bajo', 'Bajo', 'Moderado', 'Alto', 'Crítico'],
    ['#2196F3', '#4CAF50', '#FFC107', '#FF9800', '#F44336'],
    'Variable de Salida: Riesgo de Burnout',
    'Nivel de Riesgo (%)', '15_riesgo_burnout')

print(f"\n Todas las gráficas guardadas en la carpeta 'graficas/'")
