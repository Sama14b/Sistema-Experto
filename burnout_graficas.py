# GRÁFICAS DE FUNCIONES DE PERTENENCIA - SISTEMA EXPERTO BURNOUT
import numpy as np
import skfuzzy as fuzz
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

os.makedirs('graficas', exist_ok=True)

# Universos de discurso
x_carga = np.arange(1, 11, 1)
x_cal_sueno = np.arange(1, 11, 1)
x_horas_sueno = np.arange(0, 15, 1)
x_estres = np.arange(1, 11, 1)
x_mbi = np.arange(0, 7, 1)
x_desc = np.arange(1, 4, 1)
x_apoyo = np.arange(1, 4, 1)
x_riesgo = np.arange(0, 101, 1)

def plot_mf(x, conjuntos, labels, colores, titulo, xlabel, filename):
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
    print(f"  ✓ {filename}.png")

print("Generando gráficas de funciones de pertenencia...\n")

# 1. Carga de trabajo
plot_mf(x_carga,
    [fuzz.trimf(x_carga, [1,1,4]), fuzz.trimf(x_carga, [3,5,7]), fuzz.trapmf(x_carga, [6,8,10,10])],
    ['Ligera', 'Manejable', 'Abrumadora'], ['#4CAF50','#FF9800','#F44336'],
    'Carga de Trabajo Percibida', 'Nivel (1-10)', '01_carga_trabajo')

# 2. Calidad del sueño
plot_mf(x_cal_sueno,
    [fuzz.trimf(x_cal_sueno,[1,1,3]), fuzz.trimf(x_cal_sueno,[2,4,6]),
     fuzz.trimf(x_cal_sueno,[5,7,9]), fuzz.trapmf(x_cal_sueno,[8,9,10,10])],
    ['Insuficiente','Pobre','Aceptable','Excelente'], ['#F44336','#FF9800','#FFC107','#4CAF50'],
    'Calidad del Sueño', 'Nivel (1-10)', '02_calidad_sueno')

# 3. Horas de sueño
plot_mf(x_horas_sueno,
    [fuzz.trimf(x_horas_sueno,[0,0,5]), fuzz.trimf(x_horas_sueno,[5,7,9]),
     fuzz.trapmf(x_horas_sueno,[8,10,14,14])],
    ['Insuficiente','Saludable','Prolongada'], ['#F44336','#4CAF50','#2196F3'],
    'Horas de Sueño Diarias', 'Horas', '03_horas_sueno')

# 4. Estrés diario
plot_mf(x_estres,
    [fuzz.trimf(x_estres,[1,1,3]), fuzz.trimf(x_estres,[2,4,6]),
     fuzz.trimf(x_estres,[5,7,9]), fuzz.trapmf(x_estres,[8,9,10,10])],
    ['Bajo','Moderado','Alto','Crónico'], ['#4CAF50','#FFC107','#FF9800','#F44336'],
    'Nivel de Estrés Diario', 'Nivel (1-10)', '04_estres')

# 5. Agotamiento emocional
plot_mf(x_mbi,
    [fuzz.trimf(x_mbi,[0,0,2]), fuzz.trimf(x_mbi,[1,2.5,4]),
     fuzz.trimf(x_mbi,[3,4,5]), fuzz.trapmf(x_mbi,[4,5,6,6])],
    ['Raro/Nunca','Ocasional','Frecuente','Persistente'], ['#4CAF50','#FFC107','#FF9800','#F44336'],
    'Agotamiento Emocional (MBI)', 'Frecuencia (0-6)', '05_agotamiento_emocional')

# 6. Fatiga anticipatoria
plot_mf(x_mbi,
    [fuzz.trimf(x_mbi,[0,0,2]), fuzz.trimf(x_mbi,[1,3,5]), fuzz.trapmf(x_mbi,[4,5,6,6])],
    ['Nula','Leve','Severa'], ['#4CAF50','#FF9800','#F44336'],
    'Fatiga Anticipatoria (MBI)', 'Frecuencia (0-6)', '06_fatiga_anticipatoria')

# 7. Despersonalización / Cinismo
plot_mf(x_mbi,
    [fuzz.trimf(x_mbi,[0,0,2]), fuzz.trimf(x_mbi,[1,3,5]), fuzz.trapmf(x_mbi,[4,5,6,6])],
    ['Empático/Cercano','Distante','Indiferente/Cínico'], ['#4CAF50','#FF9800','#F44336'],
    'Despersonalización / Cinismo (MBI)', 'Frecuencia (0-6)', '07_despersonalizacion')

# 8. Percepción de utilidad (INVERTIDA)
plot_mf(x_mbi,
    [fuzz.trimf(x_mbi,[0,0,2]), fuzz.trimf(x_mbi,[1,3,5]), fuzz.trapmf(x_mbi,[4,5,6,6])],
    ['Inútil/Nulo','Productivo','Muy Valioso'], ['#F44336','#FF9800','#4CAF50'],
    'Percepción de Utilidad (MBI - Invertida)', 'Frecuencia (0-6)', '08_utilidad')

# 9. Autorrealización (INVERTIDA)
plot_mf(x_mbi,
    [fuzz.trimf(x_mbi,[0,0,2]), fuzz.trimf(x_mbi,[1,3,5]), fuzz.trapmf(x_mbi,[4,5,6,6])],
    ['Frustrado','Satisfecho','Plenamente Realizado'], ['#F44336','#FF9800','#4CAF50'],
    'Autorrealización (MBI - Invertida)', 'Frecuencia (0-6)', '09_autorrealizacion')

# 10. Satisfacción laboral (INVERTIDA)
plot_mf(x_mbi,
    [fuzz.trimf(x_mbi,[0,0,2]), fuzz.trimf(x_mbi,[1,3,5]), fuzz.trapmf(x_mbi,[4,5,6,6])],
    ['Bajo','Medio','Alto'], ['#F44336','#FF9800','#4CAF50'],
    'Nivel de Satisfacción Laboral (MBI - Invertida)', 'Frecuencia (0-6)', '10_satisfaccion_laboral')

# 11. Desconexión mental
plot_mf(x_desc,
    [fuzz.trimf(x_desc,[1,1,2]), fuzz.trimf(x_desc,[1,2,3]), fuzz.trimf(x_desc,[2,3,3])],
    ['Bajo','Medio','Alto'], ['#4CAF50','#FF9800','#F44336'],
    'Desconexión Mental', 'Nivel (1-3)', '11_desconexion_mental')

# 12. Apoyo social percibido (INVERTIDA)
plot_mf(x_apoyo,
    [fuzz.trimf(x_apoyo,[1,1,2]), fuzz.trimf(x_apoyo,[1,2,3]), fuzz.trimf(x_apoyo,[2,3,3])],
    ['Bajo','Medio','Alto'], ['#F44336','#FF9800','#4CAF50'],
    'Apoyo Social Percibido (Invertida)', 'Nivel (1-3)', '12_apoyo_social')

# 13. SALIDA: Riesgo de Burnout
plot_mf(x_riesgo,
    [fuzz.trimf(x_riesgo,[0,0,20]), fuzz.trimf(x_riesgo,[10,25,40]),
     fuzz.trimf(x_riesgo,[30,50,70]), fuzz.trimf(x_riesgo,[60,75,90]),
     fuzz.trapmf(x_riesgo,[80,90,100,100])],
    ['Muy Bajo','Bajo','Moderado','Alto','Crítico'],
    ['#2196F3','#4CAF50','#FFC107','#FF9800','#F44336'],
    'Variable de Salida: Riesgo de Burnout', 'Nivel de Riesgo (%)', '13_riesgo_burnout')

print(f"\n✅ 13 gráficas guardadas en graficas/")
