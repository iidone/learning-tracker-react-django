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

class Ideas(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    theme = models.CharField(max_length=255)
    description = models.TextField(max_length=2500)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Идея: {self.title}'
    
    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'

