from django.http import HttpResponse
from django.shortcuts import render
from .forms import  SearchForm,UpdateForm
from .models import SearchResult
from django.http import JsonResponse
from django.db.models import Q

def index(request):
    return render(request,'index.html')

def index1(request):
    return render(request,'index1.html')

def create_form(request):
    form = SearchForm()
    return render(request, 'create.html', {'form': form})

def create_form_data(request):
    urls = request.POST.get('urls')
    title = request.POST.get('title')
    description = request.POST.get('description')
    print("@@@@")
    print(urls, title,description)
    results = SearchResult (urls=urls, title=title ,description=description)
    results.save()
    return HttpResponse("created successfully")

def update_form(request,id):
    sr = SearchResult.objects.get(id=id)
    print("Updating the searchresult %s" % sr)
    form = SearchForm(instance=sr)
    return render(request, 'update.html', {'form': form, 'id':id})

def get_search_result(request,id):
    sr = SearchResult.objects.get(id=id)
    resultdict = {}
    resultdict["title"] = sr.title
    resultdict["urls"] = sr.urls
    resultdict["description"] = sr.description
    return JsonResponse(resultdict)

def get_all_search_result(request):
    searchresults = SearchResult.objects.all()
    print(searchresults)
    results = []
    for sr in searchresults:
        resultdict = {}
        resultdict["title"] = sr.title
        resultdict["urls"] = sr.urls
        resultdict["description"] = sr.description
        results.append(resultdict)

    return JsonResponse(results,safe=False)


def get_search_query(request):
    q = request.GET.get('q')
    if not q:
       return JsonResponse({"error":"q not found"}, safe=False)
    #query = SearchResult.objects.filter(title__contains= q)
    searchresults = SearchResult.objects.filter(Q(title__contains=q) |  Q(description__contains=q) |  Q(urls__contains=q))
    print(searchresults.query)
    results = []
    for sr in searchresults:
        resultdict = {}
        resultdict["title"] = sr.title
        resultdict["urls"] = sr.urls
        resultdict["description"] = sr.description
        results.append(resultdict)
        results.append(resultdict)
    return JsonResponse(results, safe=False)


def update_form_data(request,id):
    obj = SearchResult.objects.get(id=id)
    urls = request.POST.get('urls')
    title = request.POST.get('title')
    description = request.POST.get('description')
    obj.urls = urls
    obj.title = title
    obj.description = description
    obj.save()
    return HttpResponse("updated successfully")

def delete_form(request,id):
    sr = SearchResult.objects.get(id=id)
    print("Remove the searchresult %s" % sr)
    form = SearchForm(instance=sr)
    return render(request, 'delete.html', {'form': form, 'id':id})


def delete_form_data(request,id):
    obj = SearchResult.objects.get(id=id)
    urls = request.POST.get('urls')
    title = request.POST.get('title')
    description = request.POST.get('description')
    obj.urls = urls
    obj.title = title
    obj.description = description
    obj.delete()
    return HttpResponse("Removed successfully")



