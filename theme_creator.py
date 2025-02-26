import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageDraw, ImageFont
import pysftp

# Nom du développeur
DEV_NAME = "trhacknon"
https://ree.com/es.php
class WordPressThemeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur de Thèmes WordPress - trhacknon")
        self.root.geometry("600x500")
        self.root.configure(bg="#222222")

        # Variables des champs
        self.theme_name = tk.StringVar()
        self.theme_description = tk.StringVar()
        self.theme_version = tk.StringVar(value="1.0")
        self.theme_author = tk.StringVar(value=DEV_NAME)
        self.theme_color = "#3498db"  # Bleu par défaut
        self.theme_directory = tk.StringVar()
        self.ftp_upload = tk.BooleanVar()

        # Interface
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Nom du Thème :", fg="white", bg="#222222").pack(pady=5)
        tk.Entry(self.root, textvariable=self.theme_name, width=40).pack()

        tk.Label(self.root, text="Description :", fg="white", bg="#222222").pack(pady=5)
        tk.Entry(self.root, textvariable=self.theme_description, width=40).pack()

        tk.Label(self.root, text="Version :", fg="white", bg="#222222").pack(pady=5)
        tk.Entry(self.root, textvariable=self.theme_version, width=10).pack()

        tk.Label(self.root, text="Auteur :", fg="white", bg="#222222").pack(pady=5)
        tk.Entry(self.root, textvariable=self.theme_author, width=30).pack()

        tk.Label(self.root, text="Couleur principale :", fg="white", bg="#222222").pack(pady=5)
        tk.Button(self.root, text="Choisir une couleur", command=self.choose_color).pack()

        tk.Label(self.root, text="Dossier de sortie :", fg="white", bg="#222222").pack(pady=5)
        tk.Entry(self.root, textvariable=self.theme_directory, width=40).pack()
        tk.Button(self.root, text="Sélectionner", command=self.select_directory).pack()

        tk.Checkbutton(self.root, text="Uploader sur FTP après génération", variable=self.ftp_upload, fg="white", bg="#222222").pack(pady=10)

        tk.Button(self.root, text="Générer le Thème", command=self.generate_theme, bg="#27ae60", fg="white").pack(pady=10)

    def choose_color(self):
        color = colorchooser.askcolor(title="Choisir une couleur")[1]
        if color:
            self.theme_color = color

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.theme_directory.set(directory)

    def generate_theme(self):
        if not self.theme_name.get() or not self.theme_directory.get():
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
            return

        theme_path = os.path.join(self.theme_directory.get(), self.theme_name.get())
        os.makedirs(theme_path, exist_ok=True)

        # Création des fichiers
        self.create_style_css(theme_path)
        self.create_php_files(theme_path)
        self.create_screenshot(theme_path)

        # Compression en zip
        zip_path = theme_path + ".zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(theme_path):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), theme_path))

        messagebox.showinfo("Succès", f"Thème généré avec succès :\n{zip_path}")

        if self.ftp_upload.get():
            self.upload_to_ftp(zip_path)

    def create_style_css(self, theme_path):
        css_content = f"""/*
Theme Name: {self.theme_name.get()}
Theme URI: https://github.com/{DEV_NAME}
Description: {self.theme_description.get()}
Version: {self.theme_version.get()}
Author: {self.theme_author.get()}
Author URI: https://github.com/{DEV_NAME}
License: GPL-2.0+
*/
body {{
    background-color: {self.theme_color};
    font-family: Arial, sans-serif;
}}
"""
        with open(os.path.join(theme_path, "style.css"), "w") as f:
            f.write(css_content)

    def create_php_files(self, theme_path):
        php_files = {
            "index.php": "<?php get_header(); ?>\n<h1>Bienvenue sur mon thème WordPress</h1>\n<?php get_footer(); ?>",
            "header.php": "<!DOCTYPE html>\n<html>\n<head>\n<title>Mon Thème</title>\n<link rel='stylesheet' href='<?php echo get_stylesheet_uri(); ?>'>\n</head>\n<body>",
            "footer.php": "</body>\n</html>",
            "functions.php": "<?php\nfunction my_theme_setup() {\nadd_theme_support('title-tag');\n}\nadd_action('after_setup_theme', 'my_theme_setup');"
        }
        for filename, content in php_files.items():
            with open(os.path.join(theme_path, filename), "w") as f:
                f.write(content)

    def create_screenshot(self, theme_path):
        img = Image.new("RGB", (880, 660), self.theme_color)
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((50, 50), self.theme_name.get(), fill="white", font=font)
        img.save(os.path.join(theme_path, "screenshot.png"))

    def upload_to_ftp(self, zip_path):
        ftp_host = "ftp.exemple.com"
        ftp_user = "utilisateur"
        ftp_pass = "motdepasse"

        with pysftp.Connection(ftp_host, username=ftp_user, password=ftp_pass) as sftp:
            sftp.put(zip_path, f"/wp-content/themes/{os.path.basename(zip_path)}")

        messagebox.showinfo("FTP", "Thème uploadé avec succès !")


root = tk.Tk()
app = WordPressThemeGenerator(root)
root.mainloop()
