from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def chat_view(request):
    return render(request,'portal/uerrchat.html')

@csrf_exempt
def chat_api(request):
    print(request.method)
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message','')
        print("estou aqui 1")
        if not user_message:
            return JsonResponse({'error': 'Mensagem não fornecida'}, status=400)

        try:
            # Usando o novo cliente OpenAI com 'responses.create'
            response = cliente.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Você é um assistente de codificação que fala como um pirata."},
                    {"role": "user", "content": user_message},
                ]
            )

            #reply = response.choices[0].message.content
            reply = {"texto": "Olá, tudo bem?"}
            
            return JsonResponse({'response': reply})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método não permitido'}, status=405)
    