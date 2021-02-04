from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers') # GuessNumbers의 하나의 행
        g.generate() # GuessNumbers 클래스의 generate 함수를 실행
        # g.lottos -> 6개씩 5set 총 30개의 숫자 리스트의 str
        print(g.update_date)
        print(g.lottos)

        # 실제 Test case (OK or FAILED)
        # default로 6개 숫자 x 5set = 30개의 숫자가 생성됨을 확인
        self.assertTrue(len(g.lottos) > 20)
