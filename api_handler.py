from groq import Groq


def send_query_get_response(client, user_question):
    try:
        # Enhance question (optional context)
        user_question = user_question + (
            " and if relevant, mention which document or topic the answer is based on."
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",   # you can change model
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI tutor. Answer clearly and concisely."
                },
                {
                    "role": "user",
                    "content": user_question
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"