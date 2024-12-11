from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.views import generic as views
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from .forms import MTUserCreateForm, LoginForm, MTUserEditForm
from .models import MoniTouringUser

# Create your views here.


class UserRegisterView(views.CreateView):
    model = MoniTouringUser
    form_class = MTUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('index')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = MoniTouringUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        monitors = self.object.monitor_set.all()
        paginator = Paginator(monitors, 2)
        page_num = self.request.GET.get('page') or 1
        page_obj = paginator.get_page(page_num)

        context.update({
            "paginator": paginator,
            "page_num": page_num,
            "page_obj": page_obj,
            "monitors": monitors
        })

        return context


class UserEditView(views.UpdateView):
    model = MoniTouringUser
    form_class = MTUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class UserDeleteView(views.DeleteView):  # doesnt work
    model = MoniTouringUser
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('index')

    # def post(self, request, *args, **kwargs):
    #     user_to_delete = self.get_object()
    #     if user_to_delete == request.user:
    #         return redirect('profile details', pk=request.user.pk)
    #
    #     user_to_delete.delete()
    #     return redirect(self.success_url)

    def post(self, *args, pk):
        self.request.user.delete()
        return redirect(self.success_url)
