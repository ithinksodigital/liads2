from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers

#
def home(request):
    specialism = Specialism.objects.all()
    specialism_list= [ ]
    for i in specialism:
        l = {"id" : i.pk, "name": i.specialism_name,}
        specialism_list.append(l)

    app_json = json.dumps(specialism_list)
    # return HttpResponse(app_json, content_type='application/json')
    context = {'specialism_list': specialism_list}
    return render(request, 'generator/index.html', context)




def specialism(request, specialism_id):
    query = request.GET.get('q')
    if query:
        specialism_id = specialism_id
        specialism = Specialism.objects.get(pk=specialism_id)
        backgrounds = BackgroundImage.objects.filter(specialism=specialism_id, background_file__contains=query)
        context = {'backgrounds' : backgrounds,'specialism' : specialism}
        return render(request, 'generator/choose-background.html', context)
    else:
        specialism_id = specialism_id
        specialism = Specialism.objects.get(pk=specialism_id)
        backgrounds = BackgroundImage.objects.filter(specialism=specialism_id)
        context = {'backgrounds' : backgrounds,'specialism' : specialism}
        return render(request, 'generator/choose-background.html', context)

def create_photo(request, specialism_id, photo_id):
    specialism_id = specialism_id
    photo_id = photo_id
    photo = BackgroundImage.objects.get(pk=photo_id)
    specialism = Specialism.objects.get(pk=specialism_id)
    context = {'photo':photo, 'specialism': specialism}
    return render(request, 'generator/create-photo.html', context)

    # background_list = []
    # for i in backgrounds:
    #     l = {"id" : i.pk, "name": i.background_name, "url": i.background_file }
    #     background_list.append(l)
    # app_json = json.dumps(background_list)
    # return HttpResponse(app_json, content_type='application/json')


# def post(request, post_id):
#     try:
#         post_id = post_id
#         post = Blog.objects.get(pk=post_id)
#         user = User.objects.get(pk=post.post_author.pk)
#         user_ = user.username
#
#         data = {
#             "post_id" : post.pk,
#             "post_title": post.post_title,
#             "post_text": post.post_text,
#             "post_author":user_,
#             "post_img" : "http://127.0.0.1:8000"+post.post_picture.url,
#             "post_img_alt": post.post_picture_alt,
#
#         }
#         app_json = json.dumps(data)
#         # serialized_object = serializers.serialize('json', [data,])
#
#         return HttpResponse(app_json, content_type='application/json')
#     except:
#         data = {
#             "post_title" : "This post don't exist",
#         }
#         app_json = json.dumps(data)
#
#         return HttpResponse(app_json, content_type='application/json')