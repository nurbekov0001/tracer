from django.views.generic import CreateView, DetailView, ListView, View
from webapp.models import Project, Tracer
from webapp.forms import ProjectForm, TracerForm, SearchForm, ProjectDeleteForm
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.db.models import Q
from django.utils.http import urlencode


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


class ProjectCreateView(CreateView):

    template_name = 'tracer/create.html'
    model = Project
    form_class = ProjectForm


    def get_success_url(self):

        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectTracerCreate(CreateView):
    model = Tracer
    template_name = 'tracer/create.html'
    form_class = TracerForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        tracer = form.save(commit=False)
        tracer.project = project
        tracer.save()
        form.save_m2m()
        return redirect('project_view', pk=project.pk)


class ProjectView(DetailView):
    model = Project
    template_name = 'project/view.html'
    context_object_name = 'project'


class ProjectUpdateView(View):
    def get(self, request, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        form = ProjectForm(initial={
            'name': project.name,
            'description': project.description,
            'start_data': project.start_data,
            'end_data': project.end_data

        })
        return render(request, 'project/update.html', context={'form': form, 'project': project})

    def post(self, request, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            project.name = form.cleaned_data.get("name")
            project.description = form.cleaned_data.get("description")
            project.start_data = form.cleaned_data.get("start_data")
            project.end_data = form.cleaned_data.get("end_data")
            project.save()
            return redirect('project_view', pk=project.id)
        return render(request, 'project/update.html', context={'form': form, 'project': project})


class ProjectDeleteView(View):
    def get(self, request, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        form = ProjectDeleteForm()
        return render(request, 'project/delete.html', context={'project': project, 'form': form})

    def post(self, request, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        form = ProjectDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['name'] != project.name:
                form.errors['name'] = ['Названия записи не совпадают']
                return render(request, 'project/delete.html', context={'project': project, 'form': form})
            project.delete()
            return redirect('project_list')
        return render(request, 'project/delete.html', context={'project': project, 'form': form})




