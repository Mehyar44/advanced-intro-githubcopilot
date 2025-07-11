from azure_env import load_azure_openai_env
from openai import AzureOpenAI
from flask import Flask, render_template, request, redirect, url_for

# Load environment variables
azure_config = load_azure_openai_env()

# Create Azure OpenAI client
client = AzureOpenAI(
    api_key=azure_config["api_key"],
    azure_endpoint=azure_config["endpoint"],
    api_version=azure_config["api_version"]
)

app = Flask(__name__)

# Store messages in memory for demo purposes
chat_history = []

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.form.get("message", "")
        if user_message:
            chat_history.append({"role": "user", "content": user_message})
            # Placeholder for AI response, replace with Azure OpenAI call in next step
            ai_response = "This is a placeholder AI response."
            chat_history.append({"role": "ai", "content": ai_response})
        return redirect(url_for("chat"))
    return render_template("chat.html", messages=chat_history)

if __name__ == "__main__":
    try:
        models = client.models.list()
        print("Available models:")
        for model in models:
            print(model.id)
    except Exception as e:
        print("Error connecting to Azure OpenAI:", e)
    app.run(debug=True)