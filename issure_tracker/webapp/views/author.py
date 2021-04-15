from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView
from webapp.forms import ProjectUserForms
from webapp.models import Project


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'user/update.html'
    form_class = ProjectUserForms
    context_object_name = 'project'
    permission_required = 'webapp.add_delete_change'

    def has_permission(self):
        return self.request.user in self.get_object().user.all() and super().has_permission()

    def get_success_url(self):
        return reverse('project:project_view', kwargs={'pk': self.object.pk})


