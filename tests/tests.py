from django.test import TestCase


class MyTestingView(TestCase):
    # def test_tow_is_three(self):
    #     self.assertEqual(2,3)

    def test_tow_is_tow(self):
        self.assertEqual(2,2)