# 🐍 SKILL: PYTHON CLEAN CODE STANDARDS (REAL PYTHON)
Esta skill actúa como un linter estricto. Rige los estándares de calidad, legibilidad y rendimiento para todo el código Python del proyecto[cite: 226, 230].

#### 1. 💡 LEGIBILIDAD Y ESTRUCTURA (THE ZEN OF PYTHON)
* **Guard Clauses (Early Returns)**: Uso OBLIGATORIO de retornos tempranos para evitar el código espagueti anidado en forma de "V"[cite: 230].
* **Type Hinting Estricto**: Uso innegociable de tipado estático (Python 3.10+) en métodos, funciones, firmas de FastAPI y modelos Pydantic[cite: 226].
* **Simplicidad**: Prohibido crear lógicas anidadas de más de 3 niveles[cite: 226].

#### 2. ⚡ OPTIMIZACIÓN (PYTHONIC WAY)
* **List Comprehensions**: Usar para transformar datos en lugar de bucles `for` simples, siempre que no sacrifique legibilidad[cite: 227].
* **F-Strings**: Uso exclusivo de f-strings para formateo de cadenas (Python 3.12+). Prohibido `.format()` o `%`[cite: 227].
* **EAFP (It's Easier to Ask for Forgiveness than Permission)**: Priorizar bloques `try/except` sobre verificaciones preventivas constantes con `if`[cite: 227].

#### 3. 🚫 ANTI-PATRONES (LO QUE NO SE DEBE HACER)
* **Variables Genéricas**: Prohibido usar `i`, `temp`, `data` o `info`. Exigir nombres semánticos que reflejen la regla de negocio[cite: 228].
* **Global Imports**: Prohibido importar librerías dentro de métodos. Los imports van siempre al inicio: 1. Stdlib, 2. Externos, 3. Locales[cite: 228].
* **Magic Numbers**: Prohibido usar números directamente en la lógica. Definir constantes al inicio del archivo o en configuraciones[cite: 228].

#### 4. 📉 COMPRESIÓN Y AHORRO DE TOKENS (G-ZERO)
* **Cero Comentarios Obvios**: Prohibido documentar lo que el código ya explica por sí mismo[cite: 230].
* **Docstrings Minimalistas**: Prohibido generar docstrings gigantes. Solo una frase técnica si la complejidad de la función lo amerita, explicando el *por qué*, no el *cómo*[cite: 230].