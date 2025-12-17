from django.contrib import admin

from .models import PortfolioImage, PortfolioItem, Project, Service, Testimonial


class PortfolioImageInline(admin.TabularInline):
	model = PortfolioImage
	extra = 1


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
	list_display = ('title', 'medium', 'featured', 'created_at')
	list_filter = ('featured',)
	prepopulated_fields = {"slug": ("title",)}
	inlines = [PortfolioImageInline]
	search_fields = ('title', 'medium', 'location')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'location', 'order')
	list_editable = ('order',)
	search_fields = ('title', 'location')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('name', 'order')
	list_editable = ('order',)
	search_fields = ('name',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('author', 'order', 'created_at')
	list_editable = ('order',)
	search_fields = ('author', 'quote')
