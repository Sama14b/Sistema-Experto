# SISTEMA EXPERTO DIFUSO - DETECCIÓN DE RIESGO DE BURNOUT
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# 1. UNIVERSOS DE DISCURSO (Variables lingüísticas)
x_horas_ded = np.arange(0, 17, 1)        # Horas dedicación estudio/trabajo (0-16)
x_carga = np.arange(1, 11, 1)            # Carga de trabajo percibida (1-10)
x_horas_sueno = np.arange(0, 15, 1)      # Horas de sueño (0-14)
x_cal_sueno = np.arange(1, 11, 1)        # Calidad del sueño (1-10)
x_estres = np.arange(1, 11, 1)           # Estrés diario (1-10)
x_mbi = np.arange(0, 7, 1)              # Escala MBI para todas las preguntas (0-6)
x_riesgo = np.arange(0, 101, 1)          # Variable de salida: riesgo burnout (0-100)

# 2. FUNCIONES DE PERTENENCIA

# Horas de dedicación diaria
ded_reducida = fuzz.trimf(x_horas_ded, [0, 0, 5])
ded_estandar = fuzz.trimf(x_horas_ded, [4, 7, 10])
ded_excesiva = fuzz.trapmf(x_horas_ded, [9, 12, 16, 16])

# Carga de trabajo percibida 
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

# Estrés diario
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

# Saturación mental (MBI 0-6) 
sat_controlado = fuzz.trimf(x_mbi, [0, 0, 2])
sat_al_limite = fuzz.trimf(x_mbi, [1, 3, 5])
sat_desbordado = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Despersonalización / Cinismo (MBI 0-6)
desp_empatico = fuzz.trimf(x_mbi, [0, 0, 2])
desp_distante = fuzz.trimf(x_mbi, [1, 3, 5])
desp_cinico = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Indiferencia (MBI 0-6)
ind_comprometido = fuzz.trimf(x_mbi, [0, 0, 2])
ind_despegado = fuzz.trimf(x_mbi, [1, 3, 5])
ind_indiferente = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Deshumanización (MBI 0-6) 
desh_humano = fuzz.trimf(x_mbi, [0, 0, 2])
desh_distante = fuzz.trimf(x_mbi, [1, 3, 5])
desh_deshumanizado = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Percepción de utilidad (MBI 0-6, INVERTIDA)
util_nulo = fuzz.trimf(x_mbi, [0, 0, 2])
util_productivo = fuzz.trimf(x_mbi, [1, 3, 5])
util_muy_valioso = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Autorrealización (MBI 0-6, INVERTIDA) 
auto_frustrado = fuzz.trimf(x_mbi, [0, 0, 2])
auto_satisfecho = fuzz.trimf(x_mbi, [1, 3, 5])
auto_plenamente = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

# Competencia percibida (MBI 0-6, INVERTIDA)
comp_nula = fuzz.trimf(x_mbi, [0, 0, 2])
comp_adecuada = fuzz.trimf(x_mbi, [1, 3, 5])
comp_destacada = fuzz.trapmf(x_mbi, [4, 5, 6, 6])

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

# Variables demográficas (modificadores contextuales) 
print("1: 18-22 años")
print("2: 23-30 años")
print("3: Más de 30 años")
p_edad = int(input("¿Qué edad tienes? (1/2/3): "))

print("\n1: Mujer")
print("2: Hombre")
p_sexo = int(input("Sexo (1/2): "))

print("\n1: Estudio")
print("2: Trabajo")
print("3: Ambas")
p_ocupacion = int(input("Ocupación actual (1/2/3): "))

# Variables difusas continuas
p_horas_ded = int(input("\n¿Cuántas horas al día dedicas de media al estudio o trabajo?: "))
p_carga = int(input("¿Cómo de alta percibes tu carga de trabajo? (1-10): "))
p_horas_sueno = int(input("¿Cuántas horas duermes de media al día?: "))
p_cal_sueno = int(input("¿Cómo valorarías la calidad de tu sueño? (1-10): "))
p_estres = int(input("¿Cuánto estrés sientes en tu día a día? (1-10): "))

# Preguntas MBI (0-6)
print("\nIndica con qué frecuencia experimentas las siguientes situaciones:")
print("  0: Nunca | 1: Pocas veces al año | 2: Una vez al mes o menos")
print("  3: Unas pocas veces al mes | 4: Una vez a la semana")
print("  5: Varias veces a la semana | 6: Todos los días\n")

p_agotamiento = int(input("Me siento emocionalmente agotado (0-6): "))
p_fatiga = int(input("Me siento cansado al empezar el día (0-6): "))
p_saturacion = int(input("Siento que ya no puedo más mentalmente (0-6): "))
p_despersonalizacion = int(input("Me estoy volviendo más frío o distante (0-6): "))
p_indiferencia = int(input("Me da igual lo que pase en mi entorno (0-6): "))
p_deshumanizacion = int(input("Trato a las personas como si fueran objetos (0-6): "))
p_utilidad = int(input("Siento que hago cosas útiles y valiosas (0-6): "))
p_autorrealizacion = int(input("Me siento realizado con lo que hago (0-6): "))
p_competencia = int(input("Creo que soy bueno en lo que hago (0-6): "))

# 4. FUZZIFICACIÓN (Interpolación de grados de pertenencia)

# Horas de dedicación
f_ded_reducida = fuzz.interp_membership(x_horas_ded, ded_reducida, p_horas_ded)
f_ded_estandar = fuzz.interp_membership(x_horas_ded, ded_estandar, p_horas_ded)
f_ded_excesiva = fuzz.interp_membership(x_horas_ded, ded_excesiva, p_horas_ded)

# Carga de trabajo
f_carga_ligera = fuzz.interp_membership(x_carga, carga_ligera, p_carga)
f_carga_manejable = fuzz.interp_membership(x_carga, carga_manejable, p_carga)
f_carga_abrumadora = fuzz.interp_membership(x_carga, carga_abrumadora, p_carga)

# Horas de sueño
f_sueno_insuf = fuzz.interp_membership(x_horas_sueno, sueno_insuficiente, p_horas_sueno)
f_sueno_salud = fuzz.interp_membership(x_horas_sueno, sueno_saludable, p_horas_sueno)
f_sueno_prolong = fuzz.interp_membership(x_horas_sueno, sueno_prolongado, p_horas_sueno)

# Calidad del sueño
f_cal_insuf = fuzz.interp_membership(x_cal_sueno, cal_insuficiente, p_cal_sueno)
f_cal_pobre = fuzz.interp_membership(x_cal_sueno, cal_pobre, p_cal_sueno)
f_cal_acept = fuzz.interp_membership(x_cal_sueno, cal_aceptable, p_cal_sueno)
f_cal_excel = fuzz.interp_membership(x_cal_sueno, cal_excelente, p_cal_sueno)

# Estrés
f_est_bajo = fuzz.interp_membership(x_estres, est_bajo, p_estres)
f_est_moderado = fuzz.interp_membership(x_estres, est_moderado, p_estres)
f_est_alto = fuzz.interp_membership(x_estres, est_alto, p_estres)
f_est_cronico = fuzz.interp_membership(x_estres, est_cronico, p_estres)

# Agotamiento emocional
f_agot_raro = fuzz.interp_membership(x_mbi, agot_raro, p_agotamiento)
f_agot_ocasional = fuzz.interp_membership(x_mbi, agot_ocasional, p_agotamiento)
f_agot_frecuente = fuzz.interp_membership(x_mbi, agot_frecuente, p_agotamiento)
f_agot_persistente = fuzz.interp_membership(x_mbi, agot_persistente, p_agotamiento)

# Fatiga anticipatoria
f_fat_nula = fuzz.interp_membership(x_mbi, fat_nula, p_fatiga)
f_fat_leve = fuzz.interp_membership(x_mbi, fat_leve, p_fatiga)
f_fat_severa = fuzz.interp_membership(x_mbi, fat_severa, p_fatiga)

# Saturación mental
f_sat_controlado = fuzz.interp_membership(x_mbi, sat_controlado, p_saturacion)
f_sat_al_limite = fuzz.interp_membership(x_mbi, sat_al_limite, p_saturacion)
f_sat_desbordado = fuzz.interp_membership(x_mbi, sat_desbordado, p_saturacion)

# Despersonalización
f_desp_empatico = fuzz.interp_membership(x_mbi, desp_empatico, p_despersonalizacion)
f_desp_distante = fuzz.interp_membership(x_mbi, desp_distante, p_despersonalizacion)
f_desp_cinico = fuzz.interp_membership(x_mbi, desp_cinico, p_despersonalizacion)

# Indiferencia
f_ind_comprometido = fuzz.interp_membership(x_mbi, ind_comprometido, p_indiferencia)
f_ind_despegado = fuzz.interp_membership(x_mbi, ind_despegado, p_indiferencia)
f_ind_indiferente = fuzz.interp_membership(x_mbi, ind_indiferente, p_indiferencia)

# Deshumanización
f_desh_humano = fuzz.interp_membership(x_mbi, desh_humano, p_deshumanizacion)
f_desh_distante = fuzz.interp_membership(x_mbi, desh_distante, p_deshumanizacion)
f_desh_deshumanizado = fuzz.interp_membership(x_mbi, desh_deshumanizado, p_deshumanizacion)

# Percepción de utilidad (INVERTIDA: alto = bajo riesgo)
f_util_nulo = fuzz.interp_membership(x_mbi, util_nulo, p_utilidad)
f_util_productivo = fuzz.interp_membership(x_mbi, util_productivo, p_utilidad)
f_util_muy_valioso = fuzz.interp_membership(x_mbi, util_muy_valioso, p_utilidad)

# Autorrealización (INVERTIDA)
f_auto_frustrado = fuzz.interp_membership(x_mbi, auto_frustrado, p_autorrealizacion)
f_auto_satisfecho = fuzz.interp_membership(x_mbi, auto_satisfecho, p_autorrealizacion)
f_auto_plenamente = fuzz.interp_membership(x_mbi, auto_plenamente, p_autorrealizacion)

# Competencia percibida (INVERTIDA)
f_comp_nula = fuzz.interp_membership(x_mbi, comp_nula, p_competencia)
f_comp_adecuada = fuzz.interp_membership(x_mbi, comp_adecuada, p_competencia)
f_comp_destacada = fuzz.interp_membership(x_mbi, comp_destacada, p_competencia)

# 5. REGLAS DE INFERENCIA (50 reglas)

# BLOQUE A: Agotamiento Emocional + Factores de Carga (R1-R15)

# R1: SI agotamiento ES persistente Y carga ES abrumadora Y estrés ES crónico → CRÍTICO
regla1 = np.fmin(np.fmin(f_agot_persistente, f_carga_abrumadora), f_est_cronico)
act_r1 = np.fmin(regla1, riesgo_critico)

# R2: SI fatiga ES severa Y saturación ES desbordado Y horas_ded ES excesiva → CRÍTICO
regla2 = np.fmin(np.fmin(f_fat_severa, f_sat_desbordado), f_ded_excesiva)
act_r2 = np.fmin(regla2, riesgo_critico)

# R3: SI agotamiento ES persistente Y calidad_sueño ES insuficiente Y estrés ES alto → CRÍTICO
regla3 = np.fmin(np.fmin(f_agot_persistente, f_cal_insuf), f_est_alto)
act_r3 = np.fmin(regla3, riesgo_critico)

# R4: SI saturación ES desbordado Y carga ES abrumadora → ALTO
regla4 = np.fmin(f_sat_desbordado, f_carga_abrumadora)
act_r4 = np.fmin(regla4, riesgo_alto)

# R5: SI agotamiento ES frecuente Y estrés ES alto Y horas_sueño ES insuficiente → ALTO
regla5 = np.fmin(np.fmin(f_agot_frecuente, f_est_alto), f_sueno_insuf)
act_r5 = np.fmin(regla5, riesgo_alto)

# R6: SI fatiga ES severa Y carga ES abrumadora Y calidad_sueño ES pobre → ALTO
regla6 = np.fmin(np.fmin(f_fat_severa, f_carga_abrumadora), f_cal_pobre)
act_r6 = np.fmin(regla6, riesgo_alto)

# R7: SI agotamiento ES frecuente Y carga ES manejable → MODERADO
regla7 = np.fmin(f_agot_frecuente, f_carga_manejable)
act_r7 = np.fmin(regla7, riesgo_moderado)

# R8: SI estrés ES moderado Y fatiga ES leve Y saturación ES al_limite → MODERADO
regla8 = np.fmin(np.fmin(f_est_moderado, f_fat_leve), f_sat_al_limite)
act_r8 = np.fmin(regla8, riesgo_moderado)

# R9: SI horas_ded ES excesiva Y calidad_sueño ES aceptable → MODERADO
regla9 = np.fmin(f_ded_excesiva, f_cal_acept)
act_r9 = np.fmin(regla9, riesgo_moderado)

# R10: SI agotamiento ES ocasional Y estrés ES bajo Y carga ES ligera → BAJO
regla10 = np.fmin(np.fmin(f_agot_ocasional, f_est_bajo), f_carga_ligera)
act_r10 = np.fmin(regla10, riesgo_bajo)

# R11: SI fatiga ES nula Y calidad_sueño ES excelente Y estrés ES bajo → MUY BAJO
regla11 = np.fmin(np.fmin(f_fat_nula, f_cal_excel), f_est_bajo)
act_r11 = np.fmin(regla11, riesgo_muy_bajo)

# R12: SI agotamiento ES raro Y saturación ES controlado Y horas_sueño ES saludable → MUY BAJO
regla12 = np.fmin(np.fmin(f_agot_raro, f_sat_controlado), f_sueno_salud)
act_r12 = np.fmin(regla12, riesgo_muy_bajo)

# R13: SI horas_ded ES estándar Y carga ES ligera Y calidad_sueño ES excelente → MUY BAJO
regla13 = np.fmin(np.fmin(f_ded_estandar, f_carga_ligera), f_cal_excel)
act_r13 = np.fmin(regla13, riesgo_muy_bajo)

# R14: SI estrés ES crónico Y horas_sueño ES insuficiente → ALTO
regla14 = np.fmin(f_est_cronico, f_sueno_insuf)
act_r14 = np.fmin(regla14, riesgo_alto)

# R15: SI carga ES abrumadora Y horas_ded ES excesiva → ALTO
regla15 = np.fmin(f_carga_abrumadora, f_ded_excesiva)
act_r15 = np.fmin(regla15, riesgo_alto)

# BLOQUE B: Despersonalización / Cinismo (R16-R25)

# R16: SI desp ES cínico Y indiferencia ES indiferente Y deshum ES deshumanizado → CRÍTICO
regla16 = np.fmin(np.fmin(f_desp_cinico, f_ind_indiferente), f_desh_deshumanizado)
act_r16 = np.fmin(regla16, riesgo_critico)

# R17: SI desp ES cínico Y agotamiento ES persistente → CRÍTICO
regla17 = np.fmin(f_desp_cinico, f_agot_persistente)
act_r17 = np.fmin(regla17, riesgo_critico)

# R18: SI indiferencia ES indiferente Y saturación ES desbordado → ALTO
regla18 = np.fmin(f_ind_indiferente, f_sat_desbordado)
act_r18 = np.fmin(regla18, riesgo_alto)

# R19: SI deshum ES deshumanizado Y estrés ES alto → ALTO
regla19 = np.fmin(f_desh_deshumanizado, f_est_alto)
act_r19 = np.fmin(regla19, riesgo_alto)

# R20: SI desp ES distante Y indiferencia ES despegado → MODERADO
regla20 = np.fmin(f_desp_distante, f_ind_despegado)
act_r20 = np.fmin(regla20, riesgo_moderado)

# R21: SI deshum ES distante Y carga ES manejable → MODERADO
regla21 = np.fmin(f_desh_distante, f_carga_manejable)
act_r21 = np.fmin(regla21, riesgo_moderado)

# R22: SI desp ES empático Y indiferencia ES comprometido → BAJO
regla22 = np.fmin(f_desp_empatico, f_ind_comprometido)
act_r22 = np.fmin(regla22, riesgo_bajo)

# R23: SI deshum ES humano Y desp ES empático Y indiferencia ES comprometido → MUY BAJO
regla23 = np.fmin(np.fmin(f_desh_humano, f_desp_empatico), f_ind_comprometido)
act_r23 = np.fmin(regla23, riesgo_muy_bajo)

# R24: SI indiferencia ES indiferente Y carga ES abrumadora Y fatiga ES severa → CRÍTICO
regla24 = np.fmin(np.fmin(f_ind_indiferente, f_carga_abrumadora), f_fat_severa)
act_r24 = np.fmin(regla24, riesgo_critico)

# R25: SI desp ES distante Y estrés ES alto → ALTO
regla25 = np.fmin(f_desp_distante, f_est_alto)
act_r25 = np.fmin(regla25, riesgo_alto)

# BLOQUE C: Realización Personal (R26-R35, lógica invertida) 

# R26: SI utilidad ES nulo Y autorrealización ES frustrado Y competencia ES nula → CRÍTICO
regla26 = np.fmin(np.fmin(f_util_nulo, f_auto_frustrado), f_comp_nula)
act_r26 = np.fmin(regla26, riesgo_critico)

# R27: SI utilidad ES nulo Y agotamiento ES persistente → CRÍTICO
regla27 = np.fmin(f_util_nulo, f_agot_persistente)
act_r27 = np.fmin(regla27, riesgo_critico)

# R28: SI autorrealización ES frustrado Y estrés ES crónico → ALTO
regla28 = np.fmin(f_auto_frustrado, f_est_cronico)
act_r28 = np.fmin(regla28, riesgo_alto)

# R29: SI competencia ES nula Y saturación ES desbordado → ALTO
regla29 = np.fmin(f_comp_nula, f_sat_desbordado)
act_r29 = np.fmin(regla29, riesgo_alto)

# R30: SI utilidad ES productivo Y autorrealización ES satisfecho → BAJO
regla30 = np.fmin(f_util_productivo, f_auto_satisfecho)
act_r30 = np.fmin(regla30, riesgo_bajo)

# R31: SI competencia ES destacada Y autorrealización ES plenamente → MUY BAJO
regla31 = np.fmin(f_comp_destacada, f_auto_plenamente)
act_r31 = np.fmin(regla31, riesgo_muy_bajo)

# R32: SI utilidad ES muy_valioso Y estrés ES bajo Y calidad_sueño ES excelente → MUY BAJO
regla32 = np.fmin(np.fmin(f_util_muy_valioso, f_est_bajo), f_cal_excel)
act_r32 = np.fmin(regla32, riesgo_muy_bajo)

# R33: SI autorrealización ES satisfecho Y carga ES manejable Y estrés ES moderado → MODERADO
regla33 = np.fmin(np.fmin(f_auto_satisfecho, f_carga_manejable), f_est_moderado)
act_r33 = np.fmin(regla33, riesgo_moderado)

# R34: SI competencia ES adecuada Y agotamiento ES ocasional → BAJO
regla34 = np.fmin(f_comp_adecuada, f_agot_ocasional)
act_r34 = np.fmin(regla34, riesgo_bajo)

# R35: SI utilidad ES productivo Y desp ES empático Y estrés ES bajo → MUY BAJO
regla35 = np.fmin(np.fmin(f_util_productivo, f_desp_empatico), f_est_bajo)
act_r35 = np.fmin(regla35, riesgo_muy_bajo)

# BLOQUE D: Reglas combinadas multi-dimensión (R36-R50) 

# R36: SI agotamiento ES persistente Y desp ES cínico Y utilidad ES nulo → CRÍTICO
regla36 = np.fmin(np.fmin(f_agot_persistente, f_desp_cinico), f_util_nulo)
act_r36 = np.fmin(regla36, riesgo_critico)

# R37: SI estrés ES crónico Y carga ES abrumadora Y autorrealización ES frustrado → CRÍTICO
regla37 = np.fmin(np.fmin(f_est_cronico, f_carga_abrumadora), f_auto_frustrado)
act_r37 = np.fmin(regla37, riesgo_critico)

# R38: SI saturación ES desbordado Y deshum ES deshumanizado Y competencia ES nula → CRÍTICO
regla38 = np.fmin(np.fmin(f_sat_desbordado, f_desh_deshumanizado), f_comp_nula)
act_r38 = np.fmin(regla38, riesgo_critico)

# R39: SI agotamiento ES frecuente Y desp ES distante Y utilidad ES productivo → ALTO
regla39 = np.fmin(np.fmin(f_agot_frecuente, f_desp_distante), f_util_productivo)
act_r39 = np.fmin(regla39, riesgo_alto)

# R40: SI carga ES manejable Y estrés ES moderado Y autorrealización ES satisfecho → MODERADO
regla40 = np.fmin(np.fmin(f_carga_manejable, f_est_moderado), f_auto_satisfecho)
act_r40 = np.fmin(regla40, riesgo_moderado)

# R41: SI horas_sueño ES saludable Y calidad_sueño ES aceptable Y estrés ES moderado → MODERADO
regla41 = np.fmin(np.fmin(f_sueno_salud, f_cal_acept), f_est_moderado)
act_r41 = np.fmin(regla41, riesgo_moderado)

# R42: SI agotamiento ES raro Y desp ES empático Y competencia ES destacada → MUY BAJO
regla42 = np.fmin(np.fmin(f_agot_raro, f_desp_empatico), f_comp_destacada)
act_r42 = np.fmin(regla42, riesgo_muy_bajo)

# R43: SI fatiga ES nula Y indiferencia ES comprometido Y autorrealización ES plenamente → MUY BAJO
regla43 = np.fmin(np.fmin(f_fat_nula, f_ind_comprometido), f_auto_plenamente)
act_r43 = np.fmin(regla43, riesgo_muy_bajo)

# R44: SI horas_ded ES estándar Y carga ES manejable Y estrés ES bajo Y cal_sueño ES aceptable → BAJO
regla44 = np.fmin(np.fmin(f_ded_estandar, f_carga_manejable), np.fmin(f_est_bajo, f_cal_acept))
act_r44 = np.fmin(regla44, riesgo_bajo)

# R45: SI ocupación ES ambas Y agotamiento ES frecuente Y carga ES abrumadora → CRÍTICO
# (Modificador contextual: ocupación = 3 agrava el riesgo)
if p_ocupacion == 3:
    regla45 = np.fmin(f_agot_frecuente, f_carga_abrumadora)
    act_r45 = np.fmin(regla45, riesgo_critico)
else:
    act_r45 = np.zeros_like(x_riesgo)

# R46: SI ocupación ES ambas Y estrés ES alto Y horas_ded ES excesiva → CRÍTICO
if p_ocupacion == 3:
    regla46 = np.fmin(f_est_alto, f_ded_excesiva)
    act_r46 = np.fmin(regla46, riesgo_critico)
else:
    act_r46 = np.zeros_like(x_riesgo)

# R47: SI fatiga ES leve Y desp ES empático Y competencia ES adecuada → BAJO
regla47 = np.fmin(np.fmin(f_fat_leve, f_desp_empatico), f_comp_adecuada)
act_r47 = np.fmin(regla47, riesgo_bajo)

# R48: SI estrés ES alto Y horas_sueño ES insuficiente Y agotamiento ES frecuente → ALTO
regla48 = np.fmin(np.fmin(f_est_alto, f_sueno_insuf), f_agot_frecuente)
act_r48 = np.fmin(regla48, riesgo_alto)

# R49: SI calidad_sueño ES insuficiente Y carga ES abrumadora Y saturación ES desbordado → CRÍTICO
regla49 = np.fmin(np.fmin(f_cal_insuf, f_carga_abrumadora), f_sat_desbordado)
act_r49 = np.fmin(regla49, riesgo_critico)

# R50: SI horas_ded ES reducida Y estrés ES bajo Y autorrealización ES plenamente Y cal_sueño ES excelente → MUY BAJO
regla50 = np.fmin(np.fmin(f_ded_reducida, f_est_bajo), np.fmin(f_auto_plenamente, f_cal_excel))
act_r50 = np.fmin(regla50, riesgo_muy_bajo)

# 6. AGREGACIÓN DE TODAS LAS SALIDAS
act_rules = [
    act_r1,  act_r2,  act_r3,  act_r4,  act_r5,
    act_r6,  act_r7,  act_r8,  act_r9,  act_r10,
    act_r11, act_r12, act_r13, act_r14, act_r15,
    act_r16, act_r17, act_r18, act_r19, act_r20,
    act_r21, act_r22, act_r23, act_r24, act_r25,
    act_r26, act_r27, act_r28, act_r29, act_r30,
    act_r31, act_r32, act_r33, act_r34, act_r35,
    act_r36, act_r37, act_r38, act_r39, act_r40,
    act_r41, act_r42, act_r43, act_r44, act_r45,
    act_r46, act_r47, act_r48, act_r49, act_r50
]

aggregated = np.maximum.reduce(act_rules)

# 7. DEFUZZIFICACIÓN (Método del centroide)
resultado = fuzz.defuzz(x_riesgo, aggregated, 'centroid')
grado_riesgo = fuzz.interp_membership(x_riesgo, aggregated, resultado)

# Clasificación del nivel
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
