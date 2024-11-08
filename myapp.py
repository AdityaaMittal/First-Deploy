from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(
    base_url="https://api-inference.huggingface.co/v1/",
    api_key="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"
)

@app.route('/')
def home():
    return render_template('myapp.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Get the input text from the form
    user_input = request.form['user_input']

    # Prepare the messages
    messages = [
        {
            "role": "user",
            "content": f"{user_input}"
        }
    ]
    
    try:
        # Call the model
        stream = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct", 
            messages=messages, 
            max_tokens=500,
            stream=True
        )
        
        # Get the response
        translated_text = ""
        for chunk in stream:
            translated_text += chunk.choices[0].delta.content
        
        return render_template('myapp.html', translated_text=translated_text, user_input=user_input)

    except Exception as e:
        return render_template('myapp.html', translated_text=f"Error: {str(e)}", user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
