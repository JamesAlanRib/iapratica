from openai import OpenAI

def conversa_com_openai(openai_client, system_pront, user_prompt):


    resposta = openai_client.chat.completions.create(
        model = "gpt-4o-2024-08-06",
        messages = [
            {'role': 'system', 'content': system_pront},
            {'role': 'user', 'content': user_prompt}
        ],
        temperature=0.7
    )

    print(resposta.choices[0].message.content)


if __name__ == "__main__":
    openai_client = OpenAI(api_key = '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')
    system_prompt = "Você é um cientista muito famoso como por exemplo Einsten"
    user_prompt = "Me explique a teoria da relatividade"

    resposta = conversa_com_openai(openai_client, system_prompt, user_prompt)
    print (resposta)