from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from v1.models import Clothing, Color


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )


class UserView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
            return Response({
                "id": user.id,
                "username": user.username
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                "token is invalide or user is not connected", status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            if User.objects.filter(username=user_serializer.validated_data["username"]).exists():
                return Response(
                    {
                        "message": "this username is already exists",
                        "succes": False
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user = user_serializer.save()
            data = {
                "id": user.id,
                "username": user.username,
                "succes": True
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_403_FORBIDDEN)


class ClotheInput(serializers.Serializer):
    label = serializers.CharField(max_length=50)
    image = serializers.ImageField()
    type = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=20)
    hot = serializers.BooleanField(default=True)
    hexcode = serializers.CharField(max_length=7)


class ClotheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = "__all__"


class ColorSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["hexcode"]


class ClotheView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        clothes = Clothing.objects.filter(user_id=user)
        return Response({
            "total": len(clothes),
            "clothes": ClotheSerializer(clothes, many=True).data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        clothe_serializer = ClotheInput(data=request.data)
        user = User.objects.get(pk=request.user.id)
        if clothe_serializer.is_valid():
            clothe = Clothing.objects.create(
                label=clothe_serializer.validated_data["label"],
                image=clothe_serializer.validated_data["image"],
                type=clothe_serializer.validated_data["type"],
                category=clothe_serializer.validated_data["category"],
                hot=clothe_serializer.validated_data["hot"],
                user_id=user
            )
            Color.objects.create(
                hexcode=clothe_serializer.validated_data["hexcode"], clothing_id=clothe)
            return Response({
                "success": True,
                "new_cloth_id": clothe.id
            }, status=status.HTTP_201_CREATED)
        return Response(clothe_serializer.errors, status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
def delete_clothe(request, pk):
    if request.method == 'DELETE':
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
            clothe = Clothing.objects.filter(pk=pk, user_id=user).first()
            clothe.delete()
            return Response({
                "success": True,
                "message": "Clothe deleted"
            }, status=status.HTTP_200_OK)
        return Response(
            {"success": False, "message": "Clothe doesn't belong to this user"},
            status=status.HTTP_403_FORBIDDEN
        )
