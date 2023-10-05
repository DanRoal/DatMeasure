# DatMeasure

## ¿Qué es DatMeasure?

<p style="text-align: justify;">
Es una aplicación de código abierto auxiliar en las tareas relacionadas con el cálculo estadístico de las incertidumbres.
</p>

## ¿Para qué sirve?

Calcula las incertidumbres a partir del conjunto de datos proporcionados por el usuario.
Puede realizar cálculos para mediciones directas o indirectas.

## Cómo funciona

<p style="text-align: justify;">
La app realiza cálculos automatizados de dos tipos de incertidumbres presentes en la experimentación: desviación entre datos y desviación entre resultados.
</p>
<p style="text-align: justify;">
La desviación entre datos se calcula en los casos donde se toman varias mediciones de un mismo punto. Por ejemplo, al calcular la velocidad de un objeto tomando varias mediciones de distancia y tiempo de la sigiente forma:
</p>

![imagen]

<p style="text-align: justify;">
 El primer paso consiste en obtener la desviación estándar para cada una de las variables usando su respectivo promedio. A continuación se calculan las incertidumbres nominal, estadística, y absoluta de la siguiente forma:
</p>

$$
\begin{align}
\sigma_{est} &= \sqrt{\sum_{i=1}^n (\frac{\partial f}{\partial x_i} S_ {x_i})^2} &
\sigma_{nom} &= \sqrt{\sum_{i=1}^n (\frac{\partial f}{\partial x_i} \Delta x_i)^2}
\end{align}
$$

En donde $x_i$ representa cada una de las variables, $f$ es la función de la medición indirecta, $S_{x_i}$ la desdviación estandar de la variable $x_i$, y $\Delta x_i$ la incertidumbre de apreciación asociada a la variable $x_i$

<p style="text-align: justify;">
Conocer la desviación entre resultados es útil, cuando los datos que se obtuvieron fueron del mismo fenómeno, pero no se tomaron con configuraciones iguales; es decir, usando el ejemplo anterior, la gráfica de datos obtenidos al calcular la velocidad de un objeto, debería de verse de la siguiente forma:
</p>

![imagen2]

<p style="text-align: justify;">
En este caso, la aplicación evalúa cada conjunto de datos dado para cada uno de los puntos en la ecuación provista. En términos del ejemplo, calcula la velocidad con los tres pares de datos obtenidos para la distancia y el tiempo. Enseguida, la aplicación calcula la desviación estandar del conjunto de evaluaciones y obtiene su incertidumbre estadística tal y como se describe en la ecuacion (1)
</p>
<p style="text-align: justify;">
En ambos casos, para calcular la incertidumbre absoluta, se suma en cuadratura la incertidumbre nominal y estadística:
</p>

$$
\begin{equation}
\sigma_{abs} = \sqrt{\sigma_{est}^2 +\sigma_{nom}^2 }
\end{equation}
$$

## ¿Cómo se diseñó?

El lenguaje de programación que se utilizó para el desarrollo de la aplicación fue Python.

<p style="text-align: justify;">
Usando la librería Pandas se extrae la información de los archivos provistos por el usuario, y se almacenan en listas. Con las librerías Numpy y Sympy se crearon las funciones que hacen los calculos matemáticos requerídos. Por último, se utilizó Tkinter y CustomTkinter para crear una interfaz intuitiva, simple de usar y visualmente atractiva.
</p>

![Imagen3]

Después de llenar las casillas necesarias, se despliega una nueva ventana en la cual se pueden introducir los datos experimentales para cada variable.

![imagen4]

Una vez cargados todos los datos, se obtienen los tres tipos de incertidumbre: la nominal, estadística y absoluta.

## Alcance y retos

<p style="text-align: justify;">
Para los alumnos, la aplicación les ayudará a reducir significativamente el tiempo empleado en realizar demasiados cálculos, que llegan a ser complejos, y así centrarse más en el tema del experimento que estén llevando a cabo en el laboratorio. Para los profesores, de igual modo, les brindará apoyo en la evaluación de los informes de laboratorio que presentan los estudiantes.
</p>
<p style="text-align: justify;">
DatMeasure acepta como datos de entrada texto plano o tablas de datos en formatos .csv y .xlsx. El programa se pensó para implementarse en un contexto educativo; sin embargo, posee un gran potencial para usarse en un ámbito profesional.
</p>

<p style="text-align: justify;">
En el campo de la física calcular las incertidumbres tiene un papel de vital importancia, porque los resultados de cualquier experimento solo tendrán validez si también se reportan correctamente esas incertidumbres. Tener una aplicación que permita obtenerlas de manera sencilla y rápida, sirve para mantener el rigor científico que requiere la ciencia experimental.
</p>
