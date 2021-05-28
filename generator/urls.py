from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('specialism/<int:specialism_id>', views.specialism, name='specialism'),
    path('specialism/<int:specialism_id>/create/<int:photo_id>', views.create_photo, name='create_photo'),

    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login_request, name='login'),
    # path("logout", views.logout_request, name="logout"),
    # path("add/", views.photo_add, name="photo-add"),
    # path("search/", views.search, name="search"),
    # path("follow/", views.follow, name="follow"),
    # path("contacts/", views.contacts, name="contacts"),
    # path("contact_form/", views.send_message, name="send_message"),
    # path("newsletter/", views.newsletter, name="newsletter"),
    # path("inmails/", views.inmails, name="inmails"),
    # path("inmail/<int:inmail_id>", views.inmail, name="inmail"),
    # path("detail/<int:img_id>", views.detail, name="detail"),
    # path("like/<int:img_id>", views.like, name="like"),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)