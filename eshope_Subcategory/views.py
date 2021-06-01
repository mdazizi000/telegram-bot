from django.shortcuts import render

# Create your views here.
def get_subcat(request):

    return render(request,'subcategory_partial.html',{})