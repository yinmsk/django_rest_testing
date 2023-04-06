from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import MyUser


class MyTestingView(TestCase):
    def test_tow_is_tow(self):
        # 이 테스트는 2와 2가 서로 같은지 확인합니다.
        self.assertEqual(2,2)


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        # 회원가입 API 엔드포인트를 테스트합니다.
        url = reverse('register')
        data = {
            'email': 'test@naver.com',
            'password': 'testpassword'
        }

        # 회원가입 API에 테스트 데이터를 포함한 POST 요청을 전송합니다.
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 회원가입 API에서 생성된 유저 객체를 가져옵니다.
        user = MyUser.objects.get(email=data['email'])

        # 유저 객체의 이메일과 비밀번호가 올바른지 확인합니다.
        self.assertEqual(user.email, data['email'])
        self.assertTrue(user.check_password(data['password']))