def conjunto_potencia(conjunto):
    """Genera el conjunto potencia de un conjunto dado."""
    CP = ['∅']
    # Empezamos con el conjunto vacío
    for elem in conjunto:
        # Agregamos cada nuevo elemento a todos los subconjuntos existentes
        nuevos_subconjuntos = []
        for subset in CP:
            if subset == '∅':
                nuevos_subconjuntos.append("{" + elem + "}")
            else:
                nuevos_subconjuntos.append(subset[:-1] + ", " + elem + "}")
        CP.extend(nuevos_subconjuntos)
    return CP

conjunto = input("Ingrese un conjunto separado por comas: ").split(",")
conjunto = [elemento.strip() for elemento in conjunto]
print(conjunto_potencia(conjunto))