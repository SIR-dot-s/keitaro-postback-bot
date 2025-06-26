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
    campaign_id = params.get("sub_id_5", "-")
    campaign_name = params.get("sub_id_6", "-")
    ad_name = params.get("sub_id_2", "-")

    message = (
        f"🔔 РЕГИСТРАЦИЯ 🔔\n"
        f"{campaign}\n"
        f"ОФФЕР: {offer}\n"
        f"ID КАБА: {campaign_id}\n"
        f"COMPANY NAME: {campaign_name}\n"
        f"ID KREO: {ad_name}"
    )

    if params.get("status") == "deposit":
        message = (
            f"🚀 ДЕПОЗИТ 🚀\n"
            f"{campaign}\n"
            f"ОФФЕР: {offer}\n"
            f"ID КАБА: {campaign_id}\n"
            f"COMPANY NAME: {campaign_name}\n"
            f"ID KREO: {ad_name}"
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
