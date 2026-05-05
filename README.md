# Sistema Experto Difuso: Detección de Riesgo de Burnout

Sistema experto basado en **lógica difusa** para evaluar el nivel de riesgo de burnout en estudiantes y trabajadores, desarrollado con `scikit-fuzzy` en Python.

## Descripción

El sistema utiliza la metodología del **Maslach Burnout Inventory (MBI)** adaptada para evaluar tres dimensiones del burnout:
- **Agotamiento emocional**: cansancio, fatiga, saturación mental
- **Despersonalización/Cinismo**: distancia emocional, indiferencia, deshumanización
- **Realización personal** (invertida): percepción de utilidad, autorrealización, competencia

Además incorpora factores contextuales como carga de trabajo, horas de dedicación, calidad y cantidad de sueño, y nivel de estrés.

## Variables del Sistema

### Variables de entrada (14 difusas + 3 contextuales)
| Variable | Rango | Conjuntos Difusos |
|----------|-------|--------------------|
| Horas de dedicación | 0-16 | Reducida, Estándar, Excesiva |
| Carga de trabajo | 1-10 | Ligera, Manejable, Abrumadora |
| Horas de sueño | 0-14 | Insuficiente, Saludable, Prolongada |
| Calidad del sueño | 1-10 | Insuficiente, Pobre, Aceptable, Excelente |
| Estrés diario | 1-10 | Bajo, Moderado, Alto, Crónico |
| Agotamiento emocional | 0-6 | Raro, Ocasional, Frecuente, Persistente |
| Fatiga anticipatoria | 0-6 | Nula, Leve, Severa |
| Saturación mental | 0-6 | Controlado, Al límite, Desbordado |
| Despersonalización | 0-6 | Empático, Distante, Cínico |
| Indiferencia | 0-6 | Comprometido, Despegado, Indiferente |
| Deshumanización | 0-6 | Humano, Distante, Deshumanizado |
| Percepción de utilidad | 0-6 | Nulo, Productivo, Muy Valioso |
| Autorrealización | 0-6 | Frustrado, Satisfecho, Plenamente Realizado |
| Competencia percibida | 0-6 | Nula, Adecuada, Destacada |

### Variable de salida
| Variable | Rango | Conjuntos Difusos |
|----------|-------|--------------------|
| Riesgo de Burnout | 0-100% | Muy Bajo, Bajo, Moderado, Alto, Crítico |

## Estructura del Proyecto

```
sistema_experto/
├── burnout_sistema_experto.py   # Sistema principal (entrada manual)
├── burnout_graficas.py          # Genera gráficas de funciones de pertenencia
├── burnout_batch.py             # Procesamiento batch del CSV de la encuesta
├── Encuesta sobre Bienestar...  # Datos de la encuesta (101 respuestas)
├── graficas/                    # Gráficas de funciones de pertenencia (15 PNG)
├── resultados/                  # Resultados del procesamiento batch
│   ├── resultados_burnout.csv
│   └── distribucion_burnout.png
├── venv/                        # Entorno virtual de Python
└── README.md
```

## Instalación y ejecución

### 1. Instalación de dependencias
Desde la terminal de Visual Studio Code (con la carpeta del proyecto abierta), ejecuta:
```bash
pip install -r requirements.txt
```

### 2. Ejecutar todo el sistema (gráficas + batch)
Para generar todas las gráficas y procesar la encuesta de una sola vez:
```bash
python burnout_graficas.py && python burnout_batch.py
```

### 3. Ejecución de archivos individuales

**Sistema principal (entrada manual):**
```bash
python burnout_sistema_experto.py
```

**Generar gráficas de funciones de pertenencia:**
```bash
python burnout_graficas.py
# Las gráficas se guardan en la carpeta graficas/
```

**Procesamiento batch de la encuesta:**
```bash
python burnout_batch.py
# Los resultados se guardan en la carpeta resultados/
```

## Motor de Inferencia

El sistema contiene **50 reglas de inferencia** organizadas en 4 bloques:
- **Bloque A (R1-R15)**: Agotamiento emocional + factores de carga
- **Bloque B (R16-R25)**: Despersonalización / Cinismo
- **Bloque C (R26-R35)**: Realización personal (lógica invertida)
- **Bloque D (R36-R50)**: Reglas combinadas multi-dimensión

Se utiliza el **método del centroide** para la defuzzificación.

## Tecnologías

- Python 3.12
- scikit-fuzzy 0.5.0
- NumPy
- Matplotlib
- SciPy

## Autores

Asignatura: Razonamiento Basado en la Incertidumbre (RBI) — Curso 2025/2026
Sama Al Adib
Carla Carreras Villarejo
Sandra Crevillen Contreras
Alba García Calvete