from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.permissions import BasePermission, SAFE_METHODS

from authentication.models import User
from authentication.serializers import UserSerializer
from office.models import Office
from jose import jwt
from core.settings import SECRET_KEY


class ListViewPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or view.action in ["list"]


class AuthenticationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser | ListViewPermission]

    def list(self, request):
        api = {}

        actions = self.get_extra_actions()
        names = [a.__name__ for a in actions]
        urls = [a.url_name for a in actions]

        for name, url in zip(names, urls):
            api[name] = self.reverse_action(url)

        return Response(api)

    @action(
        methods=["GET"],
        detail=True,
        permission_classes=[IsAdminUser],
        url_path=r"password",
    )
    def get_user(self, request, id):
        user = User.objects.get(id=id)

        data = UserSerializer(user).data

        return Response(data)

    @action(
        methods=["GET"],
        detail=False,
        url_path="me",
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):
        access_token = request.headers.get("Authorization").split(" ")[1]

        secret_key = SECRET_KEY

        try:
            decoded_token = jwt.decode(
                access_token, key=secret_key, algorithms=["HS256"]
            )

            user_id = decoded_token["user_id"]

            user = User.objects.get(id=user_id)

            data = self.serializer_class(user).data
            return Response(data)
        except jwt.ExpiredSignatureError:
            return Response({"error": "Token has expired"}, status=401)
        except jwt.JWTError:
            return Response({"error": "Invalid token"}, status=401)

    @action(
        methods=["POST"], detail=False, url_path="login", permission_classes=[AllowAny]
    )
    def login(self, request):
        if "email" not in request.data:
            raise ValidationError({"error": "email must not be empty"})
        if "password" not in request.data:
            raise ValidationError({"error": "password must not be empty"})

        try:
            user = User.objects.get(email=request.data["email"])
        except User.DoesNotExist:
            raise NotFound({"error": "user with this email was not found"})

        if not user.check_password(request.data["password"]):
            raise AuthenticationFailed({"error": "password is not correct"})

        if not user.is_active:
            raise AuthenticationFailed({"error": "user is not active"})

        # Получите текущее время входа
        current_login_time = timezone.now()

        # Получите существующие данные времени входа и выхода из JSON-поля
        login_logout_times = user.login_logout_times or {}

        # Добавьте время входа в JSON-поле
        login_logout_times[current_login_time.isoformat()] = None

        # Обновите JSON-поле
        user.login_logout_times = login_logout_times
        user.save()

        data = self.serializer_class(user).data

        refresh = RefreshToken.for_user(user)

        response = Response()
        response.set_cookie("refresh", str(refresh))
        response.data = {"access": str(refresh.access_token), "data": data}

        return response

    @action(
        methods=["POST"],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path="logout",
    )
    def logout(self, request):
        error = request.data.get("error")
        user = User.objects.get(id=request.user.id)

        # Получите текущее время выхода
        current_logout_time = timezone.now()

        # Получите существующие данные времени входа и выхода из JSON-поля
        login_logout_times = request.user.login_logout_times or {}

        # Найдите последнее время входа и добавьте к нему время выхода
        last_login_time = max(login_logout_times.keys(), default=0)
        login_logout_times[last_login_time] = {
            "logout_time": current_logout_time.isoformat(),
            "error": error,
        }

        # Обновите JSON-поле
        setattr(user, "login_logout_times", login_logout_times)
        user.save()

        response = Response()
        response.delete_cookie("refresh")

        return response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().exclude(email="admin@admin.com")
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    @action(
        methods=["DELETE"],
        detail=False,
        permission_classes=[IsAdminUser],
        url_path=r"delete/(?P<id>.*)",
    )
    def delete_user(self, request, id):
        if not id:
            return Response({"error": "not user id provided"})

        try:
            user = User.objects.get(id=id)
        except:
            return Response({"error": "user with this id was not found"})

        user.delete()
        return Response({"message": "user delete"})

    @action(
        methods=["PATCH"],
        detail=False,
        permission_classes=[IsAdminUser],
        url_path="edit/(?P<id>.*)",
    )
    def edit(self, request, id):
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        office = request.data.get("office")
        login_logout_times = request.data.get("login_logout_times")
        is_active = request.data.get("is_active")
        is_superuser = request.data.get("is_superuser")

        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise NotFound({"error": "user with this id was not found"})

        if email:
            setattr(user, "email", email)
        if first_name:
            setattr(user, "first_name", first_name)
        if last_name:
            setattr(user, "last_name", last_name)
        if is_active is not None:
            user.is_superuser = is_superuser
        if is_active is not None:
            user.is_active = is_active
        office = request.data.get("office")
        if office:
            setattr(user, "office", Office.objects.get(title=office))
        login_logout_times = request.data.get("login_logout_times")
        if login_logout_times is not None:
            setattr(user, "login_logout_times", login_logout_times)

        user.is_new = False
        user.save()

        data = self.serializer_class(user).data

        return Response(data)

    @action(
        methods=["POST"], detail=False, url_path="add", permission_classes=[IsAdminUser]
    )
    def add_user(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        first_name = serializer.validated_data.get("first_name")
        last_name = serializer.validated_data.get("last_name")
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        office = serializer.validated_data.get("office")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            office=office,
            is_superuser=False,
        )

        user.set_password(password)
        user.save()

        return Response(UserSerializer(user).data)

    @action(
        methods=["PUT"],
        detail=False,
        permission_classes=[IsAdminUser],
        url_path="ban/(?P<id>\d+)",
    )
    def ban(self, request, id):
        if not id:
            return Response({"error": "Not user id provided"})
        try:
            user = User.objects.get(id=id)
        except:
            return Response({"error": "User with this id was not found"})

        user.is_new = False
        user.is_active = False

        user.save()

        return Response({"message": "Login disabled"})

    @action(
        methods=["PUT"],
        detail=False,
        permission_classes=[IsAdminUser],
        url_path="unban/(?P<id>\d+)",
    )
    def ban1(self, request, id):
        if not id:
            return Response({"error": "Not user id provided"})
        try:
            user = User.objects.get(id=id)
        except:
            return Response({"error": "User with this id was not found"})

        user.is_new = False
        user.is_active = True

        user.save()

        return Response({"message": "Login enabled"})

    @action(
        methods=["PUT"],
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path="change-logout-info/(?P<id>\d+)",
    )
    def change_logout_info(self, request, id):
        if not id:
            return Response({"error": "Not user id provided"})
        try:
            user = User.objects.get(id=id)
        except:
            return Response({"error": "User with this id was not found"})

        login_time = request.data.get("loginTime")
        reason = request.data.get("reason")

        if login_time is None:
            return Response({"error": "loginTime is required"})
        if reason is None:
            return Response({"error": "reason is required"})

        user.login_logout_times[login_time] = {"logout_time": None, "error": reason}

        user.save()

        return Response({"message": "Logout info changed"})
