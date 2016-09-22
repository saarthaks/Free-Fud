# -*- coding: utf-8 -*-
from flask import Flask, request, redirect
import twilio.twiml
import webScraper

''''
account_sid = "ACfab2961691fdc37117b2d28829663340"
auth_token = "a5ab211f1a9b18faa3267454947fc761"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+18455212270", from_="+18455354154", 
                                 body="did it work2")
'''

def make_body():
    responses = webScraper.make_text(webScraper.main())
    output = ''
    for response in responses:
        output = output + '\n'
    
    return output

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    
    resp = twilio.twiml.Response()
    body = "Hello\nHello"
    print body
    resp.message("{0}".format(body))
    return str(resp)
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
