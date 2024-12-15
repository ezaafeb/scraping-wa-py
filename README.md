# scraping-wa-py
Hi! Welcome to my GitHub @ezaafeb, in this article I will share a tutorial on how to scrape number data from WhatsApp groups, a technique usually used for digital marketing to promote goods/services.
# 🔗 WhatsApp Group Invite Automation with Python

This repository provides a step-by-step guide to automate the process of sending WhatsApp group invites using Python and the `pywhatkit` library. Follow the instructions below to set up the project and execute the script.

---

## 🔧 Features
- ✅ Automate sending messages to WhatsApp numbers.
- ✅ Easily send group invite links to multiple contacts.
- ✅ Customize message templates.

---

## 📄 Prerequisites
1. Install [Python](https://www.python.org/downloads/) (version 3.7 or later).
2. Install [Visual Studio Code (VSCode)](https://code.visualstudio.com/).
3. Extension [WhatsApp Scraping contact for web](https://chromewebstore.google.com/detail/whatsapp-manajemen-grup-p/ldodkdnfdpchaipnoklfnfmbbkdoocej)
4. Clone this repository.
   

---

## 🔗 Installation Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/ezaafeb/scraping-wa-py.git
cd scraping-wa-py
```

### Step 2: Set Up a Virtual Environment (Optional but Recommended)
```bash
python3 -m venv nama_env | example: python3 -m venv ezaafebri      # Replace env_name with the name you want to give your virtual environment.
source nama_env/bin/activate | example source ezaafebri/bin/activate # On macOS or Linux
source venv/bin/activate      # On Windows: venv\Scripts\activate
If successful, you will see the name of the virtual environment appear at the front of the terminal prompt, like this:
(nama_env) user@machine:~$ #This indicates that you are now in the virtual environment.

```

### Step 3: Install Required Dependencies
```bash
pip install pywhatkit
#If you want to exit the virtual environment, just type:
deactivate
#That will return you to your system's Python environment.
```

### Step 4: Prepare the Script
1. Open the `kirim_pesan.py` file in VSCode.
2. Edit the following variables in the script:
    - **`group_link`**: Add the invite link to your WhatsApp group.
    - **`contacts`**: List of phone numbers in international format (e.g., `['+628123456789', '+628987654321']`).

### Step 5: Execute the Script
Run the script in the terminal:
```bash
python3 /Users/apple/Documents/kirim_pesan.py #On MacOS
python "C:\Users\NamaUser\Documents\kirim_pesan.py" #On Windows
#python → If Python 3 is not the default, use python3
#C:\Users\UserName\Documents\send_messages.py → Adjust to the path (location) of your Python file in Windows.

```

---

## 🗋 Code Example
Here’s an example `invite.py` script:
```python
import pywhatkit as kit
import time

# List nomor telepon yang ingin diundang
nomor_telepon = [
'+62123456789', '+62987654321',  

]

# Link undangan grup WhatsApp
link_undangan = "https://chat.whatsapp.com/"

# Pesan yang akan dikirim
pesan = f"Halo! Teman-teman semua terimakasih sudah enthusiast untuk mengikuti Webinar Blackhat To Whitehat, Yuk Join *Community XyberXecurity!* Klik link ini untuk bergabung: {link_undangan} *Pesan ini dikirim otomatis jangan reply atau spam ya!*"

# Mengirim pesan dengan delay di antara setiap pengiriman
for nomor in nomor_telepon:
    try:
```
---


https://github.com/user-attachments/assets/b3bf56ca-102e-41df-9c38-a1c96431f73d


---

## 🚫 Notes
1. Ensure that WhatsApp Web is logged in before running the script.
2. Adjust the delay (`time.sleep`) as needed to prevent errors or spamming.
3. Always comply with WhatsApp’s usage policies.

---

## 💡 Issues and Contributions
Feel free to open issues or submit pull requests if you encounter any problems or have suggestions for improvement.

---

## 📚 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💼 Author
Created by [Reza Febriansyah](https://github.com/ezaafeb).

---

## 📲 Stay Connected
Follow me on:
- [GitHub](https://github.com/ezaafebri)
- [LinkedIn](https://linkedin.com/in/ezaafebri)
- [Instagram](https://instagram.com/ezaafebri)
- [Twitter](https://twitter.com/ezaafebri)

---
