from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False) and form.cleaned_data.get('is_main', False):
                count += 1
        if count > 1:
            raise ValidationError('Слишком много главных тегов')

        if count == 0:
            raise ValidationError('Нет главного тега')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [id, 'title', 'text', 'published_at', 'image', ]
    list_filter = ['title', 'published_at', ]
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
