# Usar una imagen base de Python
FROM python:3.13-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos e instalar dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el resto de los archivos
COPY . .

# Exponer el puerto que usa Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "reader.py", "--host", "0.0.0.0"]
