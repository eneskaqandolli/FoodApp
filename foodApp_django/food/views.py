from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Item
from .forms import ItemForm

from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
class IndexView(ListView):
    model = Item
    template_name = "food/food.html"
    context_object_name = "items"
    
class DetailFoodView(DetailView):
    model = Item
    template_name = "food/food_detail.html"
    context_object_name = "item"

class AddItemView(CreateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "image"]
    template_name = "food/item_form.html"
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def update_item(request, id):
    item = get_object_or_404(Item, id=id)
    
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("food:index")
    else:
        form = ItemForm(instance=item)  # This line should only execute for GET requests
    
    return render(request, "food/item_form.html", {"form": form, "item": item})

def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request, "food/item_delete.html", {"item":item})