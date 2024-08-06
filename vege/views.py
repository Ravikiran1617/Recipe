from django.shortcuts import render, redirect
from .models import Receipe
from django.http import HttpResponse

def receipes(request):
    search_query = request.GET.get('search', '')  # Get the search term from the GET parameters

    if request.method == "POST":
        receipe_image = request.FILES.get('receipe_image')  # Use request.FILES to get the uploaded file
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')

        Receipe.objects.create(
            receipe_image=receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description
        )
        
        return redirect('receipes')  # Redirect to the same view after form submission
    
    queryset = Receipe.objects.filter(receipe_name__icontains=search_query)  # Filter recipes based on search query
    context = {'receipes': queryset}

    return render(request, 'receipe.html', context)


# def delete_receipe(request,id):
#     # print(1)
#     # return HttpResponse('a')
#     queryset = Receipe.objects.get(id=id)
#     queryset.delete()
#     return redirect('receipes') 

from django.shortcuts import get_object_or_404, redirect
from .models import Receipe

def delete_receipe(request, id):
    if request.method == 'POST':  # Ensure deletion only happens via POST request
        # Fetch the Receipe object or return a 404 error if not found
        receipe = get_object_or_404(Receipe, id=id)
        receipe.delete()  # Call delete() method to remove the object from the database
        return redirect('receipes')  # Redirect to the list of recipes or another page

    # Optionally handle GET requests if necessary
    return redirect('receipes')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipe

def update_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)

    if request.method == "POST":
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        # Update the recipe fields
        receipe.receipe_name = receipe_name
        receipe.receipe_description = receipe_description
        if receipe_image:
            receipe.receipe_image = receipe_image
        receipe.save()

        return redirect('receipes')

    context = {'receipe': receipe}
    return render(request, 'update_receipes.html', context)



#def login():