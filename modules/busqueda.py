def buscar(query):
    """Busca un término en una lista de datos."""
    datos = ["proyecto1", "proyecto2", "simulación", "análisis"]
    resultados = [dato for dato in datos if query.lower() in dato.lower()]
    return resultados

def buscar_avanzado(query, lista_datos):
    """Busca un término en una lista de datos con búsqueda avanzada."""
    resultados = [dato for dato in lista_datos if query.lower() in dato.lower()]
    return resultados

def buscar_en_dataframe(df, columna, valor):
    """Busca un valor en una columna de un DataFrame."""
    if columna in df.columns:
        return df[df[columna].str.contains(valor, case=False)]
    return "Error: Columna no encontrada."

def buscar_por_filtro(df, filtros):
    """Filtra un DataFrame según condiciones dadas."""
    return df.query(filtros)

def buscar_por_columna(df, columna, valor):
    """Busca filas en un DataFrame donde la columna tiene un valor específico."""
    if columna in df.columns:
        return df[df[columna] == valor]
    return "Error: Columna no encontrada." 