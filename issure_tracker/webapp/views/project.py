from django.views.generic import CreateView, DetailView, ListView, View, UpdateView, DeleteView
from webapp.models import Project, Tracer
from django.urls import reverse_lazy
from webapp.forms import ProjectForm, TracerForm, SearchForm, ProjectDeleteForm
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
class ProjectIndexView(ListView):

    template_name = 'project/index.html'
    model = Project
    context_object_name = 'projects'
    ordering = ('name', '-start_data')
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProjectIndexView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
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


class ProjectCreateView(PermissionRequiredMixin, CreateView):

    template_name = 'tracer/create.html'
    model = Project
    form_class = ProjectForm
    permission_required = 'webapp.add_project'


    def get_success_url(self):
        return reverse('project:project_view', kwargs={'pk': self.object.pk})


class ProjectTracerCreate(PermissionRequiredMixin, CreateView):
    model = Tracer
    template_name = 'tracer/create.html'
    form_class = TracerForm
    permission_required = 'webapp.add_tracker'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        tracer = form.save(commit=False)
        tracer.project = project
        tracer.save()
        form.save_m2m()
        return redirect('project:project_view', pk=project.pk)


class ProjectView(DetailView):
    model = Project
    template_name = 'project/view.html'
    context_object_name = 'project'


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    context_object_name = 'project'
    permission_required = 'webapp.change_project'

    def get_success_url(self):
        return reverse('project:project_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):

    template_name = 'project/delete.html'
    model = Project
    context_object_name = 'project'
    permission_required = 'webapp.delete_project'
    success_url = reverse_lazy('project:project_list')



