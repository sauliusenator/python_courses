from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Preke
from .forms import PrekeForm

def prekiu_sarasas(request):
    query = request.GET.get('q', '')
    kategorija = request.GET.get('kategorija', '')
    prekes = Preke.objects.all()
    if query:
        prekes = prekes.filter(pavadinimas__icontains=query)

    if kategorija:
        prekes = prekes.filter(kategorija=kategorija)
    context = {
        'prekes': prekes,
        'kategorijos': Preke.KATEGORIJOS,
    }
    return render(request, 'katalogas/prekiu_sarasas.html', context)
def nauja_preke(request):
    if request.method == 'POST':
        form = PrekeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prekiu_sarasas')
    else:
        form = PrekeForm()
    return render(request, 'katalogas/preke_forma.html', {'form': form})

def redaguoti_preke(request, pk):
    preke = get_object_or_404(Preke, pk=pk)
    if request.method == 'POST':
        form = PrekeForm(request.POST, instance=preke)
        if form.is_valid():
            form.save()
            return redirect('prekiu_sarasas')
    else:
        form = PrekeForm(instance=preke)
    return render(request, 'katalogas/preke_forma.html', {'form': form})
class IstrintiPreke(DeleteView):
    model = Preke
    success_url = reverse_lazy('prekiu_sarasas')
    template_name = 'katalogas/preke_istrinti.html'