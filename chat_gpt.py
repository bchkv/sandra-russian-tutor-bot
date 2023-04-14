import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]


async def chat_gpt_response(prompt):
    model_engine = "gpt-3.5-turbo"  # Replace with the desired model engine

    prompt_finished = f"""
    Я хочу чтобы ты перевел фрагмент '{prompt}' на русский язык. 
    Приведи два-три варианта перевода.
    """

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{prompt_finished}"}
        ],
        n=1,
        temperature=0.7
    )

    message = completion.choices[0].message["content"]
    return message
