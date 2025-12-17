from django.shortcuts import get_object_or_404, render

from .models import PortfolioItem, Project, Service, Testimonial


def home(request):
	"""Render the studio showcase landing page with placeholder content."""
	studio_profile = {
		"tagline": "Immersive environments for bold cultural moments",
		"intro": (
			"Giftorium collaborates with museums, brands, and cultural leaders "
			"to craft sensorial experiences that guests remember well after the lights dim."
		),
		"cta_label": "Start a collaboration",
	}

	projects = Project.objects.all()
	services = Service.objects.all()
	testimonials = Testimonial.objects.all()
	portfolio_items = PortfolioItem.objects.prefetch_related('gallery_images').all()
	featured_portfolio = portfolio_items.filter(featured=True).first() or portfolio_items.first()

	return render(
		request,
		"experiences/home.html",
		{
			"studio_profile": studio_profile,
			"projects": projects,
			"services": services,
			"testimonials": testimonials,
			"portfolio": portfolio_items,
			"featured_portfolio": featured_portfolio,
		},
	)


def portfolio_detail(request, slug):
	"""Display a focused view of a single portfolio piece."""
	item = get_object_or_404(PortfolioItem.objects.prefetch_related('gallery_images'), slug=slug)
	other_items = PortfolioItem.objects.exclude(slug=slug)

	return render(
		request,
		"experiences/portfolio_detail.html",
		{
			"item": item,
			"other_items": other_items,
		},
	)
