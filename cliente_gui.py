import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import socket
import json
import threading

def load_client_config(config_path='client_config.json'):
    """Carga la configuración del cliente desde un archivo JSON."""
    try:
        with open(config_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la configuración: {e}")
        return None

def send_message():
    """Envía un mensaje al servidor y muestra la respuesta."""
    message = message_entry.get()
    if not message.strip():
        return
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_host.get(), int(server_port.get())))
        client_socket.sendall(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        client_socket.close()
        
        chat_area.insert(tk.END, f"[Tú]: {message}\n", "user_message")
        chat_area.insert(tk.END, f"[Servidor]: {response}\n", "server_message")
        message_entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")

def start_client_gui():
    """Carga la configuración y lanza la interfaz gráfica."""
    global server_host, server_port, message_entry, chat_area
    
    config = load_client_config()
    if config is None:
        return

    root = tk.Tk()
    root.title("Cliente TCP")
    root.geometry("400x450")
    root.resizable(False, False)
    root.configure(bg="#2c3e50")
    
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 10), padding=5)
    style.configure("TLabel", font=("Arial", 10), background="#2c3e50", foreground="white")
    
    frame = ttk.Frame(root, padding=10)
    frame.pack(expand=True, fill=tk.BOTH)
    
    ttk.Label(frame, text="Servidor IP:").pack(anchor="w")
    server_host = tk.StringVar(value=config['server_host'])
    ttk.Entry(frame, textvariable=server_host).pack(fill=tk.X)
    
    ttk.Label(frame, text="Puerto:").pack(anchor="w")
    server_port = tk.StringVar(value=str(config['server_port']))
    ttk.Entry(frame, textvariable=server_port).pack(fill=tk.X)
    
    chat_area = scrolledtext.ScrolledText(frame, width=50, height=15, wrap=tk.WORD, bg="#ecf0f1", fg="#2c3e50")
    chat_area.pack(pady=5)
    chat_area.tag_configure("user_message", foreground="#2980b9", font=("Arial", 10, "bold"))
    chat_area.tag_configure("server_message", foreground="#27ae60", font=("Arial", 10, "italic"))
    
    message_entry = ttk.Entry(frame, width=50)
    message_entry.pack(pady=5, fill=tk.X)
    
    send_button = ttk.Button(frame, text="Enviar", command=send_message)
    send_button.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    start_client_gui()
