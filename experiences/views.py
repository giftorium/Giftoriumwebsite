from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import InquiryForm
from .models import PortfolioItem, Project, Service, TeamMember, Testimonial


def home(request):
	"""Render the studio showcase landing page."""
	projects = Project.objects.all()
	services = Service.objects.all()
	testimonials = Testimonial.objects.all()
	portfolio_items = PortfolioItem.objects.prefetch_related('gallery_images').all()
	featured_portfolio = portfolio_items.filter(featured=True).first() or portfolio_items.first()

	if request.method == "POST":
		inquiry_form = InquiryForm(request.POST)
		if inquiry_form.is_valid():
			inquiry = inquiry_form.save()
			_notify_team_of_inquiry(inquiry)
			messages.success(request, "Thanks for reaching out — we’ll reply within 48 hours.")
			return redirect(f"{reverse('experiences:home')}#contact")
	else:
		inquiry_form = InquiryForm()

	return render(
		request,
		"experiences/home.html",
		{
			"projects": projects,
			"services": services,
			"testimonials": testimonials,
			"portfolio": portfolio_items,
			"featured_portfolio": featured_portfolio,
			"inquiry_form": inquiry_form,
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


def team(request):
	members = TeamMember.objects.all()
	return render(request, "experiences/team.html", {"team_members": members})


def _notify_team_of_inquiry(inquiry):
	if not settings.INQUIRY_RECIPIENTS:
		return
	subject = f"New Giftorium inquiry from {inquiry.name}"
	body_lines = [
		f"Name: {inquiry.name}",
		f"Email: {inquiry.email}",
		f"Company: {inquiry.company or '—'}",
		f"Timeline: {inquiry.timeline or '—'}",
		f"Referrer: {inquiry.referrer or '—'}",
		"",
		"Message:",
		inquiry.message,
	]
	try:
		send_mail(
			subject,
			"\n".join(body_lines),
			settings.DEFAULT_FROM_EMAIL,
			settings.INQUIRY_RECIPIENTS,
		)
	except Exception:
		# Fail silently but keep the inquiry stored in the admin
		pass
