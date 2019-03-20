
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/hello')
def helloWorldHandler():
    return 'Hello World from Flask!'
 

@app.route('/bracket')
def bracketHandler():
    
    return 'Hello World from Flask!'
 
app.run(host='0.0.0.0', port= 8090)

# class GameModel:
# class TeamModel:
# class UserModel:
