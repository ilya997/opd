from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, forms
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Profile


class RegisterView(CreateView):
    form_class = forms.UserCreationForm
    template_name = "app/register.html"
    success_url = reverse_lazy("app:about-me")

    def form_valid(self, form):
        responce = super().form_valid(form)
        email = self.request.POST['email']
        Profile.objects.create(user=self.object, email=email)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return responce


class AbouMeViews(TemplateView):
    template_name = "app/about-me.html"

def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("app/about-me.html")
        return render(request=request, template_name='app/logon.html')
    
    username = request.POST['username']
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("app/about-me.html")
    return render(request, "app/logon.html", {'error': 'Invalid Login'})

def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("app:login"))