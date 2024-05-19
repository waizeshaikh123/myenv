from django.shortcuts import render,HttpResponse


# Create your views here.

def home(request):
    
    peoples = [
        {'name' : 'waize shaikh', 'age': 20},
        {'name' : 'zohaib man', 'age': 22},
        {'name' : 'danish', 'age': 24},
        {'name' : 'neeraj', 'age': 17}
    ]
    
    # vegetables = [
    #     'Tomato','cocumber','potato','onion'
    # ]
    
    return render( request , "index.html", context= {'peoples' : peoples})