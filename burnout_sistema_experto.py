# SISTEMA EXPERTO DIFUSO - DETECCIÓN DE RIESGO DE BURNOUT
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# 1. UNIVERSOS DE DISCURSO
x_carga = np.arange(1, 11, 1)            # Carga de trabajo percibida (1-10)
x_cal_sueno = np.arange(1, 11, 1)        # Calidad del sueño (1-10)
x_horas_sueno = np.arange(0, 15, 1)      # Horas de sueño (0-14)
x_estres = np.arange(1, 11, 1)           # Estrés diario (1-10)

x_mbi = np.arange(0, 7, 1)              # Escala MBI (0-6)
x_desc = np.arange(1, 4, 1)             # Desconexión mental (1-3)
x_apoyo = np.arange(1, 4, 1)            # Apoyo social percibido (1-3)
x_riesgo = np.arange(0, 101, 1)          # SALIDA: riesgo burnout (0-100)

# 2. FUNCIONES DE PERTENENCIA

# Carga de trabajo percibida (1-10)
carga_ligera = fuzz.trimf(x_carga, [1, 1, 4])
carga_manejable = fuzz.trimf(x_carga, [3, 5, 7])
carga_abrumadora = fuzz.trapmf(x_carga, [6, 8, 10, 10])

# Calidad del sueño (1-10)
cal_insuficiente = fuzz.trimf(x_cal_sueno, [1, 1, 3])
cal_pobre = fuzz.trimf(x_cal_sueno, [2, 4, 6])
cal_aceptable = fuzz.trimf(x_cal_sueno, [5, 7, 9])
cal_excelente = fuzz.trapmf(x_cal_sueno, [8, 9, 10, 10])

# Horas de sueño (0-14)
sueno_insuficiente = fuzz.trimf(x_horas_sueno, [0, 0, 5])
sueno_saludable = fuzz.trimf(x_horas_sueno, [5, 7, 9])
sueno_prolongado = fuzz.trapmf(x_horas_sueno, [8, 10, 14, 14])

# Estrés diario (1-10)
est_bajo = fuzz.trimf(x_estres, [1, 1, 3])
est_moderado = fuzz.trimf(x_estres, [2, 4, 6])
est_alto = fuzz.trimf(x_estres, [5, 7, 9])
est_cronico = fuzz.trapmf(x_estres, [8, 9, 10, 10])



# Agotamiento emocional (MBI 0-6)
agot_raro = fuzz.trimf(x_mbi, [0, 0, 2])
agot_ocasional = fuzz.trimf(x_mbi, [1, 2.5, 4])
agot_frecuente = fuzz.trimf(x_mbi, [3, 4, 5])
agot_persistente = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Fatiga anticipatoria (MBI 0-6)
fat_nula = fuzz.trimf(x_mbi, [0, 0, 2])
fat_leve = fuzz.trimf(x_mbi, [1, 3, 5])
fat_severa = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Despersonalización / Cinismo (MBI 0-6)
desp_empatico = fuzz.trimf(x_mbi, [0, 0, 2])
desp_distante = fuzz.trimf(x_mbi, [1, 3, 5])
desp_cinico = fuzz.trapmf(x_mbi, [4, 5, 6, 6])



# Percepción de utilidad (MBI 0-6, INVERTIDA)
util_nulo = fuzz.trimf(x_mbi, [0, 0, 2])
util_productivo = fuzz.trimf(x_mbi, [1, 3, 5])
util_muy_valioso = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Autorrealización (MBI 0-6, INVERTIDA)
auto_frustrado = fuzz.trimf(x_mbi, [0, 0, 2])
auto_satisfecho = fuzz.trimf(x_mbi, [1, 3, 5])
auto_plenamente = fuzz.trapmf(x_mbi, [4, 5, 6, 6])



# Satisfacción laboral (MBI 0-6, INVERTIDA)
satis_bajo = fuzz.trimf(x_mbi, [0, 0, 2])
satis_medio = fuzz.trimf(x_mbi, [1, 3, 5])
satis_alto = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Desconexión mental (1-3)
desc_bajo = fuzz.trimf(x_desc, [1, 1, 2])
desc_medio = fuzz.trimf(x_desc, [1, 2, 3])
desc_alto = fuzz.trimf(x_desc, [2, 3, 3])

# Apoyo social percibido (1-3, INVERTIDA)
apoyo_bajo = fuzz.trimf(x_apoyo, [1, 1, 2])
apoyo_medio = fuzz.trimf(x_apoyo, [1, 2, 3])
apoyo_alto = fuzz.trimf(x_apoyo, [2, 3, 3])

# VARIABLE DE SALIDA: Riesgo de Burnout (0-100)
riesgo_muy_bajo = fuzz.trimf(x_riesgo, [0, 0, 20])
riesgo_bajo = fuzz.trimf(x_riesgo, [10, 25, 40])
riesgo_moderado = fuzz.trimf(x_riesgo, [30, 50, 70])
riesgo_alto = fuzz.trimf(x_riesgo, [60, 75, 90])
riesgo_critico = fuzz.trapmf(x_riesgo, [80, 90, 100, 100])

# 3. ENTRADA DEL USUARIO
print("=" * 65)
print("   SISTEMA EXPERTO: DETECCIÓN DE RIESGO DE BURNOUT")
print("=" * 65)
print("\nResponde con sinceridad basándote en tu rutina actual.\n")

# Variables demográficas
print("1: 18-22 años | 2: 23-30 años | 3: Más de 30 años")
p_edad = int(input("¿Qué edad tienes? (1/2/3): "))

print("\n1: Mujer | 2: Hombre")
p_sexo = int(input("Sexo (1/2): "))

print("\n1: Estudio | 2: Trabajo | 3: Ambas")
p_ocupacion = int(input("Ocupación actual (1/2/3): "))

# Variables difusas continuas

p_carga = int(input("¿Cómo de alta percibes tu carga de trabajo? (1-10): "))
p_horas_sueno = int(input("¿Cuántas horas duermes de media al día?: "))
p_cal_sueno = int(input("¿Cómo valorarías la calidad de tu sueño? (1-10): "))
p_estres = int(input("¿Cuánto estrés sientes en tu día a día? (1-10): "))

# Preguntas MBI (0-6)
print("\nIndica la frecuencia (0-6):")
print("  0: Nunca | 1: Pocas veces al año | 2: Una vez al mes o menos")
print("  3: Unas pocas veces al mes | 4: Una vez a la semana")
print("  5: Varias veces a la semana | 6: Todos los días\n")

p_agotamiento = int(input("Me siento emocionalmente agotado (0-6): "))
p_fatiga = int(input("Me siento cansado al empezar el día (0-6): "))
p_despersonalizacion = int(input("Me estoy volviendo más frío o distante (0-6): "))

p_utilidad = int(input("Siento que hago cosas útiles y valiosas (0-6): "))
p_autorrealizacion = int(input("Me siento realizado con lo que hago (0-6): "))

p_satisfaccion = int(input("Estoy satisfecho en mi entorno laboral (0-6): "))

# Desconexión mental (1-3)
print("\n¿Sigues pensando en tareas pendientes fuera de tu jornada?")
print("  1: Nunca o casi nunca")
print("  2: A veces, especialmente en días de mucha carga")
print("  3: Siempre o casi siempre")
p_desconexion = int(input("Opción (1/2/3): "))

# Apoyo social percibido (1-3)
print("\n¿Sientes que tus compañeros/supervisores se preocupan por tu bienestar?")
print("  1: No, el trato es distante")
print("  2: Trato cordial, pero sin apoyo emocional profundo")
print("  3: Sí, me siento valorado y respaldado")
p_apoyo = int(input("Opción (1/2/3): "))

# 4. FUZZIFICACIÓN
f_car_lig = fuzz.interp_membership(x_carga, carga_ligera, p_carga)
f_car_man = fuzz.interp_membership(x_carga, carga_manejable, p_carga)
f_car_abr = fuzz.interp_membership(x_carga, carga_abrumadora, p_carga)

f_cal_ins = fuzz.interp_membership(x_cal_sueno, cal_insuficiente, p_cal_sueno)
f_cal_pob = fuzz.interp_membership(x_cal_sueno, cal_pobre, p_cal_sueno)
f_cal_ace = fuzz.interp_membership(x_cal_sueno, cal_aceptable, p_cal_sueno)
f_cal_exc = fuzz.interp_membership(x_cal_sueno, cal_excelente, p_cal_sueno)

f_sue_ins = fuzz.interp_membership(x_horas_sueno, sueno_insuficiente, p_horas_sueno)
f_sue_sal = fuzz.interp_membership(x_horas_sueno, sueno_saludable, p_horas_sueno)
f_sue_pro = fuzz.interp_membership(x_horas_sueno, sueno_prolongado, p_horas_sueno)

f_est_baj = fuzz.interp_membership(x_estres, est_bajo, p_estres)
f_est_mod = fuzz.interp_membership(x_estres, est_moderado, p_estres)
f_est_alt = fuzz.interp_membership(x_estres, est_alto, p_estres)
f_est_cro = fuzz.interp_membership(x_estres, est_cronico, p_estres)



f_ago_rar = fuzz.interp_membership(x_mbi, agot_raro, p_agotamiento)
f_ago_oca = fuzz.interp_membership(x_mbi, agot_ocasional, p_agotamiento)
f_ago_fre = fuzz.interp_membership(x_mbi, agot_frecuente, p_agotamiento)
f_ago_per = fuzz.interp_membership(x_mbi, agot_persistente, p_agotamiento)

f_fat_nul = fuzz.interp_membership(x_mbi, fat_nula, p_fatiga)
f_fat_lev = fuzz.interp_membership(x_mbi, fat_leve, p_fatiga)
f_fat_sev = fuzz.interp_membership(x_mbi, fat_severa, p_fatiga)

f_dep_emp = fuzz.interp_membership(x_mbi, desp_empatico, p_despersonalizacion)
f_dep_dis = fuzz.interp_membership(x_mbi, desp_distante, p_despersonalizacion)
f_dep_cin = fuzz.interp_membership(x_mbi, desp_cinico, p_despersonalizacion)



f_uti_nul = fuzz.interp_membership(x_mbi, util_nulo, p_utilidad)
f_uti_pro = fuzz.interp_membership(x_mbi, util_productivo, p_utilidad)
f_uti_val = fuzz.interp_membership(x_mbi, util_muy_valioso, p_utilidad)

f_aut_fru = fuzz.interp_membership(x_mbi, auto_frustrado, p_autorrealizacion)
f_aut_sat = fuzz.interp_membership(x_mbi, auto_satisfecho, p_autorrealizacion)
f_aut_ple = fuzz.interp_membership(x_mbi, auto_plenamente, p_autorrealizacion)



f_sat_baj = fuzz.interp_membership(x_mbi, satis_bajo, p_satisfaccion)
f_sat_med = fuzz.interp_membership(x_mbi, satis_medio, p_satisfaccion)
f_sat_alt = fuzz.interp_membership(x_mbi, satis_alto, p_satisfaccion)

f_des_baj = fuzz.interp_membership(x_desc, desc_bajo, p_desconexion)
f_des_med = fuzz.interp_membership(x_desc, desc_medio, p_desconexion)
f_des_alt = fuzz.interp_membership(x_desc, desc_alto, p_desconexion)

f_apo_baj = fuzz.interp_membership(x_apoyo, apoyo_bajo, p_apoyo)
f_apo_med = fuzz.interp_membership(x_apoyo, apoyo_medio, p_apoyo)
f_apo_alt = fuzz.interp_membership(x_apoyo, apoyo_alto, p_apoyo)

# 5. REGLAS DE INFERENCIA (48 reglas)

# BLOQUE A: Agotamiento Emocional + Factores de Carga (R1-R8) 

# R1: agotamiento=persistente Y carga=abrumadora Y estrés=crónico → CRÍTICO
act_r1 = np.fmin(np.fmin(np.fmin(f_ago_per, f_car_abr), f_est_cro), riesgo_critico)
# R2: agotamiento=persistente Y cal_sueño=insuficiente Y estrés=alto → CRÍTICO
act_r2 = np.fmin(np.fmin(np.fmin(f_ago_per, f_cal_ins), f_est_alt), riesgo_critico)
# R3: agotamiento=frecuente Y estrés=alto Y horas_sueño=insuficiente → ALTO
act_r3 = np.fmin(np.fmin(np.fmin(f_ago_fre, f_est_alt), f_sue_ins), riesgo_alto)
# R4: fatiga=severa Y carga=abrumadora Y cal_sueño=pobre → ALTO
act_r4 = np.fmin(np.fmin(np.fmin(f_fat_sev, f_car_abr), f_cal_pob), riesgo_alto)
# R5: agotamiento=frecuente Y carga=manejable → MODERADO
act_r5 = np.fmin(np.fmin(f_ago_fre, f_car_man), riesgo_moderado)
# R6: agotamiento=ocasional Y estrés=bajo Y carga=ligera → BAJO
act_r6 = np.fmin(np.fmin(np.fmin(f_ago_oca, f_est_baj), f_car_lig), riesgo_bajo)
# R7: fatiga=nula Y cal_sueño=excelente Y estrés=bajo → MUY BAJO
act_r7 = np.fmin(np.fmin(np.fmin(f_fat_nul, f_cal_exc), f_est_baj), riesgo_muy_bajo)
# R8: estrés=crónico Y horas_sueño=insuficiente → ALTO
act_r8 = np.fmin(np.fmin(f_est_cro, f_sue_ins), riesgo_alto)
# R50: Carga manejable y Estrés moderado → RIESGO MODERADO
act_r50 = np.fmin(np.fmin(f_car_man, f_est_mod), riesgo_moderado)
# R51: Agotamiento raro y Estrés bajo → RIESGO MUY BAJO
act_r51 = np.fmin(np.fmin(f_ago_rar, f_est_baj), riesgo_muy_bajo)

# BLOQUE B: Despersonalización / Cinismo (R9-R12)

# R9: desp=cínico Y agotamiento=persistente → CRÍTICO
act_r9 = np.fmin(np.fmin(f_dep_cin, f_ago_per), riesgo_critico)
# R10: desp=distante Y carga=manejable → MODERADO
act_r10 = np.fmin(np.fmin(f_dep_dis, f_car_man), riesgo_moderado)
# R11: desp=empático Y estrés=bajo → BAJO
act_r11 = np.fmin(np.fmin(f_dep_emp, f_est_baj), riesgo_bajo)
# R12: desp=distante Y estrés=alto → ALTO
act_r12 = np.fmin(np.fmin(f_dep_dis, f_est_alt), riesgo_alto)

# BLOQUE C: Realización Personal (R13-R19) 

# R13: utilidad=nulo Y agotamiento=persistente → CRÍTICO
act_r13 = np.fmin(np.fmin(f_uti_nul, f_ago_per), riesgo_critico)
# R14: autorrealización=frustrado Y estrés=crónico → ALTO
act_r14 = np.fmin(np.fmin(f_aut_fru, f_est_cro), riesgo_alto)
# R15: utilidad=productivo Y autorrealización=satisfecho → BAJO
act_r15 = np.fmin(np.fmin(f_uti_pro, f_aut_sat), riesgo_bajo)
# R16: utilidad=muy_valioso Y estrés=bajo Y cal_sueño=excelente → MUY BAJO
act_r16 = np.fmin(np.fmin(np.fmin(f_uti_val, f_est_baj), f_cal_exc), riesgo_muy_bajo)
# R17: autorrealización=satisfecho Y carga=manejable Y estrés=moderado → MODERADO
act_r17 = np.fmin(np.fmin(np.fmin(f_aut_sat, f_car_man), f_est_mod), riesgo_moderado)
# R18: autorrealización=satisfecho Y agotamiento=ocasional → BAJO
act_r18 = np.fmin(np.fmin(f_aut_sat, f_ago_oca), riesgo_bajo)
# R19: utilidad=productivo Y desp=empático Y estrés=bajo → MUY BAJO
act_r19 = np.fmin(np.fmin(np.fmin(f_uti_pro, f_dep_emp), f_est_baj), riesgo_muy_bajo)

# BLOQUE D: Reglas combinadas multi-dimensión (R20-R28)

# R20: agotamiento=persistente Y desp=cínico Y utilidad=nulo → CRÍTICO
act_r20 = np.fmin(np.fmin(np.fmin(f_ago_per, f_dep_cin), f_uti_nul), riesgo_critico)
# R21: estrés=crónico Y carga=abrumadora Y autorrealización=frustrado → CRÍTICO
act_r21 = np.fmin(np.fmin(np.fmin(f_est_cro, f_car_abr), f_aut_fru), riesgo_critico)
# R22: agotamiento=frecuente Y desp=distante Y utilidad=productivo → ALTO
act_r22 = np.fmin(np.fmin(np.fmin(f_ago_fre, f_dep_dis), f_uti_pro), riesgo_alto)
# R23: carga=manejable Y estrés=moderado Y autorrealización=satisfecho → MODERADO
act_r23 = np.fmin(np.fmin(np.fmin(f_car_man, f_est_mod), f_aut_sat), riesgo_moderado)
# R24: horas_sueño=saludable Y cal_sueño=aceptable Y estrés=moderado → MODERADO
act_r24 = np.fmin(np.fmin(np.fmin(f_sue_sal, f_cal_ace), f_est_mod), riesgo_moderado)
# R25: agotamiento=raro Y desp=empático Y autorrealización=plenamente → MUY BAJO
act_r25 = np.fmin(np.fmin(np.fmin(f_ago_rar, f_dep_emp), f_aut_ple), riesgo_muy_bajo)
# R26: agotamiento=frecuente Y carga=abrumadora Y cal_sueño=pobre → ALTO
act_r26 = np.fmin(np.fmin(np.fmin(f_ago_fre, f_car_abr), f_cal_pob), riesgo_alto)
# R27: fatiga=leve Y desp=empático Y apoyo=alto → BAJO
act_r27 = np.fmin(np.fmin(np.fmin(f_fat_lev, f_dep_emp), f_apo_alt), riesgo_bajo)
# R28: estrés=alto Y horas_sueño=insuficiente Y agotamiento=frecuente → ALTO
act_r28 = np.fmin(np.fmin(np.fmin(f_est_alt, f_sue_ins), f_ago_fre), riesgo_alto)

# BLOQUE E: Protección y Mitigación - Apoyo y Satisfacción (R29-R34)

# R29: apoyo=alto Y satisfacción=alto Y estrés=moderado → BAJO
act_r29 = np.fmin(np.fmin(np.fmin(f_apo_alt, f_sat_alt), f_est_mod), riesgo_bajo)
# R30: apoyo=bajo Y satisfacción=bajo Y carga=abrumadora → CRÍTICO
act_r30 = np.fmin(np.fmin(np.fmin(f_apo_baj, f_sat_baj), f_car_abr), riesgo_critico)
# R31: desconexión=alto Y cal_sueño=excelente → MUY BAJO
act_r31 = np.fmin(np.fmin(f_des_alt, f_cal_exc), riesgo_muy_bajo)
# R32: desconexión=bajo Y estrés=crónico → CRÍTICO
act_r32 = np.fmin(np.fmin(f_des_baj, f_est_cro), riesgo_critico)
# R33: satisfacción=alto Y agotamiento=frecuente → MODERADO (amortiguador)
act_r33 = np.fmin(np.fmin(f_sat_alt, f_ago_fre), riesgo_moderado)
# R34: apoyo=medio Y carga=manejable Y desconexión=medio → BAJO
act_r34 = np.fmin(np.fmin(np.fmin(f_apo_med, f_car_man), f_des_med), riesgo_bajo)
# R49: Apoyo alto y Autorrealización plena → RIESGO MUY BAJO
act_r49 = np.fmin(np.fmin(f_apo_alt, f_aut_ple), riesgo_muy_bajo)

# BLOQUE F: Desconexión y Descanso (R35-R38)

# R35: desconexión=bajo Y cal_sueño=pobre Y fatiga=severa → CRÍTICO
act_r35 = np.fmin(np.fmin(np.fmin(f_des_baj, f_cal_pob), f_fat_sev), riesgo_critico)
# R36: desconexión=medio Y cal_sueño=aceptable Y horas_sueño=saludable → MODERADO
act_r36 = np.fmin(np.fmin(np.fmin(f_des_med, f_cal_ace), f_sue_sal), riesgo_moderado)
# R37: desconexión=alto Y agotamiento=ocasional Y estrés=bajo → MUY BAJO
act_r37 = np.fmin(np.fmin(np.fmin(f_des_alt, f_ago_oca), f_est_baj), riesgo_muy_bajo)
# R38: satisfacción=bajo Y desconexión=bajo Y agotamiento=persistente → CRÍTICO
act_r38 = np.fmin(np.fmin(np.fmin(f_sat_baj, f_des_baj), f_ago_per), riesgo_critico)
# R52: Calidad de sueño aceptable y Agotamiento ocasional → RIESGO BAJO
act_r52 = np.fmin(np.fmin(f_cal_ace, f_ago_oca), riesgo_bajo)

# BLOQUE G: Combinadas multi-dimensión nuevas (R39-R48)

# R39: carga=abrumadora Y apoyo=bajo Y desp=cínico → CRÍTICO
act_r39 = np.fmin(np.fmin(np.fmin(f_car_abr, f_apo_baj), f_dep_cin), riesgo_critico)
# R40: estrés=alto Y satisfacción=bajo Y utilidad=nulo → CRÍTICO
act_r40 = np.fmin(np.fmin(np.fmin(f_est_alt, f_sat_baj), f_uti_nul), riesgo_critico)
# R41: autorrealización=satisfecho Y apoyo=alto Y carga=manejable → MUY BAJO
act_r41 = np.fmin(np.fmin(np.fmin(f_aut_sat, f_apo_alt), f_car_man), riesgo_muy_bajo)
# R42: fatiga=severa Y desconexión=bajo Y apoyo=bajo → ALTO
act_r42 = np.fmin(np.fmin(np.fmin(f_fat_sev, f_des_baj), f_apo_baj), riesgo_alto)
# R43: agotamiento=frecuente Y satisfacción=medio Y desconexión=medio → ALTO
act_r43 = np.fmin(np.fmin(np.fmin(f_ago_fre, f_sat_med), f_des_med), riesgo_alto)
# R44: carga=ligera Y apoyo=alto Y autorrealización=plenamente → MUY BAJO
act_r44 = np.fmin(np.fmin(np.fmin(f_car_lig, f_apo_alt), f_aut_ple), riesgo_muy_bajo)
# R45: estrés=crónico Y apoyo=medio Y desconexión=bajo → ALTO
act_r45 = np.fmin(np.fmin(np.fmin(f_est_cro, f_apo_med), f_des_baj), riesgo_alto)
# R46: utilidad=muy_valioso Y satisfacción=alto Y agotamiento=raro → MUY BAJO
act_r46 = np.fmin(np.fmin(np.fmin(f_uti_val, f_sat_alt), f_ago_rar), riesgo_muy_bajo)
# R47: desp=distante Y satisfacción=bajo Y apoyo=bajo → ALTO
act_r47 = np.fmin(np.fmin(np.fmin(f_dep_dis, f_sat_baj), f_apo_baj), riesgo_alto)
# R48: fatiga=leve Y desconexión=medio Y satisfacción=medio → MODERADO
act_r48 = np.fmin(np.fmin(np.fmin(f_fat_lev, f_des_med), f_sat_med), riesgo_moderado)
# R53: Carga abrumadora y Estrés moderado → ALTO (Persona 72)
act_r53 = np.fmin(np.fmin(f_car_abr, f_est_mod), riesgo_alto)
# R54: Agotamiento frecuente y Estrés alto → ALTO (Persona 74)
act_r54 = np.fmin(np.fmin(f_ago_fre, f_est_alt), riesgo_alto)
# R55: Agotamiento ocasional y Estrés moderado → MODERADO (General)
act_r55 = np.fmin(np.fmin(f_ago_oca, f_est_mod), riesgo_moderado)
# R56: Agotamiento raro y Estrés moderado → MUY BAJO (Caso desempleo/inactividad)
act_r56 = np.fmin(np.fmin(f_ago_rar, f_est_mod), riesgo_muy_bajo)



# 6. AGREGACIÓN DE TODAS LAS SALIDAS
act_rules = [
    act_r1,  act_r2,  act_r3,  act_r4,  act_r5,  act_r6,  act_r7,  act_r8,
    act_r9,  act_r10, act_r11, act_r12, act_r13, act_r14, act_r15, act_r16,
    act_r17, act_r18, act_r19, act_r20, act_r21, act_r22, act_r23, act_r24,
    act_r25, act_r26, act_r27, act_r28, act_r29, act_r30, act_r31, act_r32,
    act_r33, act_r34, act_r35, act_r36, act_r37, act_r38, act_r39, act_r40,
    act_r41, act_r42, act_r43, act_r44, act_r45, act_r46, act_r47, act_r48,
    act_r49, act_r50, act_r51, act_r52, act_r53, act_r54, act_r55, act_r56
]

aggregated = np.maximum.reduce(act_rules)

# 7. DEFUZZIFICACIÓN (Método del centroide)
resultado = fuzz.defuzz(x_riesgo, aggregated, 'centroid')
grado_riesgo = fuzz.interp_membership(x_riesgo, aggregated, resultado)

if resultado <= 20:
    nivel = "MUY BAJO"
elif resultado <= 40:
    nivel = "BAJO"
elif resultado <= 60:
    nivel = "MODERADO"
elif resultado <= 80:
    nivel = "ALTO"
else:
    nivel = "CRÍTICO"

print(f"\n{'=' * 65}")
print(f"   RESULTADO: Riesgo de Burnout estimado: {resultado:.2f}%")
print(f"   Nivel: {nivel}")
print(f"{'=' * 65}")

# 8. VISUALIZACIÓN DEL RESULTADO
fig, ax0 = plt.subplots(figsize=(10, 4))
ax0.plot(x_riesgo, riesgo_muy_bajo, 'b', linestyle='--', label='Muy Bajo')
ax0.plot(x_riesgo, riesgo_bajo, 'c', linestyle='--', label='Bajo')
ax0.plot(x_riesgo, riesgo_moderado, 'orange', linestyle='--', label='Moderado')
ax0.plot(x_riesgo, riesgo_alto, 'r', linestyle='--', label='Alto')
ax0.plot(x_riesgo, riesgo_critico, 'm', linestyle='--', label='Crítico')
ax0.fill_between(x_riesgo, np.zeros_like(x_riesgo), aggregated, facecolor='orange', alpha=0.7)
ax0.plot([resultado, resultado], [0, grado_riesgo], 'k', linewidth=2, alpha=0.9)
ax0.set_title(f'Resultado del Riesgo de Burnout: {resultado:.2f}% ({nivel})')
ax0.set_xlabel('Nivel de Riesgo (%)')
ax0.set_ylabel('Grado de Pertenencia')
ax0.legend(loc='upper right')
plt.tight_layout()
plt.show()