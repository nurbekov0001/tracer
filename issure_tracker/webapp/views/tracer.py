from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.models import Tracer, Type, Status, Project
from django.views.generic import View, TemplateView, FormView, ListView
from django.views.generic import FormView, ListView, CreateView, DetailView
from webapp.forms import TracerForm, TracerDeleteForm, SearchForm, ProjectTracerForm, ProjectForm

from django.db.models import Q
from django.utils.http import urlencode


class IndexView(ListView):

    template_name = 'index.html'
    model = Tracer
    context_object_name = 'tracers'
    ordering = ('surname', '-created_at')
    paginate_by = 10
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



# class TracerView(TemplateView):
#    template_name = 'view.html'
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['tracer'] = get_object_or_404(Tracer, pk=kwargs['pk'])
#        return context


class TracerView(DetailView):
    model = Tracer
    template_name = 'tracer/view.html'



# class CreateView(View):
#     def get(self, request, *args, **kwargs):
#         form = TracerForm()
#         return render(request, 'create.html', {'form': form})
#
#
#     def post(self, request, *args, **kwargs):
#         form = TracerForm(data=request.POST)
#         if form.is_valid():
#             tracer = Tracer.objects.create(
#                 surname=form.cleaned_data.get("surname"),
#                 description=form.cleaned_data.get("description"),
#                 status=form.cleaned_data.get("status"),
#             )
#             tracer.type.set(form.cleaned_data.get("type"))
#             return redirect('view', pk=tracer.id)
#         return render(request, 'create.html', context={'form': form})

class ProjectTracerCreateView(CreateView):

    model = Project
    template_name = 'project_create.html'
    form_class = ProjectTracerForm


    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('article_view', pk=article.pk)

class CreateArticleView(CreateView):
    template_name = 'tracer/create.html'
    form_class = TracerForm
    model = Tracer

    def form_valid(self, form):
        status = form.cleaned_data.pop('status')
        tracer = Tracer()
        for key, value in form.cleaned_data.items():
            setattr(tracer, key, value)

        tracer.save()
        tracer.tags.set(status  )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article-list')


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



