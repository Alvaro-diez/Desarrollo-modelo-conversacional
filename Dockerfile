# Usar la imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto utilizado por Streamlit
EXPOSE 8501

# Copiar y exportar las variables de entorno desde el archivo .env
COPY .env .env
RUN export $(cat .env | xargs)

# Comando para ejecutar la aplicación Streamlit
CMD ["streamlit", "run", "modelo-conv-intenciones.py"]
