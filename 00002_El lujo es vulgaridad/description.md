Ahora vamos a trabajar con recetas como éstas: 

```python
empanadas = {
  "nombre": "empanadas de carne",
  "ingredientes": [ "carne picada", "aceitunas", "cebolla", "tapa de empanadas" ]
}

guiso_de_lentejas = {
  "nombre": "guiso de lentejas",
  "ingredientes": [ "tomate", "lentejas", "cebolla" ]
}

queso_y_dulce = {
  "nombre": "queso y dulce",
  "ingredientes": [ "queso", "dulce de membrillo" ]
}
```

> Definí una función `es_sofisticada` que tome una receta y nos diga si la cantidad de ingredientes es mayor o igual a 4. 
> 
> ```python
> >>> es_sofisticada(empanadas)
> True
> >>> es_sofisticada(guiso_de_lentejas)
> False
> >>> es_sofisticada(queso_y_dulce)
> False
> ```