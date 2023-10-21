import openai

def GetResponse(text):
    try:
        openai.api_key = "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"
        result = openai.Completion.create(model = "GPT-3.5",
                                          prompt = text,
                                          n = 1,
                                          max_tokens = 500)
        response = result.choices[0].text
        return response
    except Exception as exception:
        print(exception)
        return "error"