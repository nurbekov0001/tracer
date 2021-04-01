from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.models import Tracer, Project
from django.views.generic import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.forms import TracerForm, TracerDeleteForm, SearchForm, ProjectForm

from django.db.models import Q
from django.utils.http import urlencode


class IndexView(ListView):

    template_name = 'tracer/index.html'
    model = Tracer
    context_object_name = 'tracers'
    ordering = ('surname', '-created_at')
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(IndexView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(surname__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context



class TracerView(DetailView):
    model = Tracer
    template_name = 'tracer/view.html'



class ProjectCreateView(CreateView):

    template_name = 'tracer/create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):

        return reverse('view', kwargs={'pk': self.object.pk})


class ProjectTracerCreate(CreateView):
    model = Tracer
    template_name = 'tracer/create.html'
    form_class = TracerForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        tracer = form.save(commit=False)
        tracer.project = project
        tracer.save()
        tracer.save_m2m()
        return redirect('view', pk=project.pk)


# class UpdateView(View):
#     def get(self, request, **kwargs):
#         tracer = get_object_or_404(Tracer, pk=kwargs['pk'])
#         form = TracerForm(initial={
#             'surname': tracer.surname,
#             'description': tracer.description,
#             'status': tracer.status,
#             'type': tracer.type.all(),
#
#         })
#         return render(request, 'tracer/update.html', context={'form': form, 'tracer': tracer})

    # def post(self, request, **kwargs):
    #     tracer = get_object_or_404(Tracer, pk=kwargs['pk'])
    #     form = TracerForm(data=request.POST)
    #     if form.is_valid():
    #         tracer.surname = form.cleaned_data.get("surname")
    #         tracer.description = form.cleaned_data.get("description")
    #         tracer.status = form.cleaned_data.get("status")
    #         tracer.type.set(form.cleaned_data.get("type"))
    #         tracer.save()
    #         return redirect('view', pk=tracer.id)
    #     return render(request, 'tracer/update.html', context={'form': form, 'tracer': tracer})

class UpdateView(UpdateView):
    model = Tracer
    template_name = 'tracer/update.html'
    form_class = TracerForm
    context_object_name = 'tracer'

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.pk})


# class DeleteView(View):
#     def get(self, request, **kwargs):
#         tracer = get_object_or_404(Tracer, pk=kwargs['pk'])
#         form = TracerDeleteForm()
#         return render(request, 'tracer/delete.html', context={'tracer': tracer, 'form': form})
#
#     def post(self, request, **kwargs):
#         tracer = get_object_or_404(Tracer, pk=kwargs['pk'])
#         form = TracerDeleteForm(data=request.POST)
#         if form.is_valid():
#             if form.cleaned_data['surname'] != tracer.surname:
#                 form.errors['surname'] = ['Названия записи не совпадают']
#                 return render(request, 'tracer/delete.html', context={'tracer': tracer, 'form': form})
#             tracer.delete()
#             return redirect('list')
#         return render(request, 'tracer/delete.html', context={'tracer': tracer, 'form': form})

class DeleteView(DeleteView):
    template_name = 'tracer/delete.html'
    model = Tracer
    context_object_name = 'tracer'

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})





