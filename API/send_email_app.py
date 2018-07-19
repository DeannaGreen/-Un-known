from flask import Flask , render_template,request
import requests

app = Flask("MyApp")

@app.route("/")
def home():
	return render_template ("home.html") 

@app.route("/send", methods=["POST"])
def read_form_data():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	name =  form_data["name"] # from the form object getting value of dob field.
	emailto =  form_data["email"]
	
	emailtext = "Hello " + name

	send_simple_message(emailto, emailtext)

	return "Email Sent"


def send_simple_message(emailto, emailtext):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox7be174d6fe3b464fbad278bc97bd7c28.mailgun.org/messages",
        auth=("api", "220b0a312b06175524292b3157a79404-8889127d-dbaabf56"),
        data={"from": "deanna@16vmini.co.uk",
              "to": [emailto],
              "subject": "Hello",
              "text": emailtext})


app.run(debug=True)