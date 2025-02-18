# Proyecto de Comunicación Cliente-Servidor

Este proyecto implementa una comunicación entre un servidor y múltiples clientes utilizando sockets TCP, además de una API en Flask para visualizar los mensajes recibidos.

## Tecnologías Usadas

- Python (Sockets, Flask, Tkinter)
- JSON (Archivos de configuración)
- PHP (Interfaz web)
- Tkinter (Interfaz gráfica del cliente)

## Estructura del Proyecto

```
├── cliente.py           # Cliente basado en consola (TCP)
├── cliente_gui.py       # Cliente con interfaz gráfica (Tkinter)
├── servidor.py          # Servidor TCP que recibe y almacena mensajes
├── apy.py               # API Flask para visualizar los mensajes almacenados
├── index.php            # Interfaz web para mostrar mensajes del servidor
├── client_config.json   # Configuración del cliente (IP y Puerto del servidor)
├── server_config.json   # Configuración del servidor (IP, Puerto y archivo de mensajes)
├── mensajes.txt         # Archivo donde el servidor almacena los mensajes
```

## Instalación y Configuración

### Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### Configurar los archivos JSON

**client_config.json** (Configuración del cliente):

```json
{
    "server_host": "217.154.4.86",
    "server_port": 3000
}
```

**server_config.json** (Configuración del servidor):

```json
{
    "host": "0.0.0.0",
    "port": 3000,
    "message_file": "mensajes.txt"
}
```

## Ejecución del Proyecto

### Iniciar el Servidor TCP

```bash
python servidor.py
```

### Ejecutar un Cliente

**Modo Consola**:

```bash
python cliente.py
```

**Modo Gráfico**:

```bash
python cliente_gui.py
```

### Levantar la API Flask (Opcional)

```bash
python apy.py
```

Luego, accede a los mensajes en:

```
http://217.154.4.86:5000/mensajes
```

## Funcionamiento

1. El servidor escucha conexiones de clientes en el puerto 3000.
2. Los clientes pueden enviar mensajes que el servidor recibe y almacena en `mensajes.txt`.
3. La API en Flask permite consultar los mensajes en formato JSON.
4. Se incluye una interfaz gráfica en Tkinter y una web en PHP (`index.php`).

## Posibles Errores y Soluciones

**Error de conexión del cliente**  
Verifica que el servidor está corriendo y que la IP/Puerto en `client_config.json` es correcta.

**El servidor no arranca**  
Asegúrate de que el puerto 3000 no esté en uso y que el archivo `server_config.json` está bien configurado.



