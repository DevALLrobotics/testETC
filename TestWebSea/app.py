from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def test():
    return "ok", 200

@app.route('/iq')
def iq():
    return send_from_directory('static', 'Project_DeepseaM_UI.html')

@app.route('/123')
def go():
    return send_from_directory('static', 'Project_DeepseaC_UI.html')  # If you have this file

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888, debug=True)
