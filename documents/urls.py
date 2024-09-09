from django.urls import path
from . import views


app_name = "document"
urlpatterns = [
    path('', views.Showdoc.as_view()),
    path('Delete/<int:pk>', views.Delete.as_view()),
    path('create',views.UploudDoc.as_view()),
    path('createnew', views.Create.as_view()),
    path('Download/<int:file>',views.Download.as_view()),
    path('update/<int:file>', views.Update.as_view())

]