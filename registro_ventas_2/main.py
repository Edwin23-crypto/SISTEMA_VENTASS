import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sqlite3
from fpdf import FPDF
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

from customtkinter import CTkImage
from PIL import Image


import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Configuración de colores de Instagram
instagram_colors = {
    "black"  : "black",
    "background": "black",
    "button_bg": "yellow",
    "button_fg": "white",
    "entry_bg": "white",
    "entry_fg": "black",
    "label_bg": "#E1306C",
    "label_fg": "white",
    "P": "green"
}




class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("VENTAS DE ARTICULOS DEPORTIVOS")
        self.root.geometry("1300x1300")
        self.root.configure(bg=instagram_colors["entry_bg"])

        self.logo_image = Image.open("sos.jpeg")
        self.logo_image = self.logo_image.resize((600, 200), Image.LANCZOS)
        self.logo_photo = CTkImage(self.logo_image, size=(600, 200))

        self.login_frame = ctk.CTkFrame(root, fg_color=instagram_colors["entry_fg"])
        self.login_frame.pack(fill=ctk.BOTH, expand=True, padx=50, pady=20)

        ctk.CTkLabel(self.login_frame, text=" ", image=self.logo_photo, fg_color=instagram_colors["entry_fg"]).pack(pady=100)
        ctk.CTkLabel(self.login_frame, text="Usuario:", font=("Helvetica", 14), text_color=instagram_colors["entry_bg"], fg_color=instagram_colors["background"]).pack(pady=10)
        self.username_entry = ctk.CTkEntry(self.login_frame, font=("Helvetica", 14), fg_color=instagram_colors["entry_bg"], text_color=instagram_colors["entry_fg"])
        self.username_entry.pack(pady=10)

        ctk.CTkLabel(self.login_frame, text="Contraseña:", font=("Helvetica", 14), text_color=instagram_colors["label_fg"], fg_color=instagram_colors["background"]).pack(pady=5)
        self.password_entry = ctk.CTkEntry(self.login_frame, show="*", font=("Helvetica", 14), fg_color=instagram_colors["entry_bg"], text_color=instagram_colors["entry_fg"])
        self.password_entry.pack(pady=5)

        ctk.CTkButton(self.login_frame, text="confirmar", command=self.check_login, font=("Helvetica", 18), fg_color=instagram_colors["button_bg"], text_color=instagram_colors["black"]).pack(pady=10)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.login_frame.pack_forget()
            self.open_main_window()
        else:
            messagebox.showwarning("Advertencia", "Nombre de usuario o contraseña incorrectos")

    def open_main_window(self):
        self.main_frame = ctk.CTkFrame(self.root, fg_color=instagram_colors["entry_fg"])
        self.main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        ctk.CTkLabel(self.main_frame, text=" ", image=self.logo_photo, fg_color=instagram_colors["entry_fg"]).pack(pady=40)
        ctk.CTkLabel(self.main_frame, text="ARTICULOS DEPORTIVOS", font=("Helvetica", 18), text_color=instagram_colors["label_fg"], fg_color=instagram_colors["background"]).pack(pady=20)

        ctk.CTkButton(self.main_frame, text="CLIENTES", command=self.open_clientes_window, font=("Times New Roman", 50), fg_color=instagram_colors["black"], text_color="yellow").pack(pady=10)
        ctk.CTkButton(self.main_frame, text="PRODUCTOS", command=self.open_productos_window, font=("Times New Roman", 50), fg_color=instagram_colors["black"], text_color="blue").pack(pady=10)
        ctk.CTkButton(self.main_frame, text="FACTURAS", command=self.open_facturas_window, font=("Helvetica", 50), fg_color=instagram_colors["black"], text_color="red").pack(pady=10)

    def open_clientes_window(self):
        self.root.iconify()  # Minimiza la ventana principal
        ClientesWindow(self.root)

    def open_productos_window(self):
        self.root.iconify()  # Minimiza la ventana principal
        ProductosWindow(self.root)

    def open_facturas_window(self):
        self.root.iconify()  # Minimiza la ventana principal
        FacturasWindow(self.root)

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import re

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import re

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import re

class ClientesWindow:
    def __init__(self, root):
        self.top = tk.Toplevel(root)
        self.top.title("Clientes")
        self.top.geometry("1300x700")
        self.top.configure(bg='lightblue')

        self.frame = tk.Frame(self.top, padx=5, pady=5, bg='lightblue')
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.frame, columns=("Cédula", "Nombre", "Apellido", "Email", "Teléfono", "Dirección"), show='headings')
        self.tree.heading("Cédula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.heading("Dirección", text="Dirección")

        self.tree.column("Cédula", width=100)
        self.tree.column("Nombre", width=150)
        self.tree.column("Apellido", width=150)
        self.tree.column("Email", width=200)
        self.tree.column("Teléfono", width=100)
        self.tree.column("Dirección", width=200)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.form_frame = tk.Frame(self.frame, padx=5, pady=5, bg='lightblue')
        self.form_frame.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(self.form_frame, text="Cédula:", bg='lightblue').grid(row=0, column=0, padx=5, pady=5)
        self.cedula_entry = tk.Entry(self.form_frame)
        self.cedula_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Nombre:", bg='lightblue').grid(row=1, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self.form_frame)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Apellido:", bg='lightblue').grid(row=2, column=0, padx=5, pady=5)
        self.apellido_entry = tk.Entry(self.form_frame)
        self.apellido_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Email:", bg='lightblue').grid(row=3, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.form_frame)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Teléfono:", bg='lightblue').grid(row=4, column=0, padx=5, pady=5)
        self.telefono_entry = tk.Entry(self.form_frame)
        self.telefono_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.form_frame, text="Dirección:", bg='lightblue').grid(row=5, column=0, padx=5, pady=5)
        self.direccion_entry = tk.Entry(self.form_frame)
        self.direccion_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Button(self.form_frame, text="Agregar Cliente", command=self.add_cliente, bg='lightgreen', fg='black').grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.form_frame, text="Editar Cliente", command=self.edit_cliente, bg='yellow', fg='black').grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.form_frame, text="Eliminar Cliente", command=self.delete_cliente, bg='red', fg='black').grid(row=8, column=0, columnspan=2, pady=10)
        tk.Button(self.form_frame, text="Actualizar Cliente", command=self.update_cliente, bg='blue', fg='white').grid(row=9, column=0, columnspan=2, pady=10)

        self.load_clientes()

    def load_clientes(self):
        conn = sqlite3.connect('ventas.db')
        c = conn.cursor()
        c.execute("SELECT * FROM clientes")
        clientes = c.fetchall()
        conn.close()

        for cliente in self.tree.get_children():
            self.tree.delete(cliente)

        for cliente in clientes:
            self.tree.insert('', tk.END, values=cliente)

    def validate_email(self, email):
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(email_regex, email)

    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) >= 10

    def validate_cedula(self, cedula):
        # Validar si la cédula es un número y tiene exactamente 10 caracteres
        return cedula.isdigit() and len(cedula) == 10

    def add_cliente(self):
        cedula = self.cedula_entry.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()
        direccion = self.direccion_entry.get()

        if not (cedula and nombre and apellido and email and telefono and direccion):
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")
           

        if not self.validate_cedula(cedula):
            messagebox.showwarning("Advertencia", f"La cédula '{cedula}' no es válida. Asegúrese de que tenga 10 dígitos.")
        

        if not self.validate_email(email):
            messagebox.showwarning("Advertencia", "El email no tiene un formato válido")
          

        if not self.validate_phone(telefono):
            messagebox.showwarning("Advertencia", "El teléfono debe contener solo dígitos y tener al menos 10 caracteres")
           

        conn = sqlite3.connect('ventas.db')
        c = conn.cursor()
        c.execute("INSERT INTO clientes (cedula, nombre, apellido, email, telefono, direccion) VALUES (?, ?, ?, ?, ?, ?)", 
                  (cedula, nombre, apellido, email, telefono, direccion))
        conn.commit()
        conn.close()

        self.load_clientes()
        self.clear_form()

    def clear_form(self):
        self.cedula_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)

    def edit_cliente(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor seleccione un cliente")
            return

        cliente = self.tree.item(selected_item)['values']
        self.clear_form()  # Limpiar el formulario antes de rellenar
        self.cedula_entry.insert(0, cliente[0])  # Mantener el cero
        self.nombre_entry.insert(0, cliente[1])
        self.apellido_entry.insert(0, cliente[2])
        self.email_entry.insert(0, cliente[3])
        self.telefono_entry.insert(0, cliente[4])
        self.direccion_entry.insert(0, cliente[5])

    def delete_cliente(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor seleccione un cliente")
            return

        cliente_cedula = self.tree.item(selected_item)['values'][0]

        conn = sqlite3.connect('ventas.db')
        c = conn.cursor()
        c.execute("DELETE FROM clientes WHERE cedula=?", (cliente_cedula,))
        conn.commit()
        conn.close()

        self.load_clientes()

    def update_cliente(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor seleccione un cliente")
            return

        cliente_cedula = self.tree.item(selected_item)['values'][0]
        cedula = self.cedula_entry.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()
        direccion = self.direccion_entry.get()

        if not (cedula and nombre and apellido and email and telefono and direccion):
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")
            return

        if not self.validate_cedula(cedula):
            messagebox.showwarning("Advertencia", f"La cédula '{cedula}' no es válida. Asegúrese de que tenga 10 dígitos.")
            return

        if not self.validate_email(email):
            messagebox.showwarning("Advertencia", "El email no tiene un formato válido")
            return

        if not self.validate_phone(telefono):
            messagebox.showwarning("Advertencia", "El teléfono debe contener solo dígitos y tener al menos 10 caracteres")
            return

        conn = sqlite3.connect('ventas.db')
        c = conn.cursor()
        c.execute("""
            UPDATE clientes 
            SET cedula=?, nombre=?, apellido=?, email=?, telefono=?, direccion=?
            WHERE cedula=?
        """, (cedula, nombre, apellido, email, telefono, direccion, cliente_cedula))
        conn.commit()
        conn.close()

        self.load_clientes()
        self.clear_form()
        
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ProductosWindow:
    def __init__(self, root):
        self.root = root
        self.top = tk.Toplevel(root)
        self.top.title("Productos")
        self.top.geometry("1300x600")
        self.top.configure(bg='lightblue')

        self.frame = tk.Frame(self.top, padx=5, pady=5, bg='lightblue')
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.form_frame = tk.Frame(self.top)
        self.form_frame.pack(padx=20, pady=20)

        self.tree_frame = tk.Frame(self.frame)
        self.tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar_y = ttk.Scrollbar(self.tree_frame, orient=tk.VERTICAL)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_x = ttk.Scrollbar(self.tree_frame, orient=tk.HORIZONTAL)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree = ttk.Treeview(self.tree_frame, columns=("codigo", "Nombre", "Precio", "Stock", "Talla", "Color", "Modelo", "Tipo de tela"), 
                                 show='headings', yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.tree.heading("codigo", text="Código")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Talla", text="Talla")
        self.tree.heading("Color", text="Color")
        self.tree.heading("Modelo", text="Modelo")
        self.tree.heading("Tipo de tela", text="Tipo de tela")

        # Ajustar el ancho de las columnas
        self.tree.column("codigo", width=80)
        self.tree.column("Nombre", width=150)
        self.tree.column("Precio", width=100)
        self.tree.column("Stock", width=100)
        self.tree.column("Talla", width=100)
        self.tree.column("Color", width=100)
        self.tree.column("Modelo", width=150)
        self.tree.column("Tipo de tela", width=150)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar_y.config(command=self.tree.yview)
        self.scrollbar_x.config(command=self.tree.xview)

        self.form_frame = tk.Frame(self.frame, padx=5, pady=5, bg='lightblue')
        self.form_frame.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Label(self.form_frame, text="Código:", bg='lightblue').grid(row=0, column=0, padx=5, pady=5)
        self.codigo_entry = tk.Entry(self.form_frame)
        self.codigo_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Nombre:", bg='lightblue').grid(row=1, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self.form_frame)
        self.nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Precio:", bg='lightblue').grid(row=2, column=0, padx=5, pady=5)
        self.precio_entry = tk.Entry(self.form_frame)
        self.precio_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Stock:", bg='lightblue').grid(row=3, column=0, padx=5, pady=5)
        self.stock_entry = tk.Entry(self.form_frame)
        self.stock_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Talla:", bg='lightblue').grid(row=4, column=0, padx=5, pady=5)
        self.talla_entry = tk.Entry(self.form_frame, validate='key', validatecommand=(self.top.register(self.validate_talla), '%P'))
        self.talla_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Color:", bg='lightblue').grid(row=5, column=0, padx=5, pady=5)
        self.color_entry = tk.Entry(self.form_frame)
        self.color_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Modelo:", bg='lightblue').grid(row=6, column=0, padx=5, pady=5)
        self.modelo_entry = tk.Entry(self.form_frame)
        self.modelo_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Tipo de tela:", bg='lightblue').grid(row=7, column=0, padx=5, pady=5)
        self.tipo_tela_entry = tk.Entry(self.form_frame)
        self.tipo_tela_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Button(self.form_frame, text="Agregar Producto", command=self.add_producto, bg='lightgreen', fg='black').grid(row=8, column=0, columnspan=2, pady=5)
        tk.Button(self.form_frame, text="Editar Producto", command=self.edit_producto, bg='yellow', fg='black').grid(row=9, column=0, columnspan=2, pady=5)
        tk.Button(self.form_frame, text="Eliminar Producto", command=self.delete_producto, bg='red', fg='black').grid(row=10, column=0, columnspan=2, pady=5)
        tk.Button(self.form_frame, text="Actualizar Producto", command=self.update_producto, bg='blue', fg='white').grid(row=11, column=0, columnspan=2, pady=5)
        tk.Button(self.form_frame, text="Regresar", command=self.close_window, bg='black', fg='white').grid(row=12, column=0, columnspan=2, pady=10)

        self.load_productos()

    def validate_talla(self, value):
        if value == "" or value.isdigit():
            return True
        else:
            messagebox.showwarning("Advertencia", "La talla debe ser un número")
            return False

    def load_productos(self):
        conn = sqlite3.connect('ventas.db')
        c = conn.cursor()
        c.execute("SELECT * FROM productos")
        productos = c.fetchall()
        conn.close()

        self.tree.delete(*self.tree.get_children())

        for producto in productos:
            self.tree.insert('', tk.END, values=producto)

    def add_producto(self):
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        precio = self.precio_entry.get()
        stock = self.stock_entry.get()
        talla = self.talla_entry.get()
        color = self.color_entry.get()
        modelo = self.modelo_entry.get()
        tipo_tela = self.tipo_tela_entry.get()

        if not (codigo and nombre and precio and stock and talla and color and modelo and tipo_tela):
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")
            return
        
        try:
            precio = float(precio)
            stock = int(stock)
            talla = int(talla)
        except ValueError:
            messagebox.showwarning("Advertencia", "Precio, Stock y Talla deben ser números válidos")
            return

        conn = sqlite3.connect('ventas.db')
        c = conn.cursor()
        try:
            c.execute("INSERT INTO productos (codigo, nombre, precio, stock, talla, color, modelo, tipo_tela) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                      (codigo, nombre, precio, stock, talla, color, modelo, tipo_tela))
            conn.commit()
        except sqlite3.IntegrityError:
            messagebox.showwarning("Advertencia", "Ya existe un producto con ese código")
        finally:
            conn.close()

        self.load_productos()
        self.clear_form()

    def clear_form(self):
        self.codigo_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.stock_entry.delete(0, tk.END)
        self.talla_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.modelo_entry.delete(0, tk.END)
        self.tipo_tela_entry.delete(0, tk.END)

    def edit_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor seleccione un producto")
            return

        producto = self.tree.item(selected_item)['values']
        self.codigo_entry.insert(0, producto[0])
        self.nombre_entry.insert(0, producto[1])
        self.precio_entry.insert(0, producto[2])
        self.stock_entry.insert(0, producto[3])
        self.talla_entry.insert(0, producto[4])
        self.color_entry.insert(0, producto[5])
        self.modelo_entry.insert(0, producto[6])
        self.tipo_tela_entry.insert(0, producto[7])

    def delete_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor seleccione un producto")
            return

        producto_codigo = self.tree.item(selected_item)['values'][0]

        conn = sqlite3.connect('ventas.db')
        c = conn.cursor()
        c.execute("DELETE FROM productos WHERE codigo=?", (producto_codigo,))
        conn.commit()
        conn.close()

        self.load_productos()

    def update_producto(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        producto_codigo = self.tree.item(selected_item)['values'][0]
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        precio = self.precio_entry.get()
        stock = self.stock_entry.get()
        talla = self.talla_entry.get()
        color = self.color_entry.get()
        modelo = self.modelo_entry.get()
        tipo_tela = self.tipo_tela_entry.get()

        if not (codigo and nombre and precio and stock and talla and color and modelo and tipo_tela):
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")
            return

        try:
            precio = float(precio)
            stock = int(stock)
            talla = int(talla)
        except ValueError:
            messagebox.showwarning("Advertencia", "Precio, Stock y Talla deben ser números válidos")
            return

        conn = sqlite3.connect('ventas.db')
        c = conn.cursor()
        c.execute("UPDATE productos SET codigo=?, nombre=?, precio=?, stock=?, talla=?, color=?, modelo=?, tipo_tela=? WHERE codigo=?", 
                  (codigo, nombre, precio, stock, talla, color, modelo, tipo_tela, producto_codigo))
        conn.commit()
        conn.close()

        self.load_productos()
        self.clear_form()
        
    def close_window(self):
            self.top.destroy()  # Cierra la ventana actual
            self.root.deiconify()  # Muestra la ventana principal


import tkinter as tk
from tkinter import messagebox
import sqlite3

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog


import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

class VentasWindow:
    def __init__(self, root):
        self.top = tk.Toplevel(root)
        self.top.title("Gestión de Ventas")
        self.top.geometry("800x600")

        self.frame = tk.Frame(self.top, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Listbox para mostrar ventas
        self.ventas_listbox = tk.Listbox(self.frame, height=25, width=100)
        self.ventas_listbox.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar para el Listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.ventas_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.ventas_listbox.yview)

        # Botones para gestionar ventas
        self.add_button = tk.Button(self.top, text="Agregar Venta", command=self.add_venta)
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.top, text="Editar Venta", command=self.edit_venta)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self.top, text="Eliminar Venta", command=self.delete_venta)
        self.delete_button.pack(pady=5)

        # Cargar ventas
        self.load_ventas()

    def load_ventas(self):
        """Carga las ventas en el Listbox."""
        self.ventas_listbox.delete(0, tk.END)
        conn = sqlite3.connect('ventas.db')
        c = conn.cursor()
        c.execute('''
            SELECT v.id, c.nombre, c.apellido, v.fecha, v.total
            FROM venta v
            JOIN clientes c ON v.cedula_cliente = c.cedula
        ''')
        ventas = c.fetchall()
        conn.close()
        for venta in ventas:
            self.ventas_listbox.insert(tk.END, f"ID: {venta[0]} - Cliente: {venta[1]} {venta[2]} - Fecha: {venta[3]} - Total: {venta[4]:.2f}")

    def add_venta(self):
        """Abre un diálogo para agregar una nueva venta."""
        cliente_id = simpledialog.askinteger("Agregar Venta", "ID del cliente:")
        fecha = simpledialog.askstring("Agregar Venta", "Fecha (YYYY-MM-DD):")
        total = simpledialog.askfloat("Agregar Venta", "Total de la venta:")
        if cliente_id and fecha and total is not None:
            self._execute_db_command('''
                INSERT INTO venta (cedula_cliente, fecha, total) 
                VALUES (?, ?, ?)
            ''', (cliente_id, fecha, total))
            self.load_ventas()

    def edit_venta(self):
        """Abre un diálogo para editar la venta seleccionada."""
        selected = self.ventas_listbox.curselection()
        if not selected:
            messagebox.showwarning("Editar Venta", "Por favor, seleccione una venta.")
            return
        
        index = selected[0]
        venta_id = int(self.ventas_listbox.get(index).split(' - ')[0].split(': ')[1])

        cliente_id = simpledialog.askinteger("Editar Venta", "Nuevo ID del cliente:")
        fecha = simpledialog.askstring("Editar Venta", "Nueva fecha (YYYY-MM-DD):")
        total = simpledialog.askfloat("Editar Venta", "Nuevo total de la venta:")
        
        if cliente_id and fecha and total is not None:
            self._execute_db_command('''
                UPDATE venta
                SET cedula_cliente = ?, fecha = ?, total = ?
                WHERE id = ?
            ''', (cliente_id, fecha, total, venta_id))
            self.load_ventas()

    def delete_venta(self):
        """Elimina la venta seleccionada."""
        selected = self.ventas_listbox.curselection()
        if not selected:
            messagebox.showwarning("Eliminar Venta", "Por favor, seleccione una venta.")
            return
        
        index = selected[0]
        venta_id = int(self.ventas_listbox.get(index).split(' - ')[0].split(': ')[1])

        confirm = messagebox.askyesno("Eliminar Venta", "¿Está seguro de que desea eliminar esta venta?")
        if confirm:
            self._execute_db_command('DELETE FROM venta WHERE id = ?', (venta_id,))
            self.load_ventas()

    def _execute_db_command(self, query, params):
        """Ejecuta un comando SQL en la base de datos."""
        try:
            conn = sqlite3.connect('ventas.db')
            c = conn.cursor()
            c.execute(query, params)
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al acceder a la base de datos: {e}")


from fpdf import FPDF
import os
from datetime import datetime

import tkinter as tk
from tkinter import messagebox
import sqlite3
from fpdf import FPDF
import os
from datetime import datetime

class FacturasWindow:
    def __init__(self, root):
        self.top = tk.Toplevel(root)
        self.root = root
        self.top.title("Facturas")
        self.top.geometry("1300x1300")
        self.top.configure(bg='lightblue')

        self.frame = tk.Frame(self.top, padx=3, pady=3, bg='lightblue')
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.form_frame = tk.Frame(self.top)
        self.form_frame.pack(padx=20, pady=20)
        self.form_frame.configure(bg='lightblue')
        
        
        self.preview_text = tk.Text(self.frame, height=20, width=60, wrap=tk.WORD, bg='white')
        self.preview_text.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        self.form_frame = tk.Frame(self.frame, padx=5, pady=5, bg='lightblue')
        self.form_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        tk.Label(self.form_frame, text="Cédula del Cliente:", bg='lightblue').grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.cedula_entry = tk.Entry(self.form_frame)
        self.cedula_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.cedula_entry.bind("<FocusOut>", self.load_client_data)

        self.products_frame = tk.Frame(self.form_frame, bg='lightblue')
        self.products_frame.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.W)

        self.add_product_button = tk.Button(self.form_frame, text="Agregar Código", command=self.add_product_field, bg='lightgreen', fg='black')
        self.add_product_button.grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.W)

        self.button_frame = tk.Frame(self.form_frame, padx=5, pady=5, bg='lightblue')
        self.button_frame.grid(row=3, column=0, columnspan=2, pady=5, sticky=tk.W)

        self.generate_button = tk.Button(self.button_frame, text="Generar Factura", command=self.generate_invoice, bg='lightgreen', fg='black')
        self.generate_button.grid(row=0, column=0, padx=5)

        self.save_pdf_button = tk.Button(self.button_frame, text="Guardar PDF", command=self.save_pdf, bg='lightblue', fg='black')
        self.save_pdf_button.grid(row=0, column=1, padx=5)
        tk.Button(self.form_frame, text="Regresar", command=self.close_window, bg='black', fg='white').grid(row=10, column=0, columnspan=2, pady=20)

        self.product_entries = []
        self.add_product_field()

        self.cliente_data = {
            'cedula': '',
            'nombre': '',
            'apellido': '',
            'email': '',
            'direccion': '',
            'telefono': ''
        }

    def load_client_data(self, event):
        cedula = self.cedula_entry.get().strip()
        if not cedula:
            return

        try:
            conn = sqlite3.connect('ventas.db')
            c = conn.cursor()
            c.execute("SELECT nombre, apellido, email, direccion, telefono FROM clientes WHERE cedula = ?", (cedula,))
            client_data = c.fetchone()
            conn.close()

            if client_data:
                nombre, apellido, email, direccion, telefono = client_data
                self.cliente_data = {
                    'cedula': cedula,
                    'nombre': nombre,
                    'apellido': apellido,
                    'email': email,
                    'direccion': direccion,
                    'telefono': telefono
                }
            else:
                messagebox.showwarning("Advertencia", "Cliente no encontrado")
                self.cliente_data = {
                    'cedula': cedula,
                    'nombre': '',
                    'apellido': '',
                    'email': '',
                    'direccion': '',
                    'telefono': ''
                }
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al acceder a la base de datos: {e}")

    def add_product_field(self):
        row = len(self.product_entries) + 1
        tk.Label(self.products_frame, text=f"Código {row}:", bg='lightblue').grid(row=row, column=0, padx=5, pady=5, sticky=tk.W)
        codigo_entry = tk.Entry(self.products_frame)
        codigo_entry.grid(row=row, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(self.products_frame, text="Cantidad:", bg='lightblue').grid(row=row, column=2, padx=5, pady=5, sticky=tk.W)
        cantidad_entry = tk.Entry(self.products_frame)
        cantidad_entry.grid(row=row, column=3, padx=5, pady=5, sticky=tk.W)

        self.product_entries.append((codigo_entry, cantidad_entry))

    def generate_invoice(self):
        if not self.cliente_data['cedula']:
            messagebox.showwarning("Advertencia", "Por favor complete el campo de cédula del cliente")
            return

        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        preview_text = (
            f"Factura\n\n"
            f"D'GLORY SPORT S.A\n"
            f"RUC: 1719783522001 \n"
            f"Dirección: la Mana Av. 19 de Mayo \n\n"
            f"Fecha y Hora: {fecha_hora_actual}\n\n"
            f"Cliente:\n"
            f"Cédula: {self.cliente_data['cedula']}\n"
            f"Nombre: {self.cliente_data['nombre']}\n"
            f"Apellido: {self.cliente_data['apellido']}\n"
            f"Email: {self.cliente_data['email']}\n"
            f"Dirección: {self.cliente_data['direccion']}\n"
            f"Teléfono: {self.cliente_data['telefono']}\n\n"
        )

        total_factura = 0
        for codigo_entry, cantidad_entry in self.product_entries:
            codigo = codigo_entry.get()
            cantidad = cantidad_entry.get()

            if codigo and cantidad:
                conn = sqlite3.connect('ventas.db')
                c = conn.cursor()
                c.execute("SELECT color, modelo, precio FROM productos WHERE codigo = ?", (codigo,))
                producto_data = c.fetchone()
                conn.close()

                if producto_data is None:
                    color = 'No disponible'
                    modelo = 'No disponible'
                    precio = 0
                    total = 0
                else:
                    color = producto_data[0]
                    modelo = producto_data[1]
                    precio = producto_data[2]
                    total = float(precio) * int(cantidad)
                    total_factura += total

                preview_text += (
                    f"Código: {codigo}\n"
                    f"Cantidad: {cantidad}\n"
                    f"Color: {color}\n"
                    f"Modelo: {modelo}\n"
                    f"Precio Unitario: {precio}\n"
                    f"Total: {total}\n\n"
                )

        preview_text += f"Total Factura: {total_factura}\n"

        self.preview_text.delete(1.0, tk.END)
        self.preview_text.insert(tk.END, preview_text)

    def save_pdf(self):
        preview_text = self.preview_text.get(1.0, tk.END).strip()
        if not preview_text:
            messagebox.showwarning("Advertencia", "No hay vista previa para guardar.")
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, 'Factura', 0, 1, 'C')
        pdf.ln(10)

        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "D'GLORY SPORT S.A", 0, 1, 'C')
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "RUC: 1719783522001", 0, 1, 'C')
        pdf.cell(0, 10, "Dirección: la Mana Av.19 de Mayo ", 0, 1, 'C')
        pdf.ln(10)

        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"Fecha y Hora: {fecha_hora_actual}", 0, 1, 'L')
        pdf.ln(5)

        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, 'Cliente:', 0, 1, 'L')
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Cédula: {self.cliente_data['cedula']}", 0, 1, 'L')
        pdf.cell(0, 10, f"Nombre: {self.cliente_data['nombre']}", 0, 1, 'L')
        pdf.cell(0, 10, f"Apellido: {self.cliente_data['apellido']}", 0, 1, 'L')
        pdf.cell(0, 10, f"Email: {self.cliente_data['email']}", 0, 1, 'L')
        pdf.cell(0, 10, f"Dirección: {self.cliente_data['direccion']}", 0, 1, 'L')
        pdf.cell(0, 10, f"Teléfono: {self.cliente_data['telefono']}", 0, 1, 'L')
        pdf.ln(10)

        pdf.set_font("Arial", 'B', 12)
        pdf.cell(60, 10, 'Código', 1)
        pdf.cell(30, 10, 'Cantidad', 1)
        pdf.cell(30, 10, 'Color', 1)
        pdf.cell(30, 10, 'Modelo', 1)
        pdf.cell(30, 10, 'Precio Unitario', 1)
        pdf.cell(30, 10, 'Total', 1)
        pdf.ln()

        total_factura = 0
        for codigo_entry, cantidad_entry in self.product_entries:
            codigo = codigo_entry.get()
            cantidad = cantidad_entry.get()

            if codigo and cantidad:
                conn = sqlite3.connect('ventas.db')
                c = conn.cursor()
                c.execute("SELECT color, modelo, precio FROM productos WHERE codigo = ?", (codigo,))
                producto_data = c.fetchone()
                conn.close()

                if producto_data is None:
                    color = 'No disponible'
                    modelo = 'No disponible'
                    precio = 0
                    total = 0
                else:
                    color = producto_data[0]
                    modelo = producto_data[1]
                    precio = producto_data[2]
                    total = float(precio) * int(cantidad)
                    total_factura += total

                pdf.cell(60, 10, codigo, 1)
                pdf.cell(30, 10, cantidad, 1)
                pdf.cell(30, 10, color, 1)
                pdf.cell(30, 10, modelo, 1)
                pdf.cell(30, 10, f'{precio:.2f}', 1)
                pdf.cell(30, 10, f'{total:.2f}', 1)
                pdf.ln()

        pdf.set_font("Arial", 'B', 12)
        pdf.cell(150, 10, 'Total Factura:', 1)
        pdf.cell(30, 10, f'{total_factura:.2f}', 1)
        pdf.ln()

        pdf_file = "factura_guardada.pdf"
        pdf.output(pdf_file)

        os.startfile(pdf_file)

    def clear_form(self):
        self.cedula_entry.delete(0, tk.END)
        for codigo_entry, cantidad_entry in self.product_entries:
            codigo_entry.delete(0, tk.END)
            cantidad_entry.delete(0, tk.END)
    
    def close_window(self):
        self.top.destroy()  # Cierra la ventana actual
        self.root.deiconify()  # Muestra la ventana principal
      
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
