from django.db import models


class NPoems(models.Model):
    LEVEL_STATUS = (
        ('E', '지렁이'),
        ('N', '일반인'),
        ('H', '박명수'),
    )

    nickname = models.CharField(
        max_length=15,
        blank=False
    )

    level = models.CharField(
        max_length=1,
        choices=LEVEL_STATUS,
        blank=False
    )

    word = models.CharField(
        max_length=10,
        blank=False
    )

    result_text = models.TextField(
        blank=False
    )

    time = models.IntegerField(
        default=0
    )

    time_out = models.IntegerField(
        default=0
    )

    like = models.IntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def get_rank_info(self):
        return {
            'nickname': self.nickname,
            'level': self.get_level_display(),
            'word': self.word,
            'result_text': [self.result_text.split('!@')],
            'time': self.time,
            'time_out': self.time_out,
            'like': self.like,
        }
