from multiprocessing.sharedctypes import Value
from unicodedata import name
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView
from web.models import *

class Inicio(ListView):
    template_name = "index.html"
    model = Empresa
    context_object_name = 'detalle'
    success_url = reverse_lazy('Inicio')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Inicio'
        context['url_anterior'] = '/'
        context['query'] = self.request.GET.get("query") or ""
        return context

  
    

class Producto(ListView):
    template_name = "producto.html"
    model = Productos
    context_object_name = 'productos'
    paginate_by = 4  # Número de productos por página

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            return self.model.objects.filter(nombre__icontains=query)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Bienvenido a mis Productos'
        context['query'] = self.request.GET.get("query") or ""
        return context


# class Producto(ListView):
#     template_name = 'producto.html'

#     def get(self, request):
#         query = request.GET.get('q')
#         productos = Producto.objects.all()

#         if query:
#             productos = productos.filter(nombre__icontains=query)

#         paginator = Paginator(productos, 6)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         form = ProductoForm()

#         contexto = {
#             'page_obj': page_obj,
#             'form': form,
#         }

#         return render(request, self.template_name, contexto)

#     def post(self, request):
#         form = ProductoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')

#         productos = Producto.objects.all()
#         paginator = Paginator(productos, 6)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)

#         contexto = {
#             'page_obj': page_obj,
#             'form': form,
#         }

#         return render(request, self.template_name, contexto)



# class ComprarProductoView(View):
#     def post(self, request, codigo_producto):
#         producto = get_object_or_404(Producto, codigo=codigo_producto)
#         cantidad_comprada = int(request.POST.get('cantidad_comprada', 0))

#         if cantidad_comprada > 0 and cantidad_comprada <= producto.cantidad:
#             producto.cantidad -= cantidad_comprada
#             producto.save()
#             whatsapp_text = f'Hola, me gustaría información sobre el {producto.nombre}. Código: {producto.codigo}'
#             whatsapp_url = f'https://wa.me/593959682902?text={whatsapp_text}'
#             return HttpResponseRedirect(whatsapp_url)

#         return HttpResponseRedirect('/')

#     def get(self, request, codigo_producto):
#         return HttpResponseRedirect('/')
