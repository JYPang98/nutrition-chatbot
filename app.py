from flask import Flask, render_template, jsonify, request
import model
app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/chatbot', methods=["GET", "POST"])
def get_bot_response():
    the_question = request.args.get('msg')
    response = model.chat(the_question)
    if response == "I am sorry, but i do not understand. I am still learning. Please try with another question!":
        with open ("data/unanswered.txt","a+") as f:
            f.seek(0)
            data = f.read(100)
            if len(data) > 0:
                f.write("\n")
            f.write(the_question)
            return response
    else:
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)