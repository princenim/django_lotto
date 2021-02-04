from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model): # models에서 model 을 가져옴.
    #테이블에 있었으면 하는 열들
    name = models.CharField(max_length=24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    update_date = models.DateTimeField()

    def generate(self): # 로또 번호를 자동으로 생성 # 실행하는 단계에서 행을 기준으로 작동
        self.lottos = "" # 빈 str
        origin = list(range(1,46)) # 1~46의 숫자 리스트
        # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
        for _ in range(0, self.num_lotto):
            random.shuffle(origin) # 섞음.
            guess = origin[:6] # 0,1,2,3,4,5 까지 꺼냄.
            guess.sort() # 오름차순.
            self.lottos += str(guess) +'\n' # 로또 번호 str( ' ')에 6개 번호 set 추가
        self.update_date = timezone.now()  # 실행되는 순간마다의 시간.
        self.save() # GuessNumbers object를 DB에 저장

    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경 , 프린트를 했을 때 이렇게 보여달라고 하는것.
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) # pk는 자동생성됨 , pk = id 동일
