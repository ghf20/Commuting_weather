#IF YOU ARE A STUDENT CHECKOUT https://education.github.com/pack#offers FOR TWILIO CREDIT

from twilio.rest import Client

def send_message(message_str):

    
    account_sid = "" #ADD TWILIO SID HERE. 
    auth_token = 'cb3ce3936d9f46d44e2c86549d4f80ca'
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
                                from_='+123456789', #ADD YOUR TWILIO NUMBER
                                body =f'{message_str}',
                                to ='+1987654321' #ADD RECIPIENTS NUMBER
                            )
    
    #print(message.sid) #UNCOMMENT TO SEE RESPONSE FROM SERVER 
    
if __name__ == "__main__":

    send_message()