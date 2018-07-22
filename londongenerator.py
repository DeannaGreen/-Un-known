from flask import Flask , render_template,request

#This is create instance of Flask. app is variable
app = Flask("MyApp")


#Default route his method will be called when you hit http://127.0.0.0:5000/
@app.route("/")
def home():
	return render_template ("loginhomepage.html") # render_template method is a special function flask which redirect to the html file mentioned in the paramter

#creating dictionaries for each location
SouthBank = { 1 : "Southwark Bridge at Night", 2 : "Shakespeare's Globe Theatre", 3 : "Guided Tour the GLobe theatre"}
LeicesterSquare = { 1 : "Forbidden Planet London", 2 : "Golden Square", 3 : "House of MinaLima", 4 : "Covent Garden Live music", 5 : "Second Hand Book Shop"}
HydePark = { 1 : "Aplsey House", 2 : "Duke of Wellington", 3 : "Serpintine Gallery", 4 : "Summer of sound on the roof"}
TowerBridge = { 1 : "Hays Galeria", 2 : "Science gallery", 3 : "London glassblowing"}
CanaryWharf = { 1 : "The Grapes", 2 : "Giant Robot", 3 : "Rooftop Garden"}
Rooftop = { 1 : "London Fields", 2 : "South Bank rooftop", 3 : "Coq d'argent", 4 : "Sushi Samba"}

def random_location_generator():
	import random
	if(location_selector == "SouthBank"):
		random_number = random.randint(1,int(len(SouthBank)))
	elif(location_selector == "LeicesterSquare"):
		random_number = random.randint(1,int(len(LeicesterSquare)))
	elif(location_selector == "HydePark"):
		random_number = random.randint(1,int(len(HydePark)))
	elif(location_selector == "TowerBridge"):
		random_number = random.randint(1,int(len(TowerBridge)))
	elif(location_selector == "CanaryWharf"):
		random_number = random.randint(1,int(len(CanaryWharf)))
	elif(location_selector == "Rooftop"):
		random_number = random.randint(1,int(len(Rooftop)))
	else:
		random_number = 0
	return random_number

@app.route("/locgame", methods=["POST"])
def read_form_data():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	location_selector =  form_data["londonlocation"] # from the form object getting the location input
	location_number= random_location_generator(location_selector) #Takes location and returns random number
	location_chosen = location_selector[location_number] #chooses from the location array user selected and random number that place
	return render_template ("showmylocationchosen.html",location_chosen=location_chosen)



	