from djongo import models
from datetime import datetime


class Text(models.Model):
    text_id = models.CharField(max_length = 200)
    inp_text = models.CharField(max_length = 100)
    output_text = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.output_text