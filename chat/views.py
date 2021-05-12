# chat/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from django.shortcuts import render, redirect

from chat.models import MyBanner
from django.template import loader


def index(request):
    qs=MyBanner.objects.all()
    return render(request, 'chat/index.html', {'banners':qs})

    response = render(request, 'chat/index.html', {})
    response.set_cookie('viewed_banners',1)
    num_img = MyBanner.objects.all()
    response.context=num_img
    return response

    # num_img = MyBanner.objects.all()
    # response = render_to_response('chat/index.html', num_img)
    # response.set_cookie('viewed_banners',1)
    # return response


    # t1 = loader.get_template('chat/index.html')
    # context = MyBanner.objects.all()
    # return HttpResponse(t1.render(context)).set_cookie('viewed_banners',1)

    # return render(request, 'chat/index.html', {})
def ckick_banner(request,banner_id):
    try:
        seen=request.COOKIES[f'banner_{banner_id}']
        banner=MyBanner.objects.get(id=banner_id)
        response=redirect('/')
        response.set_cookie(f'banner_{banner_id}',str(int(seen)+1))
        return response
    except:
        response=redirect('/')




def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


