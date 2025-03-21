from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Configurações do Twilio
import os

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"
SEU_NUMERO_WHATSAPP = "whatsapp:+5511948530302"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/enviar_mensagem', methods=['POST'])
def enviar_mensagem():
    data = request.json
    mensagem = data.get("mensagem", "Erro: mensagem não fornecida.")

    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=mensagem,
        to=SEU_NUMERO_WHATSAPP
    )

    return jsonify({"status": "Mensagem enviada!", "message_id": message.sid})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
