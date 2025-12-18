from django.db import models


class TimestampedModel(models.Model):
	"""Abstract base that tracks creation/update timestamps."""
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class PortfolioItem(TimestampedModel):
	title = models.CharField(max_length=150)
	slug = models.SlugField(unique=True)
	medium = models.CharField(max_length=120)
	description = models.TextField()
	location = models.CharField(max_length=120, blank=True)
	year = models.CharField(max_length=10, blank=True)
	hero_image = models.ImageField(upload_to='portfolio/hero/')
	grid_image = models.ImageField(upload_to='portfolio/grid/', blank=True)
	outcome = models.TextField(blank=True)
	featured = models.BooleanField(default=False)

	class Meta:
		ordering = ['-featured', '-created_at']

	def __str__(self) -> str:
		return self.title


class PortfolioImage(models.Model):
	item = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ImageField(upload_to='portfolio/gallery/')
	alt_text = models.CharField(max_length=160, blank=True)
	order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['order', 'id']

	def __str__(self) -> str:
		return f"{self.item.title} · frame {self.pk}"


class Project(TimestampedModel):
	title = models.CharField(max_length=150)
	location = models.CharField(max_length=120)
	summary = models.TextField()
	order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['order', 'title']

	def __str__(self) -> str:
		return self.title


class Service(TimestampedModel):
	name = models.CharField(max_length=160)
	order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['order', 'name']

	def __str__(self) -> str:
		return self.name


class Testimonial(TimestampedModel):
	quote = models.TextField()
	author = models.CharField(max_length=160)
	order = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['order', '-created_at']

	def __str__(self) -> str:
		return f"{self.author} testimonial"


class StudioSettings(models.Model):
	studio_name = models.CharField(max_length=120, default="Giftorium")
	eyebrow = models.CharField(max_length=120, default="Portfolio First")
	tagline = models.CharField(max_length=200, default="Immersive environments for bold cultural moments")
	intro = models.TextField(
		default=(
			"Giftorium collaborates with museums, brands, and cultural leaders to craft sensorial experiences "
			"that guests remember well after the lights dim."
		)
	)
	hero_note = models.CharField(
		max_length=200,
		blank=True,
		default="Each commission is built as a cinematic atmosphere. Scroll to explore.",
	)
	cta_label = models.CharField(max_length=80, default="Start a collaboration")
	logo = models.ImageField(upload_to='brand/', blank=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Studio settings"
		verbose_name_plural = "Studio settings"

	def __str__(self) -> str:
		return self.studio_name


class TeamMember(TimestampedModel):
	name = models.CharField(max_length=120)
	role = models.CharField(max_length=160)
	bio = models.TextField()
	headshot = models.ImageField(upload_to='team/', blank=True)
	order = models.PositiveIntegerField(default=0)
	social_link = models.URLField(blank=True)

	class Meta:
		ordering = ['order', 'name']

	def __str__(self) -> str:
		return self.name


class Inquiry(TimestampedModel):
	name = models.CharField(max_length=120)
	email = models.EmailField()
	company = models.CharField(max_length=160, blank=True)
	timeline = models.CharField(max_length=120, blank=True)
	message = models.TextField()
	referrer = models.CharField(max_length=160, blank=True)
	processed = models.BooleanField(default=False)

	class Meta:
		ordering = ['-created_at']

	def __str__(self) -> str:
		return f"Inquiry from {self.name}"
