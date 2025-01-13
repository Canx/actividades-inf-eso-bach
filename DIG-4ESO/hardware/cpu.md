## **Unidad Central de Procesamiento (CPU)**

### **1. ¿Qué es la CPU?**
- Es el "cerebro" del ordenador.
- Se encarga de interpretar y ejecutar las instrucciones de los programas.
- Procesa datos de entrada y genera resultados en forma de salida.

---

### **2. Componentes principales de la CPU**

#### **Unidad Aritmético-Lógica (ALU)**
- Realiza cálculos matemáticos básicos (suma, resta, multiplicación, división).
- Ejecuta operaciones lógicas (comparaciones como mayor que, menor que, igual a).

#### **Unidad de Control (CU)**
- Coordina el flujo de datos entre los distintos componentes del ordenador.
- Traduce las instrucciones del programa en señales que activan los componentes correspondientes.

#### **Registros**
- Pequeñas unidades de memoria interna de alta velocidad.
- Almacenan temporalmente datos que están siendo procesados por la CPU.
- Ejemplo: Registro acumulador, contador de programa.

#### **Caché**
- Memoria rápida integrada en la CPU.
- Almacena datos e instrucciones usados con frecuencia para un acceso más rápido.
- **Niveles de caché**:
  - **L1**: Más rápida pero con menor capacidad.
  - **L2**: Más grande que L1, pero más lenta.
  - **L3**: Compartida entre todos los núcleos, es la más lenta pero también la de mayor capacidad.

---

### **3. Características clave de la CPU**

#### **Velocidad del reloj**
- Se mide en **gigahercios (GHz)**.
- Indica cuántas operaciones puede realizar por segundo.
- Ejemplo: Una CPU a 3.5 GHz puede realizar 3,500 millones de ciclos por segundo.

#### **Núcleos**
- Cada núcleo es una unidad de procesamiento independiente.
- Permite realizar varias tareas simultáneamente (procesamiento paralelo).
- Ejemplo: Un procesador de 8 núcleos puede ejecutar 8 tareas al mismo tiempo.

#### **Hilos (Threads)**
- Los hilos son las tareas que un núcleo puede manejar simultáneamente.
- Tecnologías como **Hyper-Threading** (Intel) o **SMT** (AMD) permiten que un núcleo maneje múltiples hilos.

#### **Arquitectura**
- Define cómo está diseñada y organizada la CPU.
- Ejemplos:
  - **x86**: Arquitectura común en ordenadores personales.
  - **ARM**: Usada en dispositivos móviles por su eficiencia energética.

#### **Instrucciones por Ciclo (IPC)**
- La cantidad de instrucciones que una CPU puede ejecutar en cada ciclo de reloj.
- A mayor IPC, mejor rendimiento.

#### **TDP (Potencia de diseño térmico)**
- Medida de la cantidad de calor que genera la CPU bajo carga.
- Influye en el tipo de sistema de refrigeración necesario.

---

### **4. Funcionamiento de la CPU**
La CPU realiza su trabajo en 3 pasos principales:

#### 1. **Búsqueda (Fetch)**
- La CPU obtiene las instrucciones desde la memoria RAM.

#### 2. **Decodificación (Decode)**
- La unidad de control traduce las instrucciones en señales que pueden ser entendidas por la CPU.

#### 3. **Ejecución (Execute)**
- La ALU realiza los cálculos necesarios.
- Los resultados se almacenan en los registros o se envían de vuelta a la memoria.

---

### **5. Tipos de CPU**

#### **Por fabricante**
- **Intel**: Línea Core (i3, i5, i7, i9) y Xeon.
- **AMD**: Ryzen (3, 5, 7, 9) y EPYC (para servidores).
- **ARM**: Usadas en móviles y tablets (Apple Silicon, Qualcomm Snapdragon).

#### **Por propósito**
- **Procesadores de escritorio**: Potencia balanceada para tareas generales.
- **Procesadores de servidores**: Diseñados para manejar múltiples usuarios y cargas pesadas.
- **Procesadores móviles**: Optimizados para eficiencia energética.

---

### **6. Tecnologías comunes en CPUs modernas**

#### **Hyper-Threading (Intel) y SMT (AMD)**
- Permiten a un núcleo manejar más de un hilo simultáneamente, mejorando el rendimiento multitarea.

#### **Overclocking**
- Incrementar la frecuencia de reloj para obtener un rendimiento mayor al especificado por el fabricante.
- Requiere sistemas de refrigeración eficientes para evitar sobrecalentamiento.

#### **Virtualización**
- Permite a la CPU ejecutar múltiples sistemas operativos en un solo hardware físico.
- Importante para servidores y entornos empresariales.

---

### **7. Factores importantes al elegir una CPU**

#### **Uso**
- **Gaming**: Prioriza núcleos y frecuencia.
- **Edición de video/diseño 3D**: Más núcleos y mayor caché.
- **Tareas cotidianas**: CPUs básicas son suficientes.

#### **Compatibilidad**
- Verifica el **socket** y el **chipset** compatibles con la placa base.

#### **Presupuesto**
- CPUs de gama baja ofrecen buen rendimiento para tareas básicas.
- CPUs de gama alta son ideales para tareas avanzadas y profesionales.
