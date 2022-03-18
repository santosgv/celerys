from celery import shared_task
from PIL import Image ,ImageDraw, ImageFont
from django.core.mail import send_mail

@shared_task
def cria_convite_envia_email(nome , email):
    font = ImageFont.truetype("./templates/font/font1.ttf", size=80)
    imagem = Image.open("./templates/static/img/convite.png").convert("RGBA")
    lapis = ImageDraw.Draw(imagem)
    lapis.text((32,602),
    text=f'Bem vindo {nome} ao nosso treinamento',
    fill="#000",
    font=font)
    imagem.save(f"./templates/static/img/{email}.png")

       # pessoa=Pessoa(nome=nome, email=email)
       # pessoa.save()
        
    send_mail('CADASTRO CONFIRMADO',f'Parabens por este passo importante na sua carreira {nome}','santosgomesv@gmail.com',recipient_list=[email])