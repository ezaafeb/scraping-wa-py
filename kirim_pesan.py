import pywhatkit as kit
import time

# List nomor telepon yang ingin diundang
nomor_telepon = [
'+6281535220085', '+6281295085279', '+6287874567819', '+6285693046831', '+6281276380783', '+62859106643435', '+6285604710395', '+6289601632917', '+6285864183587', '+6281586752945', '+6287754031633', '+6289515210305', '+6289512867949', '+6289655606289', '+6287770254798'

]

# Link undangan grup WhatsApp
link_undangan = "https://chat.whatsapp.com/LQNJsoC5jR50MHS6E2TBqu"

# Pesan yang akan dikirim
pesan = f"Halo! Teman-teman semua terimakasih sudah enthusiast untuk mengikuti Webinar Blackhat To Whitehat, Yuk Join *Community XyberXecurity!* Klik link ini untuk bergabung: {link_undangan} *Pesan ini dikirim otomatis jangan reply atau spam ya!*"

# Mengirim pesan dengan delay di antara setiap pengiriman
for nomor in nomor_telepon:
    try:
        # Mengirim pesan ke setiap nomor secara instan
        kit.sendwhatmsg_instantly(nomor, pesan, 18, tab_close=False)  # Memberikan waktu 15 detik
        
        # Menunggu 20 detik untuk memastikan pesan terkirim
        time.sleep(15)  # Tunggu 20 detik setelah pengiriman
        
        # Menunggu beberapa detik sebelum melanjutkan ke pengiriman berikutnya
        print(f"Pesan berhasil dikirim ke {nomor}, menunggu untuk pengiriman berikutnya...")
        time.sleep(17)  # Tunggu 10 detik sebelum mengirim ke nomor berikutnya
    except Exception as e:
        print(f"Gagal mengirim pesan ke {nomor}: {e}")
