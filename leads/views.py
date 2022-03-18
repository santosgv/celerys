from tkinter import font
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .tasks import cria_convite_envia_email



def home(request):
    return render(request,'principal.html')

def valida(request):
    nome =request.POST.get('nome')
    email =request.POST.get('email')


    if len(nome) < 3 or len(email) < 10:
        return HttpResponse('Email ou senha invalidos')

    try:  
       # font = ImageFont.truetype("./templates/font/font1.ttf", size=80)
       # imagem = Image.open("./templates/static/img/convite.png").convert("RGBA")
       # lapis = ImageDraw.Draw(imagem)
       # lapis.text((32,602),
       # text=f'Bem vindo {nome} ao nosso treinamento',
       # fill="#000",
       # font=font)
       # imagem.save(f"./templates/static/img/{email}.png")

       # pessoa=Pessoa(nome=nome, email=email)
       # pessoa.save()
        
        #send_mail('CADASTRO CONFIRMADO',f'Parabens por este passo importante na sua carreira {nome}','santosgomesv@gmail.com',recipient_list=[email])
        
        cria_convite_envia_email.delay(nome, email)
        return render(request, 'envio.html',{'nome':nome,
                                            'email':email,
                                            })


    except Exception as e:
        return HttpResponse(f'{e}')
