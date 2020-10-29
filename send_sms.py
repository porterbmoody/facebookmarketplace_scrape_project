

from twilio.rest import Client 
 
# phone_numbers = {
#     "kristin" : "+15038930864",
#     "porter"  : "+17193385009",
#     "nate"    : "+15035803396"
# }

# monday 8
# tue 9
# wed 7:33
# thu 8:11
# fri 10:18
# sunday 9
# phone_numbers = ["+15038930864", "+17193385009", "+15035803396", "+19712005681", "+18016693768", "+13852303728"]
# __to__ = ["+17193385009", "+17192002026"]

print("------------------------")
# my_text = "https://www.facebook.com/marketplace/item/797520111059937"
print("------------------------")
def main(recipient, body):
    send_sms_epic_to(recipient, body)
def send_sms_epic_to(recipient, body):

    account_sid = 'ACb8fa2683a0e0572bde6d0816efac96cc' 
    auth_token = '6190475282b6fb3585db2babca1eb2ea' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create(body = body,
                                    from_ = '+16508307908',        
                                    to = recipient 
                                )

if __name__ == "__main__":
    main(recipient, body)

