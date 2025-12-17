from django.contrib import admin

from .models import (
	Inquiry,
	PortfolioImage,
	PortfolioItem,
	Project,
	Service,
	StudioSettings,
	TeamMember,
	Testimonial,
)


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


@admin.register(StudioSettings)
class StudioSettingsAdmin(admin.ModelAdmin):
	list_display = ('studio_name', 'updated_at')
	readonly_fields = ('updated_at',)

	def has_add_permission(self, request):
		if StudioSettings.objects.count() >= 1:
			return False
		return super().has_add_permission(request)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'role', 'order')
	list_editable = ('order',)
	search_fields = ('name', 'role')


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'company', 'created_at', 'processed')
	list_filter = ('processed', 'created_at')
	search_fields = ('name', 'email', 'company', 'message')
	readonly_fields = ('created_at', 'updated_at')
	actions = ['mark_processed']

	def mark_processed(self, request, queryset):
		queryset.update(processed=True)
		self.message_user(request, f"Marked {queryset.count()} inquiries as processed.")

	mark_processed.short_description = "Mark selected inquiries as processed"
