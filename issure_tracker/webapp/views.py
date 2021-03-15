from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.models import Tracer, Type, Status
from django.views.generic import View, TemplateView
from webapp.forms import TracerForm, TracerDeleteForm


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tracers'] = Tracer.objects.all()
        return context


class TracerView(TemplateView):
   template_name = 'view.html'
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['tracer'] = get_object_or_404(Tracer, pk=kwargs['pk'])
       return context



class CreateView(View):
    def get(self, request, *args, **kwargs):
        form = TracerForm()
        return render(request, 'create.html', {'form': form})


    def post(self, request, *args, **kwargs):
        form = TracerForm(data=request.POST)
        if form.is_valid():
            tracer = Tracer.objects.create(
                surname=form.cleaned_data.get("surname"),
                description=form.cleaned_data.get("description"),
                status=form.cleaned_data.get("status"),
            )
            tracer.type.set(form.cleaned_data.get("type"))
            return redirect('view', pk=tracer.id)
        return render(request, 'create.html', context={'form': form})


class UpdateView(View):
    def get(self, request, **kwargs):
        tracer = get_object_or_404(Tracer, pk=kwargs['pk'])
        form = TracerForm(initial={
            'surname': tracer.surname,
            'description': tracer.description,
            'status': tracer.status,
            'type': tracer.type.all(),

        })
        return render(request, 'update.html', context={'form': form, 'tracer': tracer})

    def post(self, request, **kwargs):
        tracer = get_object_or_404(Tracer, pk=kwargs['pk'])
        form = TracerForm(data=request.POST)
        if form.is_valid():
            tracer.surname = form.cleaned_data.get("surname")
            tracer.description = form.cleaned_data.get("description")
            tracer.status = form.cleaned_data.get("status")
            tracer.type.set(form.cleaned_data.get("type"))
            tracer.save()
            return redirect('view', pk=tracer.id)
        return render(request, 'update.html', context={'form': form, 'tracer': tracer})


class DeleteView(View):
    def get(self, request, **kwargs):
        tracer = get_object_or_404(Tracer, pk=kwargs['pk'])
        form = TracerDeleteForm()
        return render(request, 'delete.html', context={'tracer': tracer, 'form': form})

    def post(self, request, **kwargs):
        tracer = get_object_or_404(Tracer, pk=kwargs['pk'])
        form = TracerDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['surname'] != tracer.surname:
                form.errors['surname'] = ['Названия записи не совпадают']
                return render(request, 'delete.html', context={'tracer': tracer, 'form': form})
            tracer.delete()
            return redirect('list')
        return render(request, 'delete.html', context={'tracer': tracer, 'form': form})



