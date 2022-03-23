from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200) # CharField — блок данных, состоящий из символов, то есть текст

    # задается максимальная длина max_length, равная 200 символам; этого должно быть достаточно для хранения большинства имен тем.

    date_added = models.DateTimeField(auto_now_add=True) # DateTimeField — блок данных для хранения даты и времени

    # auto_add_now=True приказывает Django автоматически присвоить этому атрибуту текущую дату и время каждый раз, когда пользователь создает новую тему.

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text

class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # Аргумент on_delete=models.CASCADE сообщает Django, что при удалении темы 
    # все записи, связанные с этой темой, также должны быть удалены (это называется 
    # каскадным удалением).

    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"{self.text[:50]}..."
