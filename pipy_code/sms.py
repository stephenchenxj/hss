from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1c7a1729170405c928b81f02ee690596"
# Your Auth Token from twilio.com/console
auth_token  = "c82373a24c739eb2dc9c36f7182a99b6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14086149233", 
    from_="+15623144564",
    body="Hello from Python!")

print(message.sid)
