from django.contrib import admin
from .models import User, Question, Answer

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'created_at',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'display_user', 'text', 'created_at', 'display_likes',)

    def display_likes(self, obj):
        return obj.likes.count()

    display_likes.short_description = 'Likes'

    def display_user(self, obj):
        return obj.user.username

    display_user.short_description = 'User'

admin.site.register(Answer, AnswerAdmin)

    

admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
