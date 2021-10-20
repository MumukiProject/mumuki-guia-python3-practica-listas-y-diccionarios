Necesitamos que nuestro menú tenga opciones sin tacc. Por eso definimos una lista de ingredientes que no tienen tacc:

```python
ingredientes_sin_tacc = ["tomate", "aceitunas", "cebolla", "carne picada", "lentejas"]
```

> Aprovechando la variable global `ingredientes_sin_tacc`, definí una función `apto_celiacos` que nos diga si todos los ingredientes son sin tacc. 
>
> ```python
> >>> apto_celiacos(guiso_de_lentejas)
> True
> >>> apto_celiacos(empanadas)
> False # porque las tapas de empanadas tienen tacc
```