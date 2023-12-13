with open('./prohibited_words.txt', 'r') as f:
    prohibited_words = [line.strip() for line in f.readlines()]    

prompt2 = """Please write a polite one paragraph reply to the following review assuming you are a property management company.

Review:  {0}.

Considering:
- Never mention refunds, free or resource.
- If the review mentions dissatisfaction, reply with 'Thank you for taking the time to write.'.
- If the review mentions refunds, reply with 'Thank you for your feedback'.
- If a person name comes in the review, Do NOT mention it in the response. 
- never use in the review these words {1}.
"""

# Crear una cadena de texto separada por comas de las palabras prohibidas
prohibited_words_str = ', '.join(prohibited_words)

# Formatear el prompt para reemplazar las palabras prohibidas
prompt2 = prompt2.format("{0}", prohibited_words_str)


print(prompt2)