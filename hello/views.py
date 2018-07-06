from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializers

class SnippetGet(APIView):
    def get(self, request, format=None):
        return Response("Hello")

class SnippetPost(APIView):
    def post(self, request, format=None):
        return Response({"data":request.data['name']})

class UserDetails(APIView):
    def post(self, request, format=None):
     login_instance = User.objects.filter(username=request.data['username']).first()
     if login_instance:
            valid = login_instance.check_password(request.data['password'])
            if not valid:
                return Response("Password Incorrect")
            else:
                return Response("login successful")

class GetUserdetails(APIView):
    def get(self, request,userid):
        user_query = User.objects.filter(id=userid).first()
        response = {"data":{},"message":"User details"}
        if user_query :
            response["data"] = UserSerializers(instance=user_query).data
        else:
            response["message"] = "user details not found"
        return Response(response)

class changepass(APIView):
    def post(self,request):
        user_instance = User.objects.filter(username = request.data['username']).first()
        if user_instance:
            valid = user_instance.check_password(request.data['password'])
            if not valid:
                return Response("Password Incorrect")
            else:
                #TODO SET NEW PASSWORD TO the User
                user_instance.set_password(request.data["new_password"])
                user_instance.save()
                return Response("password updated")
        else:
            return Response("User Not matched")


