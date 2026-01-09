import requests,pycountry,os
from flask import Flask, jsonify,request
from flask_cors import CORS
app = Flask(__name__)
origins = os.environ.get("REQUEST_ORIGIN", "").split(",")
CORS(app, origins=origins)
@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/data', methods=['GET'])
def data_page():
   return jsonify({"message": "Hello from Flask!"})

@app.route('/api/name', methods=['GET'])
def name_page():
   name = request.args.get('name')
   name_data = requests.get('https://api.nationalize.io/?',params={'name':name})
   return name_data.json()

@app.route('/api/age', methods=['GET'])
def age_page():
   name = request.args.get('name')
   age_data = requests.get('https://api.agify.io?',params={'name':name})
   result = age_data.json()
   return result

@app.route('/api/gender', methods=['GET'])
def gender_page():
   name = request.args.get('name')
   gender_data = requests.get('https://api.genderize.io',params={'name':name})
   result = gender_data.json()
   return result

@app.route('/api/country_code', methods=['GET'])
def country_code():
   code = request.args.get('code')
   name = country_name(code)
   return name
def country_name(code):
   try:
       country = pycountry.countries.get(alpha_2=code)
       return country.name
   except:
       return "Invalid country code"
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)