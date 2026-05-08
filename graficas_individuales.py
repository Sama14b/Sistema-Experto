# GENERACIÓN DE GRÁFICAS INDIVIDUALES - PERSONA 2 Y PERSONA 27
import numpy as np
import skfuzzy as fuzz
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

os.makedirs('graficas', exist_ok=True)

# 1. Variables y funciones de pertenencia (Copiadas de burnout_batch.py para consistencia)
x_carga = np.arange(1, 11, 1)
x_cal_sueno = np.arange(1, 11, 1)
x_horas_sueno = np.arange(0, 15, 1)
x_estres = np.arange(1, 11, 1)
x_ae = np.arange(0, 19, 1)    
x_dp = np.arange(0, 19, 1)    
x_rp = np.arange(0, 25, 1)    
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
agot_raro = fuzz.trimf(x_ae, [0,0,6])
agot_ocasional = fuzz.trimf(x_ae, [3,7,12])
agot_frecuente = fuzz.trimf(x_ae, [9,13,16])
agot_persistente = fuzz.trapmf(x_ae, [13,16,18,18])
fat_nula = fuzz.trimf(x_ae, [0,0,6])
fat_leve = fuzz.trimf(x_ae, [3,9,15])
fat_severa = fuzz.trapmf(x_ae, [12,15,18,18])
desp_empatico = fuzz.trimf(x_dp, [0,0,6])
desp_distante = fuzz.trimf(x_dp, [3,9,15])
desp_cinico = fuzz.trapmf(x_dp, [12,15,18,18])
util_nulo = fuzz.trimf(x_rp, [0,0,10])
util_productivo = fuzz.trimf(x_rp, [8,14,20])
util_muy_valioso = fuzz.trapmf(x_rp, [16,20,24,24])
auto_frustrado = fuzz.trimf(x_rp, [0,0,10])
auto_satisfecho = fuzz.trimf(x_rp, [8,14,20])
auto_plenamente = fuzz.trapmf(x_rp, [16,20,24,24])
satis_bajo = fuzz.trimf(x_rp, [0,0,10])
satis_medio = fuzz.trimf(x_rp, [8,14,20])
satis_alto = fuzz.trapmf(x_rp, [16,20,24,24])
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

def graficar_resultado_individual(p_carga, p_cal_sueno, p_horas_sueno, p_estres,
                                 p_agotamiento, p_fatiga, p_saturacion,
                                 p_despersonalizacion, p_indiferencia, p_deshumanizacion,
                                 p_utilidad, p_autorrealizacion, p_satisfaccion, p_competencia,
                                 p_desconexion, p_apoyo, filename, titulo_p):
    
    # subescalas MBI
    ae = p_agotamiento + p_fatiga + p_saturacion         
    dp = p_despersonalizacion + p_indiferencia + p_deshumanizacion  
    rp = p_utilidad + p_autorrealizacion + p_satisfaccion + p_competencia  

    # fuzzificación
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
    f['ago_rar'] = fuzz.interp_membership(x_ae, agot_raro, ae)
    f['ago_oca'] = fuzz.interp_membership(x_ae, agot_ocasional, ae)
    f['ago_fre'] = fuzz.interp_membership(x_ae, agot_frecuente, ae)
    f['ago_per'] = fuzz.interp_membership(x_ae, agot_persistente, ae)
    f['fat_nul'] = fuzz.interp_membership(x_ae, fat_nula, ae)
    f['fat_lev'] = fuzz.interp_membership(x_ae, fat_leve, ae)
    f['fat_sev'] = fuzz.interp_membership(x_ae, fat_severa, ae)
    f['dep_emp'] = fuzz.interp_membership(x_dp, desp_empatico, dp)
    f['dep_dis'] = fuzz.interp_membership(x_dp, desp_distante, dp)
    f['dep_cin'] = fuzz.interp_membership(x_dp, desp_cinico, dp)
    f['uti_nul'] = fuzz.interp_membership(x_rp, util_nulo, rp)
    f['uti_pro'] = fuzz.interp_membership(x_rp, util_productivo, rp)
    f['uti_val'] = fuzz.interp_membership(x_rp, util_muy_valioso, rp)
    f['aut_fru'] = fuzz.interp_membership(x_rp, auto_frustrado, rp)
    f['aut_sat'] = fuzz.interp_membership(x_rp, auto_satisfecho, rp)
    f['aut_ple'] = fuzz.interp_membership(x_rp, auto_plenamente, rp)
    f['sat_baj'] = fuzz.interp_membership(x_rp, satis_bajo, rp)
    f['sat_med'] = fuzz.interp_membership(x_rp, satis_medio, rp)
    f['sat_alt'] = fuzz.interp_membership(x_rp, satis_alto, rp)
    f['des_baj'] = fuzz.interp_membership(x_desc, desc_bajo, p_desconexion)
    f['des_med'] = fuzz.interp_membership(x_desc, desc_medio, p_desconexion)
    f['des_alt'] = fuzz.interp_membership(x_desc, desc_alto, p_desconexion)
    f['apo_baj'] = fuzz.interp_membership(x_apoyo, apoyo_bajo, p_apoyo)
    f['apo_med'] = fuzz.interp_membership(x_apoyo, apoyo_medio, p_apoyo)
    f['apo_alt'] = fuzz.interp_membership(x_apoyo, apoyo_alto, p_apoyo)

    # inferencia
    r = []
    # (Reglas R1 a R56 - Mismas que burnout_batch.py)
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
    r.append(np.fmin(np.fmin(f['dep_cin'], f['ago_per']), riesgo_critico))
    r.append(np.fmin(np.fmin(f['dep_dis'], f['car_man']), riesgo_moderado))
    r.append(np.fmin(np.fmin(f['dep_emp'], f['est_baj']), riesgo_bajo))
    r.append(np.fmin(np.fmin(f['dep_dis'], f['est_alt']), riesgo_alto))
    r.append(np.fmin(np.fmin(f['uti_nul'], f['ago_per']), riesgo_critico))
    r.append(np.fmin(np.fmin(f['aut_fru'], f['est_cro']), riesgo_alto))
    r.append(np.fmin(np.fmin(f['uti_pro'], f['aut_sat']), riesgo_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['uti_val'], f['est_baj']), f['cal_exc']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['aut_sat'], f['car_man']), f['est_mod']), riesgo_moderado))
    r.append(np.fmin(np.fmin(f['aut_sat'], f['ago_oca']), riesgo_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['uti_pro'], f['dep_emp']), f['est_baj']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_per'], f['dep_cin']), f['uti_nul']), riesgo_critico))
    r.append(np.fmin(np.fmin(np.fmin(f['est_cro'], f['car_abr']), f['aut_fru']), riesgo_critico))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_fre'], f['dep_dis']), f['uti_pro']), riesgo_alto))
    r.append(np.fmin(np.fmin(np.fmin(f['car_man'], f['est_mod']), f['aut_sat']), riesgo_moderado))
    r.append(np.fmin(np.fmin(np.fmin(f['sue_sal'], f['cal_ace']), f['est_mod']), riesgo_moderado))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_rar'], f['dep_emp']), f['aut_ple']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['ago_fre'], f['car_abr']), f['cal_pob']), riesgo_alto))
    r.append(np.fmin(np.fmin(np.fmin(f['fat_lev'], f['dep_emp']), f['apo_alt']), riesgo_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['est_alt'], f['sue_ins']), f['ago_fre']), riesgo_alto))
    r.append(np.fmin(np.fmin(np.fmin(f['apo_alt'], f['sat_alt']), f['est_mod']), riesgo_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['apo_baj'], f['sat_baj']), f['car_abr']), riesgo_critico))
    r.append(np.fmin(np.fmin(f['des_alt'], f['cal_exc']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(f['des_baj'], f['est_cro']), riesgo_critico))
    r.append(np.fmin(np.fmin(f['sat_alt'], f['ago_fre']), riesgo_moderado))
    r.append(np.fmin(np.fmin(np.fmin(f['apo_med'], f['car_man']), f['des_med']), riesgo_bajo))
    r.append(np.fmin(np.fmin(f['apo_alt'], f['aut_ple']), riesgo_muy_bajo)) # R49
    r.append(np.fmin(np.fmin(np.fmin(f['des_baj'], f['cal_pob']), f['fat_sev']), riesgo_critico))
    r.append(np.fmin(np.fmin(np.fmin(f['des_med'], f['cal_ace']), f['sue_sal']), riesgo_moderado))
    r.append(np.fmin(np.fmin(np.fmin(f['des_alt'], f['ago_oca']), f['est_baj']), riesgo_muy_bajo))
    r.append(np.fmin(np.fmin(np.fmin(f['sat_baj'], f['des_baj']), f['ago_per']), riesgo_critico))
    r.append(np.fmin(np.fmin(f['cal_ace'], f['ago_oca']), riesgo_bajo))     # R52
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
    grado_riesgo = fuzz.interp_membership(x_riesgo, aggregated, resultado)

    if resultado <= 20: nivel = "MUY BAJO"
    elif resultado <= 40: nivel = "BAJO"
    elif resultado <= 60: nivel = "MODERADO"
    elif resultado <= 80: nivel = "ALTO"
    else: nivel = "CRÍTICO"

    # Gráfica
    fig, ax0 = plt.subplots(figsize=(10, 4))
    ax0.plot(x_riesgo, riesgo_muy_bajo, 'b', linestyle='--', label='Muy Bajo')
    ax0.plot(x_riesgo, riesgo_bajo, 'c', linestyle='--', label='Bajo')
    ax0.plot(x_riesgo, riesgo_moderado, 'orange', linestyle='--', label='Moderado')
    ax0.plot(x_riesgo, riesgo_alto, 'r', linestyle='--', label='Alto')
    ax0.plot(x_riesgo, riesgo_critico, 'm', linestyle='--', label='Crítico')
    ax0.fill_between(x_riesgo, np.zeros_like(x_riesgo), aggregated, facecolor='#FF9800', alpha=0.7)
    ax0.plot([resultado, resultado], [0, grado_riesgo], 'k', linewidth=2, alpha=0.9)
    ax0.set_title(f'{titulo_p}: {resultado:.2f}% ({nivel})', fontsize=14, fontweight='bold')
    ax0.set_xlabel('Nivel de Riesgo (%)')
    ax0.set_ylabel('Grado de Pertenencia')
    ax0.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(f'graficas/{filename}.png', dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  ✓ {filename}.png (Resultado: {resultado:.2f}%)")

print("Generando gráficas de resultados individuales...\n")

# DATOS PERSONA 2 (Result: 25.00%)
# Inputs: 7, 6, 6, 6, 3, 3, 2, 2, 1, 0, 2, 1, 5, 2, 3, 3
graficar_resultado_individual(7, 6, 6, 6, 3, 3, 2, 2, 1, 0, 2, 1, 5, 2, 3, 3, 'resultado_persona_2', 'Riesgo Burnout: Persona 2')

# DATOS PERSONA 27 (Result: 67.46%)
# Inputs: 6, 7, 6, 8, 4, 5, 4, 3, 0, 1, 1, 1, 2, 1, 3, 1
graficar_resultado_individual(6, 7, 6, 8, 4, 5, 4, 3, 0, 1, 1, 1, 2, 1, 3, 1, 'resultado_persona_27', 'Riesgo Burnout: Persona 27')

print("\nGráficas individuales generadas correctamente.")
