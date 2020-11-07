from django.conf.urls import url
from searchapp import views
from django.urls import path

urlpatterns = [
    #url(r'^$',views.index,name='index'),
    path('index1', views.index1,name='index1'),
    path('create/form', views.create_form,name='createForm'),
    path('create',views.create_form_data,name='createFormData'),
    path('update/<int:id>/form', views.update_form, name="updateForm"),
    path('update/<int:id>', views.update_form_data, name='updateFormData'),
    path('get/<int:id>', views.get_search_result, name='getSearchResult'),
    path('get/all/', views.get_all_search_result, name='getallSearchResult'),
    path('getquery/', views.get_search_query, name='getSearchQueruyResult'),
    path('delete/<int:id>/form', views.delete_form, name="deleteForm"),
    path('update/<int:id>', views.update_form_data, name='updateFormData'),
    path('delete/<int:id>', views.delete_form_data, name='deleteFormData'),

]
