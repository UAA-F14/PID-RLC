Proyecto Intermedio Teoría de Control II 



<!-- Start of picture text -->
~—<br>Cr<br><!-- End of picture text -->



<!-- Start of picture text -->
Be<br>30<br><!-- End of picture text -->

# **1. Objetivo** 

Diseñar, simular, construir y evaluar un controlador PID analógico, implementado con amplificadores operacionales, que mejore la respuesta transitoria de una planta RLC subamortiguada. La sintonía inicial se obtiene con el método de oscilaciones sostenidas (Ziegler-Nichols en lazo cerrado) y se refina mediante simulación en MATLAB. 

# **2. Descripción del sistema** 

# **2.1 Planta RLC** 

Cada equipo construye un circuito RLC serie cuya salida se toma en el capacitor. Los valores de R, L y C se eligen de modo que el factor de amortiguamiento medido esté en el intervalo: 

𝟎. 𝟏𝟓≤𝜻≤𝟎. 𝟑𝟓 

- Se recomienda 𝐿= 100 𝑚𝐻 y 𝐶= 100 𝑛𝐹 (𝜔ₙ ≈10 𝑘𝑟𝑎𝑑/𝑠), con una resistencia ajustable en serie. 

- La resistencia total del lazo (potenciómetro + resistencia DC del inductor + salida del driver) determina ζ. El alumno debe medir ζ a partir del sobrepaso del escalón en lazo abierto y reportarlo. 

# **2.2 Etapa RC adicional (planta de 3er orden)** 

Los alumnos deben agregar a la planta un circuito RC con su respectivo seguidor de tensión (aislamiento), de modo que el conjunto pase a ser un sistema de 3er orden. Con esta etapa la planta alcanza el límite de estabilidad con una ganancia proporcional finita, lo que permite aplicar el método de oscilaciones sostenidas. Los valores de R y C de la etapa son parte del diseño; en el Anexo A se muestran valores sugeridos. 

El diagrama de bloques del sistema y el circuito completo se presentan en el Anexo A. 

# **3. Método de sintonía: oscilaciones sostenidas** 

Se utiliza únicamente el método de Ziegler-Nichols en lazo cerrado: 

1. Desactivar las acciones integral y derivativa (𝐾ᵢ= 0 y 𝐾𝑑 = 0). 

2. Incrementar la ganancia proporcional hasta obtener una oscilación sostenida de amplitud constante en la salida, sin saturar los opamps. 

Proyecto Intermedio Teoría de Control II 



<!-- Start of picture text -->
~—<br>Cr<br><!-- End of picture text -->



<!-- Start of picture text -->
Be<br>30<br><!-- End of picture text -->

3. Registrar con el osciloscopio la ganancia última 𝐾𝑐𝑟 y el periodo de oscilación 𝑃𝑐𝑟. 

4. Calcular los parámetros iniciales con la tabla siguiente. 

5. Verificar 𝐾𝑐𝑟 y 𝑃𝑐𝑟 con el modelo en MATLAB (por ejemplo, con margin()) y comparar con lo medido. 

En el circuito se ajustan las ganancias independientes de cada rama: 𝐾ₚ, 𝐾ᵢ= 𝐾ₚ/𝑇ᵢ  𝑦 𝐾𝑑 = 𝐾ₚ · 𝑇𝑑. 

Sintonía fina en MATLAB: modelar la planta con los parámetros medidos, simular el escalón incluyendo la saturación de los opamps, ajustar 𝐾ₚ, 𝑇ᵢ y 𝑇𝑑 con criterio, comparar con pidtune y trasladar los valores finales a los potenciómetros. 

# **4. Actividades y entregables** 

1. Planta: armar el RLC y la etapa RC, medir 𝑀𝑝, 𝜔ₙ y 𝜁, y obtener la función de transferencia. 

2. Sintonía inicial: obtener 𝐾𝑐𝑟 y 𝑃𝑐𝑟 y calcular 𝐾ₚ, 𝑇ᵢ y 𝑇𝑑. 

3. MATLAB/Simulink: simular con step, margin y rlocus, incluir saturación de ±12 V y hacer el ajuste fino. 

4. Diseño circuital: calcular los valores de R y C del PID, verificar en un SPICE y construir el circuito. 

5. Medición: comparar lazo abierto, lazo cerrado simulado y lazo cerrado medido. 

6. Reporte y demostración. 

# **5. Especificaciones de desempeño** 

- Error en estado estable nulo. 

- Sobrepaso 𝑀𝑝≤15%. 

- Tiempo de asentamiento menor que el de lazo abierto. 



<!-- Start of picture text -->
cy<br><!-- End of picture text -->

|**6. Rúbrica de e**<br> <br><br>|P<br> <br>**valuación (100 pts**<br> <br>|royecto Intermedio<br>Teoría de Control II<br>**)**<br> <br>|<br> <br>|**i**<br><br>|
|---|---|---|---|---|
|**Criterio**<br>|**Excelente**<br>|**Satisfactorio**<br>|**Básico**<br>|**Insuficiente**<br>|
|**Modelado de la**<br>**planta (10)**<br>|Función de transferencia<br>de 3er orden con ζ y𝜔ₙ<br>medidos y calculados,<br>comparados con los<br>teóricos; considera DCR<br>y tolerancias (9–10)<br>|Modelo correcto, con<br>diferencias sin explicar<br>(7–8)<br>|Modelo parcial o sin<br>medición (5–6)<br>|Sin modelo o erróneo (0–<br>4)<br>|
|**Sintonía inicial**<br>**(15)**<br>|𝐾𝑐𝑟y𝑃𝑐𝑟medidos con<br>osciloscopio y<br>verificados con margin();<br>Kₚ, Tᵢy𝑇𝑑calculados<br>correctamente (13–15)<br>|Procedimiento correcto<br>con errores menores en<br>la medición o el cálculo<br>(10–12)<br>|Método aplicado de<br>forma mecánica, sin<br>verificar (7–9)<br>|Método mal aplicado o<br>ausente (0–6)<br>|
|**Simulación y**<br>**ajuste fino (20)**<br>|Simula con saturación,<br>itera con criterio,<br>compara con pidtune y<br>justifica cada ajuste (18–<br>20)<br>|Ajuste fino correcto con<br>justificación parcial (14–<br>17)<br>|Simula sin iteración<br>razonada (10–13)<br>|Sin simulación o<br>resultados incoherentes<br>(0–9)<br>|
|**Diseño circuito**<br>**(15)**<br>|PID con filtro derivativo,<br>reset del integrador,<br>valores comerciales<br>calculados y verificados<br>en un SPICE (13–15)<br>|Diseño funcional con<br>omisiones menores (10–<br>12)<br>|Topología correcta, pero<br>valores sin verificar (7–9)<br>|Diseño incorrecto (0–6)<br>|
|**Implementación y**<br>**medición (20)**<br>|Cumple las<br>especificaciones;<br>capturas de osciloscopio<br>de lazo abierto y cerrado;<br>cuantifica Mp, ts y ess<br>(18–20)<br>|Funciona, cumple<br>parcialmente las<br>especificaciones (14–17)<br>|Funciona, pero sin<br>mediciones adecuadas<br>(10–13)<br>|No funciona o no se<br>midió (0–9)<br>|
|**Análisis y**<br>**discusión (10)**<br>|Compara simulación y<br>medición, explica<br>discrepancias<br>(tolerancias, DCR, GBW)<br>y limitaciones del<br>método (9–10)<br>|Comparación correcta<br>con explicación<br>superficial (7–8)<br>|Solo describe resultados<br>(5–6)<br>|Sin análisis (0–4)<br>|
|**Reporte y**<br>**comunicación (10)**<br>|Claro, ordenado, figuras<br>legibles, referencias,<br>demostración fluida (9–<br>10)<br>|Buen reporte con<br>detalles menores por<br>pulir (7–8)<br>|Reporte incompleto o<br>desordenado (5–6)<br>|Deficiente (0–4)<br>|



Proyecto Intermedio Teoría de Control II 



<!-- Start of picture text -->
Cié<br>f v)<br><!-- End of picture text -->



<!-- Start of picture text -->
2.J (/h)<br>InGenieria en<br>€LecTROnica<br><!-- End of picture text -->

# **Anexo A. Esquema del circuito** 

# **A.1 Diagrama de bloques** 



<!-- Start of picture text -->
r(t) + e(t) | Controlador PID | u(t) Planta RLC Etapa RC agregada y(t)<br>() analégico subamortiguada por el alumno<br>- (opamps) 7 (0.15 sf $0.35)7 (3.er orden) |<br>Realimentaci6n unitaria<br><!-- End of picture text -->

_Figura 1. Lazo de control con realimentación unitaria._ 

# **A.2 Planta de 3er orden (RLC + etapa RC)** 



<!-- Start of picture text -->
Ry= 20 kO Oyit)<br>Ry |<br>(pot 1k + 1000) += 100 mH<br>u(t)o Wu<br>| C= 100nF l C= 10nF<br><!-- End of picture text -->

_Figura 2. RLC serie con salida en C, seguidor, etapa RC (agregada por el alumno) y seguidor de salida._ 

Proyecto Intermedio Teoría de Control II 



<!-- Start of picture text -->
C ~_<br>t 4<br><!-- End of picture text -->



<!-- Start of picture text -->
s<br>Ingenieria€LEcTRONICAaen<br><!-- End of picture text -->

# **A.3 Controlador PID analógico (forma paralela)** 



<!-- Start of picture text -->
feiprs010<br>f<br>sia > 100<br>Se<br>10K0 °F ‘Sumador inversor<br>Wve<br>boa<br>vei na pot 10040,<br>‘wey 22<br>i Integra: -Kefeat<br>futpt2010<br>/<br>Centon R=s800 > 1x0<br><!-- End of picture text -->

_Figura 3. Restador, ramas P, I y D inversoras y sumador inversor (la doble inversión entrega u(t) con signo positivo)._ 

