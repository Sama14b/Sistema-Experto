# PROCESAMIENTO BATCH DEL CSV - SISTEMA EXPERTO BURNOUT
import numpy as np
import skfuzzy as fuzz
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
import re
import os

# 1. Variables y funciones de pertenencia
x_carga = np.arange(1, 11, 1)
x_cal_sueno = np.arange(1, 11, 1)
x_horas_sueno = np.arange(0, 15, 1)
x_estres = np.arange(1, 11, 1)
x_mbi = np.arange(0, 7, 1)
x_desc = np.arange(1, 4, 1)
x_apoyo = np.arange(1, 4, 1)
x_riesgo = np.arange(0, 101, 1)

carga_ligera = fuzz.trimf(x_carga, [1,1,4])
carga_manejable = fuzz.trimf(x_carga, [3,5,7])
carga_abrumadora = fuzz.trapmf(x_carga, [6,8,10,10])
cal_insuficiente = fuzz.trimf(x_cal_sueno, [1,1,3])
cal_pobre = fuzz.trimf(x_cal_sueno, [2,4,6])
cal_aceptable = fuzz.trimf(x_cal_sueno, [5,7,9])
cal_excelente = fuzz.trapmf(x_cal_sueno, [8,9,10,10])
sueno_insuficiente = fuzz.trimf(x_horas_sueno, [0,0,5])
sueno_saludable = fuzz.trimf(x_horas_sueno, [5,7,9])
sueno_prolongado = fuzz.trapmf(x_horas_sueno, [8,10,14,14])
est_bajo = fuzz.trimf(x_estres, [1,1,3])
est_moderado = fuzz.trimf(x_estres, [2,4,6])
est_alto = fuzz.trimf(x_estres, [5,7,9])
est_cronico = fuzz.trapmf(x_estres, [8,9,10,10])
agot_raro = fuzz.trimf(x_mbi, [0,0,2])
agot_ocasional = fuzz.trimf(x_mbi, [1,2.5,4])
agot_frecuente = fuzz.trimf(x_mbi, [3,4,5])
agot_persistente = fuzz.trapmf(x_mbi, [4,5,6,6])
fat_nula = fuzz.trimf(x_mbi, [0,0,2])
fat_leve = fuzz.trimf(x_mbi, [1,3,5])
fat_severa = fuzz.trapmf(x_mbi, [4,5,6,6])
desp_empatico = fuzz.trimf(x_mbi, [0,0,2])
desp_distante = fuzz.trimf(x_mbi, [1,3,5])
desp_cinico = fuzz.trapmf(x_mbi, [4,5,6,6])
util_nulo = fuzz.trimf(x_mbi, [0,0,2])
util_productivo = fuzz.trimf(x_mbi, [1,3,5])
util_muy_valioso = fuzz.trapmf(x_mbi, [4,5,6,6])
auto_frustrado = fuzz.trimf(x_mbi, [0,0,2])
auto_satisfecho = fuzz.trimf(x_mbi, [1,3,5])
auto_plenamente = fuzz.trapmf(x_mbi, [4,5,6,6])
satis_bajo = fuzz.trimf(x_mbi, [0,0,2])
satis_medio = fuzz.trimf(x_mbi, [1,3,5])
satis_alto = fuzz.trapmf(x_mbi, [4,5,6,6])
desc_bajo = fuzz.trimf(x_desc, [1,1,2])
desc_medio = fuzz.trimf(x_desc, [1,2,3])
desc_alto = fuzz.trimf(x_desc, [2,3,3])
apoyo_bajo = fuzz.trimf(x_apoyo, [1,1,2])
apoyo_medio = fuzz.trimf(x_apoyo, [1,2,3])
apoyo_alto = fuzz.trimf(x_apoyo, [2,3,3])
riesgo_muy_bajo = fuzz.trimf(x_riesgo, [0,0,20])
riesgo_bajo = fuzz.trimf(x_riesgo, [10,25,40])
riesgo_moderado = fuzz.trimf(x_riesgo, [30,50,70])
riesgo_alto = fuzz.trimf(x_riesgo, [60,75,90])
riesgo_critico = fuzz.trapmf(x_riesgo, [80,90,100,100])

# 2. Funciones auxiliares
def limpiar_numero(valor):
    match = re.match(r'(\d+)', str(valor).strip())
    return int(match.group(1)) if match else 0

def mapear_desconexion(texto):
    texto = texto.strip().lower()
    if 'nunca' in texto: return 1
    elif 'veces' in texto or 'a veces' in texto: return 2
    else: return 3

def mapear_apoyo(texto):
    texto = texto.strip().lower()
    if 'distante' in texto or 'no' in texto: return 1
    elif 'cordial' in texto: return 2
    else: return 3

def evaluar_burnout(p_carga, p_cal_sueno, p_horas_sueno, p_estres,
                    p_agotamiento, p_fatiga, p_despersonalizacion,
                    p_utilidad, p_autorrealizacion, p_satisfaccion,
                    p_desconexion, p_apoyo):
    f = {}
    f['car_lig'] = fuzz.interp_membership(x_carga, carga_ligera, p_carga)
    f['car_man'] = fuzz.interp_membership(x_carga, carga_manejable, p_carga)
    f['car_abr'] = fuzz.interp_membership(x_carga, carga_abrumadora, p_carga)
    f['cal_ins'] = fuzz.interp_membership(x_cal_sueno, cal_insuficiente, p_cal_sueno)
    f['cal_pob'] = fuzz.interp_membership(x_cal_sueno, cal_pobre, p_cal_sueno)
    f['cal_ace'] = fuzz.interp_membership(x_cal_sueno, cal_aceptable, p_cal_sueno)
    f['cal_exc'] = fuzz.interp_membership(x_cal_sueno, cal_excelente, p_cal_sueno)
    f['sue_ins'] = fuzz.interp_membership(x_horas_sueno, sueno_insuficiente, p_horas_sueno)
    f['sue_sal'] = fuzz.interp_membership(x_horas_sueno, sueno_saludable, p_horas_sueno)
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
    f['dep_emp'] = fuzz.interp_membership(x_mbi, desp_empatico, p_despersonalizacion)
    f['dep_dis'] = fuzz.interp_membership(x_mbi, desp_distante, p_despersonalizacion)
    f['dep_cin'] = fuzz.interp_membership(x_mbi, desp_cinico, p_despersonalizacion)
    f['uti_nul'] = fuzz.interp_membership(x_mbi, util_nulo, p_utilidad)
    f['uti_pro'] = fuzz.interp_membership(x_mbi, util_productivo, p_utilidad)
    f['uti_val'] = fuzz.interp_membership(x_mbi, util_muy_valioso, p_utilidad)
    f['aut_fru'] = fuzz.interp_membership(x_mbi, auto_frustrado, p_autorrealizacion)
    f['aut_sat'] = fuzz.interp_membership(x_mbi, auto_satisfecho, p_autorrealizacion)
    f['aut_ple'] = fuzz.interp_membership(x_mbi, auto_plenamente, p_autorrealizacion)
    f['sat_baj'] = fuzz.interp_membership(x_mbi, satis_bajo, p_satisfaccion)
    f['sat_med'] = fuzz.interp_membership(x_mbi, satis_medio, p_satisfaccion)
    f['sat_alt'] = fuzz.interp_membership(x_mbi, satis_alto, p_satisfaccion)
    f['des_baj'] = fuzz.interp_membership(x_desc, desc_bajo, p_desconexion)
    f['des_med'] = fuzz.interp_membership(x_desc, desc_medio, p_desconexion)
    f['des_alt'] = fuzz.interp_membership(x_desc, desc_alto, p_desconexion)
    f['apo_baj'] = fuzz.interp_membership(x_apoyo, apoyo_bajo, p_apoyo)
    f['apo_med'] = fuzz.interp_membership(x_apoyo, apoyo_medio, p_apoyo)
    f['apo_alt'] = fuzz.interp_membership(x_apoyo, apoyo_alto, p_apoyo)

    # 48 reglas
    r = []
    # Bloque A
    r.append(np.fmin(np.fmin(np.fmin(f['ago_per'], f['car_abr']), f['est_cro']), riesgo_critico))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_per'], f['cal_ins']), f['est_alt']), riesgo_critico))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_fre'], f['est_alt']), f['sue_ins']), riesgo_alto))
    r.append(np.fmin(np.fmin(np.fmin(f['fat_sev'], f['car_abr']), f['cal_pob']), riesgo_alto))
    r.append(np.fmin(np.fmin(f['ago_fre'], f['car_man']), riesgo_moderado))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_oca'], f['est_baj']), f['car_lig']), riesgo_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['fat_nul'], f['cal_exc']), f['est_baj']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(f['est_cro'], f['sue_ins']), riesgo_alto))
    r.append(np.fmin(np.fmin(f['car_man'], f['est_mod']), riesgo_moderado)) # R50
    r.append(np.fmin(np.fmin(f['ago_rar'], f['est_baj']), riesgo_muy_bajo)) # R51
    # Bloque B
    r.append(np.fmin(np.fmin(f['dep_cin'], f['ago_per']), riesgo_critico))
    r.append(np.fmin(np.fmin(f['dep_dis'], f['car_man']), riesgo_moderado))
    r.append(np.fmin(np.fmin(f['dep_emp'], f['est_baj']), riesgo_bajo))
    r.append(np.fmin(np.fmin(f['dep_dis'], f['est_alt']), riesgo_alto))
    # Bloque C
    r.append(np.fmin(np.fmin(f['uti_nul'], f['ago_per']), riesgo_critico))
    r.append(np.fmin(np.fmin(f['aut_fru'], f['est_cro']), riesgo_alto))
    r.append(np.fmin(np.fmin(f['uti_pro'], f['aut_sat']), riesgo_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['uti_val'], f['est_baj']), f['cal_exc']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['aut_sat'], f['car_man']), f['est_mod']), riesgo_moderado))
    r.append(np.fmin(np.fmin(f['aut_sat'], f['ago_oca']), riesgo_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['uti_pro'], f['dep_emp']), f['est_baj']), riesgo_muy_bajo))
    # Bloque D
    r.append(np.fmin(np.fmin(np.fmin(f['ago_per'], f['dep_cin']), f['uti_nul']), riesgo_critico))
    r.append(np.fmin(np.fmin(np.fmin(f['est_cro'], f['car_abr']), f['aut_fru']), riesgo_critico))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_fre'], f['dep_dis']), f['uti_pro']), riesgo_alto))
    r.append(np.fmin(np.fmin(np.fmin(f['car_man'], f['est_mod']), f['aut_sat']), riesgo_moderado))
    r.append(np.fmin(np.fmin(np.fmin(f['sue_sal'], f['cal_ace']), f['est_mod']), riesgo_moderado))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_rar'], f['dep_emp']), f['aut_ple']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_fre'], f['car_abr']), f['cal_pob']), riesgo_alto))
    r.append(np.fmin(np.fmin(np.fmin(f['fat_lev'], f['dep_emp']), f['apo_alt']), riesgo_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['est_alt'], f['sue_ins']), f['ago_fre']), riesgo_alto))
    # Bloque E
    r.append(np.fmin(np.fmin(np.fmin(f['apo_alt'], f['sat_alt']), f['est_mod']), riesgo_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['apo_baj'], f['sat_baj']), f['car_abr']), riesgo_critico))
    r.append(np.fmin(np.fmin(f['des_alt'], f['cal_exc']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(f['des_baj'], f['est_cro']), riesgo_critico))
    r.append(np.fmin(np.fmin(f['sat_alt'], f['ago_fre']), riesgo_moderado))
    r.append(np.fmin(np.fmin(np.fmin(f['apo_med'], f['car_man']), f['des_med']), riesgo_bajo))
    r.append(np.fmin(np.fmin(f['apo_alt'], f['aut_ple']), riesgo_muy_bajo)) # R49
    # Bloque F
    r.append(np.fmin(np.fmin(np.fmin(f['des_baj'], f['cal_pob']), f['fat_sev']), riesgo_critico))
    r.append(np.fmin(np.fmin(np.fmin(f['des_med'], f['cal_ace']), f['sue_sal']), riesgo_moderado))
    r.append(np.fmin(np.fmin(np.fmin(f['des_alt'], f['ago_oca']), f['est_baj']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['sat_baj'], f['des_baj']), f['ago_per']), riesgo_critico))
    r.append(np.fmin(np.fmin(f['cal_ace'], f['ago_oca']), riesgo_bajo))     # R52
    # Bloque G
    r.append(np.fmin(np.fmin(np.fmin(f['car_abr'], f['apo_baj']), f['dep_cin']), riesgo_critico))
    r.append(np.fmin(np.fmin(np.fmin(f['est_alt'], f['sat_baj']), f['uti_nul']), riesgo_critico))
    r.append(np.fmin(np.fmin(np.fmin(f['aut_sat'], f['apo_alt']), f['car_man']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['fat_sev'], f['des_baj']), f['apo_baj']), riesgo_alto))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_fre'], f['sat_med']), f['des_med']), riesgo_alto))
    r.append(np.fmin(np.fmin(np.fmin(f['car_lig'], f['apo_alt']), f['aut_ple']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['est_cro'], f['apo_med']), f['des_baj']), riesgo_alto))
    r.append(np.fmin(np.fmin(np.fmin(f['uti_val'], f['sat_alt']), f['ago_rar']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['dep_dis'], f['sat_baj']), f['apo_baj']), riesgo_alto))
    r.append(np.fmin(np.fmin(np.fmin(f['fat_lev'], f['des_med']), f['sat_med']), riesgo_moderado))
    r.append(np.fmin(np.fmin(f['car_abr'], f['est_mod']), riesgo_alto)) # R53
    r.append(np.fmin(np.fmin(f['ago_fre'], f['est_alt']), riesgo_alto)) # R54
    r.append(np.fmin(np.fmin(f['ago_oca'], f['est_mod']), riesgo_moderado)) # R55
    r.append(np.fmin(np.fmin(f['ago_rar'], f['est_mod']), riesgo_muy_bajo)) # R56

    

    aggregated = np.maximum.reduce(r)
    resultado = fuzz.defuzz(x_riesgo, aggregated, 'centroid')
    if resultado <= 20: nivel = "MUY BAJO"
    elif resultado <= 40: nivel = "BAJO"
    elif resultado <= 60: nivel = "MODERADO"
    elif resultado <= 80: nivel = "ALTO"
    else: nivel = "CRÍTICO"
    return resultado, nivel

# 3. Cargar y procesar CSV
CSV_PATH = 'encuesta.csv'

print("=" * 65)
print("PROCESAMIENTO BATCH - SISTEMA EXPERTO BURNOUT")
print("=" * 65)

resultados = []
with open(CSV_PATH, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for i, row in enumerate(reader):
        try:
            edad = row[1].strip()
            sexo = row[2].strip()
            ocupacion = row[3].strip()
            carga = limpiar_numero(row[5])
            horas_sueno = limpiar_numero(row[6])
            cal_sueno = limpiar_numero(row[7])
            estres = limpiar_numero(row[8])
            agotamiento = limpiar_numero(row[9])
            fatiga = limpiar_numero(row[10])
            despersonalizacion = limpiar_numero(row[12])
            utilidad = limpiar_numero(row[15])
            autorrealizacion = limpiar_numero(row[16])
            # Nuevas variables - ajustar columnas según CSV actualizado
            satisfaccion = limpiar_numero(row[17]) if len(row) > 17 else 3
            desconexion = limpiar_numero(row[18]) if len(row) > 18 else 2
            apoyo = limpiar_numero(row[19]) if len(row) > 19 else 2

            carga = min(max(carga, 1), 10)
            horas_sueno = min(max(horas_sueno, 0), 14)
            cal_sueno = min(max(cal_sueno, 1), 10)
            estres = min(max(estres, 1), 10)
            desconexion = min(max(desconexion, 1), 3)
            apoyo = min(max(apoyo, 1), 3)

            resultado, nivel = evaluar_burnout(
                carga, cal_sueno, horas_sueno, estres,
                agotamiento, fatiga, despersonalizacion,
                utilidad, autorrealizacion, satisfaccion,
                desconexion, apoyo
            )
            resultados.append({'id': i+1, 'edad': edad, 'sexo': sexo,
                             'ocupacion': ocupacion, 'riesgo': resultado, 'nivel': nivel})
            print(f"  Persona {i+1:3d}: {resultado:5.1f}% - {nivel}")
        except Exception as e:
            print(f"Error en fila {i+1}: {e}")

# 4. Guardar resultados
os.makedirs('resultados', exist_ok=True)
with open('resultados/resultados_burnout.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Edad', 'Sexo', 'Ocupación', 'Riesgo (%)', 'Nivel'])
    for r2 in resultados:
        writer.writerow([r2['id'], r2['edad'], r2['sexo'], r2['ocupacion'],
                        f"{r2['riesgo']:.2f}", r2['nivel']])
print(f"\nResultados guardados en resultados/resultados_burnout.csv")

# 5. Estadísticas y visualización
riesgos = [r2['riesgo'] for r2 in resultados]
niveles = [r2['nivel'] for r2 in resultados]
print(f"\n{'=' * 45}")
print(f"  ESTADÍSTICAS ({len(resultados)} respuestas)")
print(f"{'=' * 45}")
print(f"  Media:    {np.mean(riesgos):.2f}%")
print(f"  Mediana:  {np.median(riesgos):.2f}%")
print(f"  Mínimo:   {np.min(riesgos):.2f}%")
print(f"  Máximo:   {np.max(riesgos):.2f}%")
print(f"  Desv.Std: {np.std(riesgos):.2f}%")

cats = ['MUY BAJO', 'BAJO', 'MODERADO', 'ALTO', 'CRÍTICO']
conteo = {c: niveles.count(c) for c in cats}
print(f"\n  Distribución por nivel:")
for c in cats:
    pct = conteo[c] / len(resultados) * 100
    print(f"    {c:10s}: {conteo[c]:3d} ({pct:.1f}%)")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.hist(riesgos, bins=20, color='#FF9800', edgecolor='black', alpha=0.8)
ax1.axvline(np.mean(riesgos), color='red', linestyle='--', linewidth=2, label=f'Media: {np.mean(riesgos):.1f}%')
ax1.set_title('Distribución del Riesgo de Burnout', fontsize=13, fontweight='bold')
ax1.set_xlabel('Riesgo de Burnout (%)')
ax1.set_ylabel('Número de personas')
ax1.legend()

colores_nivel = ['#2196F3', '#4CAF50', '#FFC107', '#FF9800', '#F44336']
barras = ax2.bar(cats, [conteo[c] for c in cats], color=colores_nivel, edgecolor='black')
ax2.set_title('Distribución por Nivel de Riesgo', fontsize=13, fontweight='bold')
ax2.set_ylabel('Número de personas')
for bar, c in zip(barras, cats):
    ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
             str(conteo[c]), ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('resultados/distribucion_burnout.png', dpi=150, bbox_inches='tight')
print(f"\nGráfica guardada en resultados/distribucion_burnout.png")
