import openai

openai.api_key = "REEEEEEEEEEEEEEEEEEEEEEEE"

def get_response(question):
    if question is None:
        return "I'm sorry, there was a problem while recording your question. Please try again."

    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}])
        return response['choices'][0]['message']['content']
    except:
        return "I'm sorry, There seems to be an error with ChatGPT. Try again later."