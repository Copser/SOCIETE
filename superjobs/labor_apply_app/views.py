from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.views.generic.edit import CreateView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .forms import PersonalInfoForm
from .models import PersonalInfo
from .serializers import PersonalInfoSerializer

#Create your views here.
def index(request):
    """TODO: Landing Page
    return: TODO
    """
    return render_to_response(
        'index.html',
        context_instance=RequestContext(request)
    )


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
