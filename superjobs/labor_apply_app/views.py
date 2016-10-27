from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .forms import PersonalInfoForm
from .models import PersonalInfo
from .serializers import PersonalInfoSerializer, UserSerializer

#Create your views here.
# @login_required(login_url='/accounts/signup')
class PersonalInfoView(CreateView):
    """TODO: CreateView for PersonalInfoForm
    return: TODO
    """
    template_name = 'apply_now.html'
    form_class = PersonalInfoForm
    success_url = 'success/'

    def form_valid(self, form, *args, **kwargs):
        """TODO: Validate form
        return: TODO
        """
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, *args, **kwargs):
        """TODO: handle invalid form request
        return: TODO
        """
        return self.render_to_response(
            self.get_context_data(form=form))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """TODO: this instance should give are views login protection
        return: TODO
        """
        return super(PersonalInfoView, self).dispatch(*args, **kwargs)


class PersonalInfoViewList(APIView):
    """TODO: list all Personal info list, or create a new one
    return: TODO
    """
    def get(self, request, format=None):
        info = PersonalInfo.objects.all()
        serializer = PersonalInfoSerializer(info, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonalInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class PersonalInfoViewDetail(APIView):
    """TODO: retreve, update or delete a personal info
    return: TODO
    """
    def get_object(self, pk):
        try:
            return PersonalInfo.objects.get(pk=pk)
        except PersonalInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        info = self.get_object(pk)
        serializer = PersonalInfoSerializer(info)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        info = self.get_object(pk)
        serializer = PersonalInfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        info = self.get_object(pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    """TODO: handle User persmission and authentication
    return: TODO
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """TODO: handle User permission and auth
    return: TODO
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
