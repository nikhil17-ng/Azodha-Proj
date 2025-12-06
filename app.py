from flask import Flask 
import os 
app = Flask(__name__) 


@app.get('/health') 
def health(): 
    return "Health OK ! ", 200

@app.get('/predict')
def predict():
    return {"score": 0.75}, 200
   

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True)
