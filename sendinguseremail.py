from flask import Flask , render_template,request
import requests

app = Flask("MyApp")

@app.route("/")
def home():
	return render_template ("signup.html") 

@app.route("/send", methods=["POST"])
def read_form_data():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	name =  form_data["username"] # from the form object get the Username
	emailto =  form_data["email"] # from the form object get the email
	
	emailtext = "Hello " + name + "Welcome to the (Un)Known"

	send_simple_message(emailto, emailtext)

	return render_template ("emailsent.html")


def send_simple_message(emailto, emailtext):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox7be174d6fe3b464fbad278bc97bd7c28.mailgun.org/messages",
        auth=("api", "220b0a312b06175524292b3157a79404-8889127d-dbaabf56"),
        data={"from": "deanna@16vmini.co.uk",
              "to": [emailto],
              "subject": "Hello",
              "text": emailtext})


app.run(debug=True)