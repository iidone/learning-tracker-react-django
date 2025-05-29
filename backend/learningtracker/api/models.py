from django.db import models

class Users(models.Model):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пользователь: {self.username}'
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'