# Pruebas de modelos de intenciones y entidades - práctica modelo conversacional

## Desplegar online usando streamlit
Gracias a usar streamlit se puede hostear la aplicación en su comunidad a través de Github permitiendo el acceso simplemente desde esta url:

- https://modelo-conver-alvaro.streamlit.app

---

## Desplegar en local

Para desplegar la aplicación en local hay que tener las librerías instaladas, además de cargar las variables de entorno pertinentes. 

### 1. Crear un entorno virtual 

Lo primero es crear un entorno virtual y desplegarlo para que no se queden en nuestra máquina las librerías descargadas.

```bash
python -m venv .venv
```

### 2. Activar el entorno virtual
Ahora tenemos que activar el entorno para que las librerías se descarguen en él.

- Para windows
    ```bash
    .venv\Scripts\activate
    ```

- Para linux
    ```bash
    source .venv/bin/activate
    ```

### 3. Descargar librerías
Una vez activado podemos descargar las librerías necesarias
```bash
pip install python-dotenv
pip install streamlit
pip install azure-ai-language-conversations
```

### 4. Definir `.env`
Cuando ya estén instaladas tenemos que definir un archivo `.env` con la siguiente estructura:
```
LS_CONVERSATIONS_ENDPOINT=<endpoint_language_azure>
LS_CONVERSATIONS_KEY=<key_language_azure>
PROJECT_NAME=<nombre_proyecto>
DEPLOYMENT_NAME=<nombre_despliegue>
```

En caso de que quieras utilizar el que yo he hecho mandame un correo a alvaro.diez@tajamar365.com

### 5. Lanzar proyecto
Con todo ya correctemente hecho y definido, lanzamos la aplicación.
```bash
streamlit run modelo-conv-intenciones.py
```



