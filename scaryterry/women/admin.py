from django.contrib import admin
from django.core.checks import messages
from .models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title='статус женжин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'cat', 'husband', 'tags')
    filter_horizontal = ['tags']  # виджет для работы с тегами
    # filter_vertical = ['tags']
    # exclude = ('is_published', 'tags') # исключает поля
    # readonly_fields = ('slug', )  # поля только для чтения
    prepopulated_fields = {'slug': ('title', )}  # для авто создания слага
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title', )
    ordering = ('time_create', 'title')
    list_editable = ("is_published", )
    list_per_page = 5
    actions = ('set_published',  'set_draft')
    search_fields = ('title__startswith', 'cat__name')
    list_filter = (MarriedFilter, 'cat__name', 'is_published')

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)} символов'

    @admin.action(description='Опубликовать запись')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей')

    @admin.action(description='Снять с публикации запись')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'{count} записей снять с публикации', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
#admin.site.register(Women, WomenAdmin)
