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
