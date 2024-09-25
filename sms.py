from twilio.rest import Client

account_sid = "AC166276d490a973cabbfe551cd6f9c314"
auth_token = "6c26e2a98cf91beb45e70e1c8b54c2cf"
cliente = Client(account_sid, auth_token)

mensagem = cliente.messages.create(
    from_="+15134947015",
    to="+5561992211346",
    body="opaa"
)

print(mensagem.body)



