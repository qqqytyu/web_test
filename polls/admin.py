from django.contrib import admin

from .models import Question , Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')

# fieldsets中的元组顺序，表示了表单上的显示顺序
# fieldsets中每个元组的第一个元素是字段集的标题 , 你可以任意地为每个字段集指定HTML样式类(classes)
# 这告诉Django：Choice对象在Question的管理界面中编辑。默认提供足够3个Choice的空间。
# 默认地，Django显示每个对象的str()返回的内容。但有时如果我们能显示个别的字段将很有帮助。
# 我们使用#list_display 选项来实现这个功能，它是一个要显示的字段名称的元组，在对象的变更列表页面上作为列显示

admin.site.register(Question, QuestionAdmin)
# Register your models here.
