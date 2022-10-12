from django.shortcuts import render
from .models import Category, Product

products = Product.objects.all()
categories = Category.objects.all()

def GetList(request):
    return render(request, 'index.html')

def GetBouquets(request):
    return render(request, 'bouquets.html', {'bouquets': products})
    #return render(request, 'bouquets.html', {'bouquets': [{'title': 'Букет с пионовидными розами', 'id': 1, 'img': '/../../../../../../static/images/bouquet1.jpg'},
    #                  {'title': 'Космические орхидеи с красными розами', 'id': 2, 'img': '/../../../../../../static/images/bouquet2.jpg'},
     #                 {'title': 'Нежная эустома с ирисами', 'id': 3, 'img': '/../../../../../../static/images/bouquet3.jpg'},
      #                {'title': 'Тайна с пионовидной розой', 'id': 4, 'img': '/../../../../../../static/images/bouquet4.jpg'},
       #               {'title': 'Космический комплимент', 'id': 5, 'img': '/../../../../../../static/images/bouquet5.jpg'},
        #              {'title': 'Сиреневая мечта', 'id': 6, 'img': '/../../../../../../static/images/bouquet6.jpg'}]
    #})

def GetPlants(request):
    return render(request, 'plants.html', {'plants': products})
    #return render(request, 'plants.html', {'plants': [{'title': 'Эхеверии в сердце', 'id': 1, 'img': '/../../../../../../static/images/plant1.jpg'},
                   # {'title': 'Кактусы в соте', 'id': 2, 'img': '/../../../../../../static/images/plant2.jpg'},
                   # {'title': 'Спатифиллум в призме', 'id': 3, 'img': '/../../../../../../static/images/plant3.jpg'},
                   # {'title': 'Бамбук', 'id': 4, 'img': '/../../../../../../static/images/plant4.jpg'},
                   # {'title': 'Флорариум Додекаэдр', 'id': 5, 'img': '/../../../../../../static/images/plant5.jpg'},
                   # {'title': 'Замиокулькас', 'id': 6, 'img': '/../../../../../../static/images/plant6.jpg'}]})

def GetFlowers(request):
    return render(request, 'flowers.html', {'flowers': products})
    #return render(request, 'flowers.html', {'flowers': [{'title': 'Роза одноголовая 50 см', 'id': 1, 'img': '/../../../../../../static/images/flower1.jpg'},
                    #{'title': 'Подсолнух', 'id': 2, 'img': '/../../../../../../static/images/flower2.jpg'},
                    #{'title': 'Красная роза Res Naomi', 'id': 3, 'img': '/../../../../../../static/images/flower3.jpg'},
                    #{'title': 'Роза Пич Аваланж', 'id': 4, 'img': '/../../../../../../static/images/flower4.jpg'},
                    #{'title': 'Тюльпан розовый', 'id': 5, 'img': '/../../../../../../static/images/flower5.jpg'},
                    #{'title': 'Роза пионовидная Джульетта', 'id': 6, 'img': '/../../../../../../static/images/flower6.jpg'}]})

def GetReasons(request):
    return render(request, 'reasons.html')

def GetBirthday(request):
    return render(request, 'birthday.html', {'bd': products})
    #return render(request, 'birthday.html', {'bd': [{'title': 'Подарочный набор из 29 роз и клубники в шоколаде', 'id': 1, 'img': '/../../../../../../static/images/bd1.jpg'},
    #                {'title': 'Подарочный набор "Офелия"', 'id': 2, 'img': '/../../../../../../static/images/bd2.jpg'},
    #                {'title': 'Дуо набор с подсолнухами и клубникой в шоколаде', 'id': 3, 'img': '/../../../../../../static/images/bd3.jpg'}]})

def GetWedding(request):
    return render(request, 'wedding.html', {'wed': products})
    #return render(request, 'wedding.html', {'wed': [{'title': 'Букет невесты', 'id': 1, 'img': '/../../../../../../static/images/wed1.jpg'},
    #                {'title': 'Букет невесты и бутоньерка', 'id': 2, 'img': '/../../../../../../static/images/wed2.jpg'},
    #                {'title': 'Букет нежно-розовый с розой мадам Бомбастик', 'id': 3, 'img': '/../../../../../../static/images/wed3.jpg'}]})