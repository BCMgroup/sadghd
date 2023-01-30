import time
from pyrogram import Client
app = Client(
    "My_Account",
    api_id = 28012514,
    api_hash ="a58b30c1da1e3a2e9b86da20206269c4")
with app:
    while True:
        time.sleep(60)
        time1 = time.localtime()
        soat = time.strftime("%H:%M", time1)
        app.update_profile(first_name=f"Bobursher |{soat}")
