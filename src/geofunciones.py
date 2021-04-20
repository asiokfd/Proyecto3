def geocode(address):
     """
    Saca las coordenadas de una dirección que le des.
    """
     data = requests.get(f"https://geocode.xyz/{address}?json=1").json()
     try:
        return {
            "type":"Point",
            "coordinates":[float(data["latt"]),float(data["longt"])]}
     except:
        return data


def loc_decimo (dicfromgoogle):
     
     """ Recibe como parámetro una respuesta de googleapi y retorna la localización del décimo elemento"""

     return dicfromgoogle ["results"][9]["geometry"]["location"]


def distancia_entre (origen, destino):  
    """
    Recibe como parámetros 2 coordenadas y nos devuelve la distancia entre ellas en metros y en valor numérico
    
    :param origins: One or more addresses, Place IDs, and/or latitude/longitude
        values, from which to calculate distance and time. Each Place ID string
        must be prepended with 'place_id:'. If you pass an address as a string,
        the service will geocode the string and convert it to a
        latitude/longitude coordinate to calculate directions.
    
    :type origins: a single location, or a list of locations, where a
        location is a string, dict, list, or tuple
    
    :param destinations: One or more addresses, Place IDs, and/or lat/lng values
        , to which to calculate distance and time. Each Place ID string must be
        prepended with 'place_id:'. If you pass an address as a string, the
        service will geocode the string and convert it to a latitude/longitude
        coordinate to calculate directions.
    
    :type destinations: a single location, or a list of locations, where a
        location is a string, dict, list, or tuple
    """ #copiado de la función original
    
    averquenossale=gmaps.distance_matrix (origen, destino) #esta sería la función original de la librería
    
    return averquenossale["rows"][0]["elements"][0]["distance"]["value"]# y le decimos que nos retorne lo que nos interesa


def getFromDict(diccionario,mapa):
    """" 
    Esta función recibe 2 parámetros, un diccionario de diccionarios y una lista de strings  realizada "ad hoc" para 
        ese diccionario, esos strings serán las keys por las que entrará la función para retornarnos el value del último string
    """

    return reduce(operator.getitem,mapa,diccionario)