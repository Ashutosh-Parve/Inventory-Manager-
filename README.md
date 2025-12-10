# 📦 Inventory Manager

A Python-based Inventory Management system that allows you to **track, manage, and backup inventory data**.  
Built with **SQLite**, modular architecture, and optional **AWS S3 backup integration**.

---

## 🚀 Features

- 🗃️ Add, update, and delete inventory items  
- 📊 View all inventory items  
- 💾 Backup inventory database to AWS S3  
- 📝 Logs every action in SQLite  
- 🔐 Secure environment variables using `.env`  
- 🌐 Modular design for easy extension

---

## 🗂️ Project Structure

inventory-manager/
│
├── .env
├── app.py
├── backup.py
├── database.py
└── inventory

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/inventory-manager.git
cd inventory-manager


2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the environment
Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Create .env in project root

AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=ap-south-1
AWS_BUCKET_NAME=your_bucket
DB_PATH=inventory

⚠️ Never upload .env to GitHub.

▶️ How to Run the Project

python app.py

You will see menu options:


1. Add Item
2. Update Item
3. Delete Item
4. View Inventory
5. Backup Inventory
6. Exit


📝 Logging and Backup

All actions are stored in SQLite database (inventory)

Backup files are automatically created with timestamps (backup_YYYYMMDD_HHMMSS)

Optional AWS S3 integration for cloud backup

☁️ AWS Backup Requirements 

AWS Account

S3 Bucket

IAM User with S3 permissions

Keys stored securely in .env

👤 Author
Ashutosh Parve
Made with ❤️ in India 🇮🇳


---

### ✅  **requirements.txt**

For this Inventory Manager project, the minimal requirements are:

boto3
python-dotenv


- `boto3` → for AWS S3 backups  
- `python-dotenv` → to read `.env` variables  
- SQLite is built-in, no need to include  

---













ChatGPT ca# Inventory-Manager-
