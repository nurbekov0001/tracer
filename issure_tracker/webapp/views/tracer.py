from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.models import Tracer
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from webapp.forms import TracerForm, SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class TracerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Tracer
    template_name = 'tracer/update.html'
    form_class = TracerForm
    context_object_name = 'tracer'
    permission_required = 'webapp.change_tracer'

    def has_permission(self):
        return self.request.user in self.get_object().project.user.all() and super().has_permission()

    def get_success_url(self):
        return reverse('project:view', kwargs={'pk': self.object.pk})


class TracerDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'tracer/delete.html'
    model = Tracer
    context_object_name = 'tracer'
    permission_required = 'webapp.delete_tracer'

    def has_permission(self):
        return self.request.user in self.get_object().project.user.all() and super().has_permission()

    def get_success_url(self):
        return reverse('project:project_view', kwargs={'pk': self.object.project.pk})
