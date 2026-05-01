# PROCESAMIENTO BATCH DEL CSV - SISTEMA EXPERTO BURNOUT
import numpy as np
import skfuzzy as fuzz
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
import re
import os

# =============================================================================
# 1. Definición de variables y funciones de pertenencia (idénticas al principal)
# =============================================================================
x_horas_ded = np.arange(0, 17, 1)
x_carga = np.arange(1, 11, 1)
x_horas_sueno = np.arange(0, 15, 1)
x_cal_sueno = np.arange(1, 11, 1)
x_estres = np.arange(1, 11, 1)
x_mbi = np.arange(0, 7, 1)
x_riesgo = np.arange(0, 101, 1)

# Horas dedicación
ded_reducida = fuzz.trimf(x_horas_ded, [0, 0, 5])
ded_estandar = fuzz.trimf(x_horas_ded, [4, 7, 10])
ded_excesiva = fuzz.trapmf(x_horas_ded, [9, 12, 16, 16])

# Carga de trabajo
carga_ligera = fuzz.trimf(x_carga, [1, 1, 4])
carga_manejable = fuzz.trimf(x_carga, [3, 5, 7])
carga_abrumadora = fuzz.trapmf(x_carga, [6, 8, 10, 10])

# Horas de sueño
sueno_insuficiente = fuzz.trimf(x_horas_sueno, [0, 0, 5])
sueno_saludable = fuzz.trimf(x_horas_sueno, [5, 7, 9])
sueno_prolongado = fuzz.trapmf(x_horas_sueno, [8, 10, 14, 14])

# Calidad del sueño
cal_insuficiente = fuzz.trimf(x_cal_sueno, [1, 1, 3])
cal_pobre = fuzz.trimf(x_cal_sueno, [2, 4, 6])
cal_aceptable = fuzz.trimf(x_cal_sueno, [5, 7, 9])
cal_excelente = fuzz.trapmf(x_cal_sueno, [8, 9, 10, 10])

# Estrés
est_bajo = fuzz.trimf(x_estres, [1, 1, 3])
est_moderado = fuzz.trimf(x_estres, [2, 4, 6])
est_alto = fuzz.trimf(x_estres, [5, 7, 9])
est_cronico = fuzz.trapmf(x_estres, [8, 9, 10, 10])

# MBI scales
agot_raro = fuzz.trimf(x_mbi, [0, 0, 2])
agot_ocasional = fuzz.trimf(x_mbi, [1, 2.5, 4])
agot_frecuente = fuzz.trimf(x_mbi, [3, 4, 5])
agot_persistente = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

fat_nula = fuzz.trimf(x_mbi, [0, 0, 2])
fat_leve = fuzz.trimf(x_mbi, [1, 3, 5])
fat_severa = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

sat_controlado = fuzz.trimf(x_mbi, [0, 0, 2])
sat_al_limite = fuzz.trimf(x_mbi, [1, 3, 5])
sat_desbordado = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

desp_empatico = fuzz.trimf(x_mbi, [0, 0, 2])
desp_distante = fuzz.trimf(x_mbi, [1, 3, 5])
desp_cinico = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

ind_comprometido = fuzz.trimf(x_mbi, [0, 0, 2])
ind_despegado = fuzz.trimf(x_mbi, [1, 3, 5])
ind_indiferente = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

desh_humano = fuzz.trimf(x_mbi, [0, 0, 2])
desh_distante = fuzz.trimf(x_mbi, [1, 3, 5])
desh_deshumanizado = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

util_nulo = fuzz.trimf(x_mbi, [0, 0, 2])
util_productivo = fuzz.trimf(x_mbi, [1, 3, 5])
util_muy_valioso = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

auto_frustrado = fuzz.trimf(x_mbi, [0, 0, 2])
auto_satisfecho = fuzz.trimf(x_mbi, [1, 3, 5])
auto_plenamente = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

comp_nula = fuzz.trimf(x_mbi, [0, 0, 2])
comp_adecuada = fuzz.trimf(x_mbi, [1, 3, 5])
comp_destacada = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Salida
riesgo_muy_bajo = fuzz.trimf(x_riesgo, [0, 0, 20])
riesgo_bajo = fuzz.trimf(x_riesgo, [10, 25, 40])
riesgo_moderado = fuzz.trimf(x_riesgo, [30, 50, 70])
riesgo_alto = fuzz.trimf(x_riesgo, [60, 75, 90])
riesgo_critico = fuzz.trapmf(x_riesgo, [80, 90, 100, 100])

# =============================================================================
# 2. Funciones auxiliares
# =============================================================================
def limpiar_numero(valor):
    """Extrae el número de un string como '4h', '7', '5: Varias veces...'"""
    match = re.match(r'(\d+)', str(valor).strip())
    return int(match.group(1)) if match else 0

def mapear_ocupacion(texto):
    """Convierte texto de ocupación a código numérico"""
    texto = texto.strip().lower()
    if 'ambas' in texto:
        return 3
    elif 'trabajo' in texto:
        return 2
    else:
        return 1

def evaluar_burnout(p_horas_ded, p_carga, p_horas_sueno, p_cal_sueno, p_estres,
                    p_agotamiento, p_fatiga, p_saturacion, p_despersonalizacion,
                    p_indiferencia, p_deshumanizacion, p_utilidad,
                    p_autorrealizacion, p_competencia, p_ocupacion):
    """Evalúa el riesgo de burnout para una persona. Retorna (resultado, nivel)."""

    # Fuzzificación
    f = {}
    f['ded_red'] = fuzz.interp_membership(x_horas_ded, ded_reducida, p_horas_ded)
    f['ded_est'] = fuzz.interp_membership(x_horas_ded, ded_estandar, p_horas_ded)
    f['ded_exc'] = fuzz.interp_membership(x_horas_ded, ded_excesiva, p_horas_ded)
    f['car_lig'] = fuzz.interp_membership(x_carga, carga_ligera, p_carga)
    f['car_man'] = fuzz.interp_membership(x_carga, carga_manejable, p_carga)
    f['car_abr'] = fuzz.interp_membership(x_carga, carga_abrumadora, p_carga)
    f['sue_ins'] = fuzz.interp_membership(x_horas_sueno, sueno_insuficiente, p_horas_sueno)
    f['sue_sal'] = fuzz.interp_membership(x_horas_sueno, sueno_saludable, p_horas_sueno)
    f['cal_ins'] = fuzz.interp_membership(x_cal_sueno, cal_insuficiente, p_cal_sueno)
    f['cal_pob'] = fuzz.interp_membership(x_cal_sueno, cal_pobre, p_cal_sueno)
    f['cal_ace'] = fuzz.interp_membership(x_cal_sueno, cal_aceptable, p_cal_sueno)
    f['cal_exc'] = fuzz.interp_membership(x_cal_sueno, cal_excelente, p_cal_sueno)
    f['est_baj'] = fuzz.interp_membership(x_estres, est_bajo, p_estres)
    f['est_mod'] = fuzz.interp_membership(x_estres, est_moderado, p_estres)
    f['est_alt'] = fuzz.interp_membership(x_estres, est_alto, p_estres)
    f['est_cro'] = fuzz.interp_membership(x_estres, est_cronico, p_estres)
    f['ago_rar'] = fuzz.interp_membership(x_mbi, agot_raro, p_agotamiento)
    f['ago_oca'] = fuzz.interp_membership(x_mbi, agot_ocasional, p_agotamiento)
    f['ago_fre'] = fuzz.interp_membership(x_mbi, agot_frecuente, p_agotamiento)
    f['ago_per'] = fuzz.interp_membership(x_mbi, agot_persistente, p_agotamiento)
    f['fat_nul'] = fuzz.interp_membership(x_mbi, fat_nula, p_fatiga)
    f['fat_lev'] = fuzz.interp_membership(x_mbi, fat_leve, p_fatiga)
    f['fat_sev'] = fuzz.interp_membership(x_mbi, fat_severa, p_fatiga)
    f['sat_con'] = fuzz.interp_membership(x_mbi, sat_controlado, p_saturacion)
    f['sat_lim'] = fuzz.interp_membership(x_mbi, sat_al_limite, p_saturacion)
    f['sat_des'] = fuzz.interp_membership(x_mbi, sat_desbordado, p_saturacion)
    f['dep_emp'] = fuzz.interp_membership(x_mbi, desp_empatico, p_despersonalizacion)
    f['dep_dis'] = fuzz.interp_membership(x_mbi, desp_distante, p_despersonalizacion)
    f['dep_cin'] = fuzz.interp_membership(x_mbi, desp_cinico, p_despersonalizacion)
    f['ind_com'] = fuzz.interp_membership(x_mbi, ind_comprometido, p_indiferencia)
    f['ind_dep'] = fuzz.interp_membership(x_mbi, ind_despegado, p_indiferencia)
    f['ind_ind'] = fuzz.interp_membership(x_mbi, ind_indiferente, p_indiferencia)
    f['des_hum'] = fuzz.interp_membership(x_mbi, desh_humano, p_deshumanizacion)
    f['des_dis'] = fuzz.interp_membership(x_mbi, desh_distante, p_deshumanizacion)
    f['des_des'] = fuzz.interp_membership(x_mbi, desh_deshumanizado, p_deshumanizacion)
    f['uti_nul'] = fuzz.interp_membership(x_mbi, util_nulo, p_utilidad)
    f['uti_pro'] = fuzz.interp_membership(x_mbi, util_productivo, p_utilidad)
    f['uti_val'] = fuzz.interp_membership(x_mbi, util_muy_valioso, p_utilidad)
    f['aut_fru'] = fuzz.interp_membership(x_mbi, auto_frustrado, p_autorrealizacion)
    f['aut_sat'] = fuzz.interp_membership(x_mbi, auto_satisfecho, p_autorrealizacion)
    f['aut_ple'] = fuzz.interp_membership(x_mbi, auto_plenamente, p_autorrealizacion)
    f['com_nul'] = fuzz.interp_membership(x_mbi, comp_nula, p_competencia)
    f['com_ade'] = fuzz.interp_membership(x_mbi, comp_adecuada, p_competencia)
    f['com_des'] = fuzz.interp_membership(x_mbi, comp_destacada, p_competencia)

    # 50 Reglas de inferencia
    rules = []
    # Bloque A
    rules.append(np.fmin(np.fmin(np.fmin(f['ago_per'], f['car_abr']), f['est_cro']), riesgo_critico))
    rules.append(np.fmin(np.fmin(np.fmin(f['fat_sev'], f['sat_des']), f['ded_exc']), riesgo_critico))
    rules.append(np.fmin(np.fmin(np.fmin(f['ago_per'], f['cal_ins']), f['est_alt']), riesgo_critico))
    rules.append(np.fmin(np.fmin(f['sat_des'], f['car_abr']), riesgo_alto))
    rules.append(np.fmin(np.fmin(np.fmin(f['ago_fre'], f['est_alt']), f['sue_ins']), riesgo_alto))
    rules.append(np.fmin(np.fmin(np.fmin(f['fat_sev'], f['car_abr']), f['cal_pob']), riesgo_alto))
    rules.append(np.fmin(np.fmin(f['ago_fre'], f['car_man']), riesgo_moderado))
    rules.append(np.fmin(np.fmin(np.fmin(f['est_mod'], f['fat_lev']), f['sat_lim']), riesgo_moderado))
    rules.append(np.fmin(np.fmin(f['ded_exc'], f['cal_ace']), riesgo_moderado))
    rules.append(np.fmin(np.fmin(np.fmin(f['ago_oca'], f['est_baj']), f['car_lig']), riesgo_bajo))
    rules.append(np.fmin(np.fmin(np.fmin(f['fat_nul'], f['cal_exc']), f['est_baj']), riesgo_muy_bajo))
    rules.append(np.fmin(np.fmin(np.fmin(f['ago_rar'], f['sat_con']), f['sue_sal']), riesgo_muy_bajo))
    rules.append(np.fmin(np.fmin(np.fmin(f['ded_est'], f['car_lig']), f['cal_exc']), riesgo_muy_bajo))
    rules.append(np.fmin(np.fmin(f['est_cro'], f['sue_ins']), riesgo_alto))
    rules.append(np.fmin(np.fmin(f['car_abr'], f['ded_exc']), riesgo_alto))
    # Bloque B
    rules.append(np.fmin(np.fmin(np.fmin(f['dep_cin'], f['ind_ind']), f['des_des']), riesgo_critico))
    rules.append(np.fmin(np.fmin(f['dep_cin'], f['ago_per']), riesgo_critico))
    rules.append(np.fmin(np.fmin(f['ind_ind'], f['sat_des']), riesgo_alto))
    rules.append(np.fmin(np.fmin(f['des_des'], f['est_alt']), riesgo_alto))
    rules.append(np.fmin(np.fmin(f['dep_dis'], f['ind_dep']), riesgo_moderado))
    rules.append(np.fmin(np.fmin(f['des_dis'], f['car_man']), riesgo_moderado))
    rules.append(np.fmin(np.fmin(f['dep_emp'], f['ind_com']), riesgo_bajo))
    rules.append(np.fmin(np.fmin(np.fmin(f['des_hum'], f['dep_emp']), f['ind_com']), riesgo_muy_bajo))
    rules.append(np.fmin(np.fmin(np.fmin(f['ind_ind'], f['car_abr']), f['fat_sev']), riesgo_critico))
    rules.append(np.fmin(np.fmin(f['dep_dis'], f['est_alt']), riesgo_alto))
    # Bloque C
    rules.append(np.fmin(np.fmin(np.fmin(f['uti_nul'], f['aut_fru']), f['com_nul']), riesgo_critico))
    rules.append(np.fmin(np.fmin(f['uti_nul'], f['ago_per']), riesgo_critico))
    rules.append(np.fmin(np.fmin(f['aut_fru'], f['est_cro']), riesgo_alto))
    rules.append(np.fmin(np.fmin(f['com_nul'], f['sat_des']), riesgo_alto))
    rules.append(np.fmin(np.fmin(f['uti_pro'], f['aut_sat']), riesgo_bajo))
    rules.append(np.fmin(np.fmin(f['com_des'], f['aut_ple']), riesgo_muy_bajo))
    rules.append(np.fmin(np.fmin(np.fmin(f['uti_val'], f['est_baj']), f['cal_exc']), riesgo_muy_bajo))
    rules.append(np.fmin(np.fmin(np.fmin(f['aut_sat'], f['car_man']), f['est_mod']), riesgo_moderado))
    rules.append(np.fmin(np.fmin(f['com_ade'], f['ago_oca']), riesgo_bajo))
    rules.append(np.fmin(np.fmin(np.fmin(f['uti_pro'], f['dep_emp']), f['est_baj']), riesgo_muy_bajo))
    # Bloque D
    rules.append(np.fmin(np.fmin(np.fmin(f['ago_per'], f['dep_cin']), f['uti_nul']), riesgo_critico))
    rules.append(np.fmin(np.fmin(np.fmin(f['est_cro'], f['car_abr']), f['aut_fru']), riesgo_critico))
    rules.append(np.fmin(np.fmin(np.fmin(f['sat_des'], f['des_des']), f['com_nul']), riesgo_critico))
    rules.append(np.fmin(np.fmin(np.fmin(f['ago_fre'], f['dep_dis']), f['uti_pro']), riesgo_alto))
    rules.append(np.fmin(np.fmin(np.fmin(f['car_man'], f['est_mod']), f['aut_sat']), riesgo_moderado))
    rules.append(np.fmin(np.fmin(np.fmin(f['sue_sal'], f['cal_ace']), f['est_mod']), riesgo_moderado))
    rules.append(np.fmin(np.fmin(np.fmin(f['ago_rar'], f['dep_emp']), f['com_des']), riesgo_muy_bajo))
    rules.append(np.fmin(np.fmin(np.fmin(f['fat_nul'], f['ind_com']), f['aut_ple']), riesgo_muy_bajo))
    rules.append(np.fmin(np.fmin(f['ded_est'], f['car_man']), np.fmin(np.fmin(f['est_baj'], f['cal_ace']), riesgo_bajo)))
    # R45-R46: Modificador contextual ocupación
    if p_ocupacion == 3:
        rules.append(np.fmin(np.fmin(f['ago_fre'], f['car_abr']), riesgo_critico))
        rules.append(np.fmin(np.fmin(f['est_alt'], f['ded_exc']), riesgo_critico))
    else:
        rules.append(np.zeros_like(x_riesgo))
        rules.append(np.zeros_like(x_riesgo))
    rules.append(np.fmin(np.fmin(np.fmin(f['fat_lev'], f['dep_emp']), f['com_ade']), riesgo_bajo))
    rules.append(np.fmin(np.fmin(np.fmin(f['est_alt'], f['sue_ins']), f['ago_fre']), riesgo_alto))
    rules.append(np.fmin(np.fmin(np.fmin(f['cal_ins'], f['car_abr']), f['sat_des']), riesgo_critico))
    rules.append(np.fmin(np.fmin(f['ded_red'], f['est_baj']), np.fmin(np.fmin(f['aut_ple'], f['cal_exc']), riesgo_muy_bajo)))

    # Agregación y defuzzificación
    aggregated = np.maximum.reduce(rules)
    resultado = fuzz.defuzz(x_riesgo, aggregated, 'centroid')

    if resultado <= 20: nivel = "MUY BAJO"
    elif resultado <= 40: nivel = "BAJO"
    elif resultado <= 60: nivel = "MODERADO"
    elif resultado <= 80: nivel = "ALTO"
    else: nivel = "CRÍTICO"

    return resultado, nivel

# =============================================================================
# 3. Cargar y procesar CSV
# =============================================================================
CSV_PATH = 'Encuesta sobre Bienestar y Carga de Trabajo .csv'

print("=" * 65)
print("   PROCESAMIENTO BATCH - SISTEMA EXPERTO BURNOUT")
print("=" * 65)

resultados = []

with open(CSV_PATH, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Saltar cabecera

    for i, row in enumerate(reader):
        try:
            edad = row[1].strip()
            sexo = row[2].strip()
            ocupacion = mapear_ocupacion(row[3])
            horas_ded = limpiar_numero(row[4])
            carga = limpiar_numero(row[5])
            horas_sueno = limpiar_numero(row[6])
            cal_sueno = limpiar_numero(row[7])
            estres = limpiar_numero(row[8])
            agotamiento = limpiar_numero(row[9])
            fatiga = limpiar_numero(row[10])
            saturacion = limpiar_numero(row[11])
            despersonalizacion = limpiar_numero(row[12])
            indiferencia = limpiar_numero(row[13])
            deshumanizacion = limpiar_numero(row[14])
            utilidad = limpiar_numero(row[15])
            autorrealizacion = limpiar_numero(row[16])
            competencia = limpiar_numero(row[17])

            # Limitar valores a rangos válidos
            horas_ded = min(max(horas_ded, 0), 16)
            carga = min(max(carga, 1), 10)
            horas_sueno = min(max(horas_sueno, 0), 14)
            cal_sueno = min(max(cal_sueno, 1), 10)
            estres = min(max(estres, 1), 10)

            resultado, nivel = evaluar_burnout(
                horas_ded, carga, horas_sueno, cal_sueno, estres,
                agotamiento, fatiga, saturacion, despersonalizacion,
                indiferencia, deshumanizacion, utilidad,
                autorrealizacion, competencia, ocupacion
            )

            resultados.append({
                'id': i + 1, 'edad': edad, 'sexo': sexo,
                'ocupacion': row[3].strip(), 'riesgo': resultado, 'nivel': nivel
            })
            print(f"  Persona {i+1:3d}: {resultado:5.1f}% - {nivel}")

        except Exception as e:
            print(f"  ⚠ Error en fila {i+1}: {e}")

# =============================================================================
# 4. Guardar resultados en CSV
# =============================================================================
os.makedirs('resultados', exist_ok=True)

with open('resultados/resultados_burnout.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Edad', 'Sexo', 'Ocupación', 'Riesgo (%)', 'Nivel'])
    for r in resultados:
        writer.writerow([r['id'], r['edad'], r['sexo'], r['ocupacion'],
                        f"{r['riesgo']:.2f}", r['nivel']])

print(f"\n✅ Resultados guardados en resultados/resultados_burnout.csv")

# =============================================================================
# 5. Estadísticas y visualización
# =============================================================================
riesgos = [r['riesgo'] for r in resultados]
niveles = [r['nivel'] for r in resultados]

print(f"\n{'=' * 45}")
print(f"  ESTADÍSTICAS ({len(resultados)} respuestas)")
print(f"{'=' * 45}")
print(f"  Media:    {np.mean(riesgos):.2f}%")
print(f"  Mediana:  {np.median(riesgos):.2f}%")
print(f"  Mínimo:   {np.min(riesgos):.2f}%")
print(f"  Máximo:   {np.max(riesgos):.2f}%")
print(f"  Desv.Std: {np.std(riesgos):.2f}%")

# Conteo por nivel
cats = ['MUY BAJO', 'BAJO', 'MODERADO', 'ALTO', 'CRÍTICO']
conteo = {c: niveles.count(c) for c in cats}
print(f"\n  Distribución por nivel:")
for c in cats:
    pct = conteo[c] / len(resultados) * 100
    print(f"    {c:10s}: {conteo[c]:3d} ({pct:.1f}%)")

# Histograma
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Histograma de riesgo
ax1.hist(riesgos, bins=20, color='#FF9800', edgecolor='black', alpha=0.8)
ax1.axvline(np.mean(riesgos), color='red', linestyle='--', linewidth=2, label=f'Media: {np.mean(riesgos):.1f}%')
ax1.set_title('Distribución del Riesgo de Burnout', fontsize=13, fontweight='bold')
ax1.set_xlabel('Riesgo de Burnout (%)')
ax1.set_ylabel('Número de personas')
ax1.legend()

# Gráfico de barras por nivel
colores_nivel = ['#2196F3', '#4CAF50', '#FFC107', '#FF9800', '#F44336']
barras = ax2.bar(cats, [conteo[c] for c in cats], color=colores_nivel, edgecolor='black')
ax2.set_title('Distribución por Nivel de Riesgo', fontsize=13, fontweight='bold')
ax2.set_ylabel('Número de personas')
for bar, c in zip(barras, cats):
    ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
             str(conteo[c]), ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('resultados/distribucion_burnout.png', dpi=150, bbox_inches='tight')
plt.show()
print(f"\n✅ Gráfica guardada en resultados/distribucion_burnout.png")
