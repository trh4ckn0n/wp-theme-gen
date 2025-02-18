# 🎨 WordPress Theme Creator – trhacknon
 
**Un outil interactif pour générer des thèmes WordPress personnalisés et les uploader via FTP.**
 
## 📌 Fonctionnalités
 
✅ Interface graphique intuitive avec **Tkinter** 

✅ Personnalisation complète : **nom du thème, couleurs, polices, CSS, structure** 

✅ Génération automatique des fichiers WordPress : `style.css`, `index.php`, `functions.php` 

✅ **Upload FTP intégré** pour envoyer le thème directement sur un serveur 

✅ Gestion des **prévisualisations et templates** 

✅ Option pour **sauvegarder et charger des configurations**
  
## 🚀 Installation
 
### 1️⃣ Cloner le projet

 ```bash
 git clone https://github.com/trh4ckn0n/wp-theme-creator.git
 cd wp-theme-creator
 ``` 

### 2️⃣ Installer les dépendances
 ```bash
 pip install -r requirements.txt
 ```  
## 🎯 Utilisation
 
### 1️⃣ Lancer l'interface

 ```bash
 python theme_creator.py 
 ``` 

### 2️⃣ Remplir les informations du thème
 
 
- Nom du thème
 
- Couleurs principales
 
- Fichiers CSS et PHP personnalisés
 
- Structure du thème (header, footer, sidebar...)
 
- Chemin FTP pour l'upload
 

 
### 3️⃣ Générer et envoyer 🚀
 
 
- Le thème est créé dans le dossier `output/`
 
- Possibilité d'uploader directement via FTP
 

  
## 📂 Arborescence du projet

 ```bash
 wp-theme-creator/ 
 │── theme_creator.py # Script principal 
 │── requirements.txt # Dépendances 
 │── README.md        # Documentation 
 │── output/                
 │── templates/             
 └── assets/
 ```

## 🔥 À venir
 
☑️ Support de **SFTP & FTP sécurisé** 

☑️ Sélection de **templates préconçus** 

☑️ Intégration d’un **éditeur live**
  
👨‍💻 Développé par **trhacknon** 
