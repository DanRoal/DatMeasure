# Bienvenid@ a mi aplicación para calcular incertidumbres

Hola! Esta es mi primer proyecto *en serio* que hago. La idea es hacer una aplicacioón descargable opensource que calcule incertidumbres dada una ecuación y un arreglo de datos asociados a mediciones hechas en laboratorio.

Sin embargo el autor ahora mismo ~~no sabe como hacer aplicaciones xd~~ no dispone de los conocimientos necesarios para hacer una aplicación completamente funcional. Sin embargo lo que el autor sí sabe es escribir un poco de python y usar jupyter notebooks ((masomenos)).

## OPCIONES DISPONIBLES

Dado que este proyecto personal estará enfocado en documentar mi propio proceso de aprendizaje a la vez que produzco algo tangible y que se pueda usar, conforme pase el tiempo y aprenda más, nuevas funciones serán agregadas pero de mientras lo único disponible será:

* Notebook de Jupyter.
* Módulo de funciones de Python.

Las funciones que planeo agregar son:

* Aplicación descargable.
* Integración de archivos .xlsx (Excel).
* Opción de ingresar ya sea archivos de texto numérico o comandos de $\LaTeX$
* ~~Un taco de bienvenida~~

## Cálculo de incertidumbres

¿Cómo es que voy a calcular las incertidumbres? La respuesta es simple, usando ésta fórmula:

$$
\Delta f(x_0, x_1, ...) = \Delta f(x_0,x_1,x_2,...) =  \sqrt{(\sigma_{nom})^2 + (\sigma_{est})^2}
$$

Donde $\sigma_{nom}$ representa la incertidumbre nominal de nuestra medición indirecta y donde $\sigma_{est}$ representa la incertidumbre estadística asociada a la función $f$.

La incertidumbre nominal y estadísiticas estarán calculadas de la siguiente manera:

$$
\sigma_{nom} = \sqrt{\sum_{i=0}^N (\frac{\partial f}{\partial x_i})^2 \sigma_{ap}^2}
$$

$$
\sigma_{est} = \sqrt{\sum_{i=0}^N (\frac{\partial f}{\partial x_i})^2 S_{x_i}^2}
$$

En donde $\sigma_{ap}$ representa la incertidumbre de apreciación, i.e. La incertidumbre debida a la resolución de nuestro instrumento de medición. $S_{x_i}$ Representa la desviación estandar asociada a cada una de las muestras tomadas de la variable $x_i$ Asumiendo una distribución normal.

Cabe aclarar que estamos tomando muchas restricciones, dado que estamos asumiendo que la parte no lineal de la función $f$ es no-significativa, y que úede ser despresiada en una expansión en serie de Taylor. Sin embargo debido a que este proyecto está pensado en ser usado en un laboratorio de enseñanza, La mayoría de funciones tratadas serán no tan no-lineales, o bueno eso espero.

Espero poder actualizar y agrgar más funciones en el futuro, por lo que la opción de calcular incertidumbres de funciones completamente no lineales eventualmente será agregada.

También cabe añadir que estamos reduciendo la incertidumbre absoluta dada por $\Delta f$ a la incertidumbre nominal y estadística, y aunque estricatmente esto es solo una parte de la misma, para propocitos de enseñanza es más que suficiente.
