# 📱 Phone-Intel Pro

> **Outil d'analyse OSINT pour numéros de téléphone**  
> Un utilitaire de reconnaissance permettant d'extraire les métadonnées techniques, géographiques et réseau à partir d'un numéro de téléphone international.  
> Python 3 · Phonenumbers Lib · OSINT Data

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-557C94?logo=kalilinux&logoColor=white)
![Category](https://img.shields.io/badge/Category-OSINT-orange)

---

## 📋 Présentation

**Phone-Intel Pro** est un outil de collecte d'informations en source ouverte (OSINT).  
Il utilise la bibliothèque de métadonnées de Google pour analyser les numéros de téléphone et fournir des informations utiles lors d'une phase de reconnaissance ou d'investigation numérique.

---

## 🚀 Fonctionnalités

- **Validation de format** : Vérifie si un numéro est valide selon les standards internationaux (**E.164**)  
- **Géolocalisation OSINT** : Identifie le pays et la région/ville d'origine du numéro  
- **Identification de l'opérateur** : Détecte le fournisseur de services réseau  
- **Analyse temporelle** : Extrait les fuseaux horaires associés  
- **Formatage automatique** : Conversion en formats national et international  

---

## ⚙️ Installation & Prérequis

### 🔧 Prérequis

Le script repose sur la bibliothèque `phonenumbers` :

```bash
pip install phonenumbers
```

### 📦 Installation du projet

```bash
git clone https://github.com/Maxime288/Phone-Intel-Pro.git
cd Phone-Intel-Pro
chmod +x phone_intel.py
```

---

## 🚀 Utilisation

> ⚠️ Le numéro doit être fourni au **format international** (avec le préfixe `+`)

### 📌 Syntaxe

```bash
python3 phone_intel.py -n "+33612345678"
```

---

## 🖥️ Exemple de sortie

```text
[*] Analyse terminée pour : +336XXXXXXXX

🔍 INFORMATIONS GÉNÉRALES
  Format International : +33 6 XX XX XX XX
  Format National      : 06 XX XX XX XX
  Code Pays            : +33

🌍 GÉOGRAPHIE
  Localisation         : France

📡 RÉSEAU & TEMPS
  Opérateur d'origine  : Orange
  Fuseaux horaires     : Europe/Paris
```

---

## 🔬 Détails Techniques

- **Langage** : Python 3  
- **Bibliothèque principale** : `phonenumbers`  
  (portage Python de libphonenumber de Google)  
- **Méthodologie** :  
  Analyse statique de métadonnées + exploitation des registres de numérotation internationaux  

---

## ⚠️ Avertissement légal

Cet outil est destiné exclusivement à un usage :

- **éducatif**
- **OSINT légitime**
- **investigation autorisée**

⚠️ La collecte d'informations sur des individus doit respecter les lois en vigueur, notamment le **RGPD** (protection des données personnelles).

L'auteur décline toute responsabilité en cas d'utilisation abusive ou malveillante.
