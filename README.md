# Proyecto4
# PROYECTO DE ANÁLISIS DE DATOS GEOESPACIALES

En este proyecto el objetivo será buscar la ubicación ideal para una empresa basándonos en las necesidades y gustos de sus trabajadores. Para ello tendremos que utulizar la base de datos "companies" de Mongodb, que es una base de datos en la que se almacenan determinados datos de compañias alrededor del mundo y que, si bien no está actualizada a la última, sí que es lo suficientemente amplia como para utilizar de punto de partida y después utilizar herramientas geoespaciales para poder encontrar aquellos lugares ideales para los trabajadores.



## 1 .  Filtrado inicial:

Filtraré en mongob para obtener algunas ubicaciones concretas por donde empezar a buscar.

## 2. Geoquerys:

Utilizaré la api de Google Places para poder consultar las localizaciones conseguidas anteriormente en relación a las necesidades de la plantilla.

## 3. Puntuación:

Con los datos obtenidos de las geoquerys estableceré la ubicación ideal para ubicar la empresa.

## 4. Visualización:
    ### 4.1 Recopilación:
            Recopilaré datos para poder mostrarlos luego.
    ### 4.2 Visualización:
            Utilizaré la libreria Kepler para ver la ubicación de los elementos.
       

## Archivos incluidos:

1. Este README
2. Una carpeta llamada src con:
      **El Jupyter Notebook principal, llamado "p3"**
      Un archivo de python con las funciones utilizadas llamado "geofunciones"
3. Una carpeta llamada "mapa" con la visualización en formato html
4. Un archivo de texto con los requirements
5- Un archivo yml con el entorno utilizado



## Librerias:

Para todo esto, hemos utilizado las siguientes librerias:

[pymongo] (https://pymongo.readthedocs.io/en/stable/)
[pandas] (https://pandas.pydata.org/docs/)
[json] (https://docs.python.org/3/library/json.html)
[pandas.io.json] (https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html)
[googlemaps] (https://github.com/googlemaps/google-maps-services-python)
[datetime] (https://docs.python.org/3/library/datetime.html)
[requests] (https://docs.python-requests.org/es/latest/)
[dotenv] (https://pypi.org/project/python-dotenv/)
[os] (https://docs.python.org/3/library/os.html)
[keplergl] (https://docs.kepler.gl/)
[operator] (https://docs.python.org/3/library/operator.html)
[functools] (https://docs.python.org/3/library/functools.html)

## Links utilizados
https://developers.google.com/maps/documentation/places/web-service/search
https://es.stackoverflow.com/
https://www.delftstack.com/es/
https://github.com/Ironhack-Data-Madrid-Marzo-2021/Classroom-Materials-FT

