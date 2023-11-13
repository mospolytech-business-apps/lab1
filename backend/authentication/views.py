from rest_framework.exceptions import ValidationError,NotFound, AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from authentication.models import User
from authentication.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class  UserViewset(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
 
    @action (methods=['POST'],detail= False,url_path="register")
    def register(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'massage': 'success'})
    

    @action(methods=['POST'], detail=False, url_path="login")
    def login(self, request):
        if 'Email' not in request.data:
            raise ValidationError({'error': 'email must not be empty'})

        if 'password' not in request.data:
            raise ValidationError({'error': 'password must not be empty'})

        try:
            user = User.objects.get(Email=request.data['Email'])
        except User.DoesNotExist:
            raise NotFound({'error': 'user with this email was not found'})

        if user.is_banned:
            raise AuthenticationFailed({'error': 'You are banned. Please contact support.'})

        if not user.check_password(request.data['password']):
            raise AuthenticationFailed({'error': 'incorrect password'})

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.data = {'access': str(refresh.access_token)}
        return response

    @action (methods=['GET'],detail= False,permission_classes=[IsAuthenticated],url_path="me")
    def get_user(self, request):
        user = request.user
        data =self.serializer_class(user).data
        return Response(data)
    
    @action(methods=['GET'], detail=False, permission_classes=[IsAdminUser], url_path="all-users")
    def get_all_users(self, request):
         users = User.objects.all()
         serializer = self.serializer_class(users, many=True)
         return Response(serializer.data)
    
    @action(methods=['PUT'], detail=True, url_path="ban-users")
    def ban_user(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound({'error': 'Пользователь не найден'})

        # Установите поле is_banned в True
        user.is_banned = True
        user.save()
        return Response({'message': 'Статус блокировки пользователя успешно обновлен'})

    @action(methods=['POST'], detail=True, permission_classes=[IsAdminUser], url_path="unban-users")
    def unban(self, request, pk=None):
        user = self.get_object()
        user.is_banned = False
        user.save()
        return Response({'message': 'Пользователь разбанен'})

    @action(methods=['PUT'], detail=True, permission_classes=[IsAdminUser], url_path="grant-admin-status")
    def grant_admin_status(self, request, pk=None):
        user = self.get_object()
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return Response({'message': 'Статус админа присвоен'})

    @action(methods=['PUT'], detail=True, permission_classes=[IsAdminUser], url_path="revoke-admin-status")
    def revoke_admin_status(self, request, pk=None):
        user = self.get_object()
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return Response({'message': 'Статус админа снят'})


        

    


        

            





   
