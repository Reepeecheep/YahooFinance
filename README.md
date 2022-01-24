# YahooFinance
Notificaciones sobre cambios en las bolsas Nikkei 225, DAX Index y Nasdaq. Usando https://www.yahoofinanceapi.com/


## Instrucciones para ejecutar el programa

1. Crear el entorno virtual:

```
python3 -m venv nombre_env
```  

> Nota: Nombrar el enterno virtual diferente de **env**, ya que el archivo **.env** lo utilizaremos para guardar key del API que nos proporciona Yahoo Finance

2. Activar el entorno virtual

```
source nombre_env/bin/activate
```

3. Instalar las dependencias de pip

```
pip install -r requirements.txt
``` 

4. Crear archivo **.env** y dentro colocar nuestra variable para el uso de la API

```
API_SECRET_KEY=TU_API
```

5. Ejecutar en un terminal

```
python3 main.py
```

## Video explicando el código

https://youtu.be/rqqj1gVdq_A


## VIdeo del programa en ejecución

https://youtu.be/-bUyNNwmcqA

