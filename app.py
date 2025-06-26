from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/postback", methods=["GET"])
def postback():
    params = request.args.to_dict()
    if not params:
        return "No parameters", 400

    campaign = params.get("campaign_name", "-")
    offer = params.get("offer_name", "-")
    revenue = params.get("revenue", "-")
    sub4 = params.get("sub_id_4", "-")
    sub5 = params.get("sub_id_5", "-")
    sub6 = params.get("sub_id_6", "-")

    message = (
        f"🔔 Новая регистрация!\n"
        f"📢 ОФФЕР: {offer}\n"
        f"📋 КАМПАНИЯ: {campaign}\n"
        f"💰 CPA: {revenue} $\n"
        f"🧾 ID КАБА: {sub4}\n"
        f"🏷️ Нейминг: {sub5}\n"
        f"🧩 Адсет: {sub6}"
    )

    if params.get("status") == "deposit":
        message = (
            f"✅ Новый депозит!\n"
            f"📢 ОФФЕР: {offer}\n"
            f"📋 КАМПАНИЯ: {campaign}\n"
            f"💰 CPA: {revenue} $\n"
            f"🧾 ID КАБА: {sub4}\n"
            f"🏷️ Нейминг: {sub5}\n"
            f"🧩 Адсет: {sub6}"
        )

    response = requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": message}
    )

    if response.status_code != 200:
        return "Telegram error", 500

    return "OK", 200

if __name__ == "__main__":
    app.run()
