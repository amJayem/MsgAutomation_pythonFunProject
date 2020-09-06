from twilio.rest import Client

account_sid = 'AC01159837f14638fabafa90a4e597bba6'
auth_token = '5d3722a928f48de13ed5bf55690d2b45'
client = Client(account_sid, auth_token)

def send_msg():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='hey!!good to see this *_*',
        to='whatsapp:+8801521312525'
    )

    print(message.sid)