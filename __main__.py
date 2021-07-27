from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/childs",methods=['GET'])
def hello_world():
    model.connexion()
    childs = model.getChild()
    return jsonify(childs)

@app.route('/stupidity', methods=['POST'])
def stupidity():
    if request.method == 'POST':
        idChild = request.json['id']  
        result = model.setStupidity(idChild)      
        return jsonify(result)
    
    
    
@app.route("/stupidity/<id>",methods=['GET'])
def getStupidity(id):
    model.connexion()
    error = model.getCountStupidityById(id)
    return jsonify(error)    


if __name__ == "__main__":
    app.run()
    
    
    
    



