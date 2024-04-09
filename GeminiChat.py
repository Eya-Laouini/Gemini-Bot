from flask import Flask, request, render_template, redirect, url_for, session
from flask_session import Session 
import google.generativeai as genai
from api import Gemini_API_KEY as api
import markdown

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"  
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-pro')

print(dir(model))

@app.route('/', methods=['GET', 'POST'])
def chat():
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST':
        user_message = request.form['message']
        ai_response_markdown = model.generate_content(user_message).text
        ai_response_html = markdown.markdown(ai_response_markdown)  # Convert Markdown to HTML
        session['chat_history'].append((user_message, ai_response_html))  # Store HTML in session
        session.modified = True
        return redirect(url_for('chat'))

    return render_template('chat.html', chat_history=session['chat_history'])

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['chat_history'] = [] 
    session.modified = True
    return redirect(url_for('chat'))  


if __name__ == "__main__":
    app.run(debug=True)
