from django.db import models


class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to='media', default='pic_folder/None/no-img.jpg')
