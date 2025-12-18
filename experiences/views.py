from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import InquiryForm
from .models import PortfolioItem, Service, TeamMember


def home(request):
	"""Render the studio showcase landing page."""
	portfolio_items = PortfolioItem.objects.prefetch_related('gallery_images')
	services = Service.objects.all()
	featured_portfolio = portfolio_items.filter(featured=True).first() or portfolio_items.first()
	work_preview = portfolio_items[:4]

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
			"services": services,
			"work_preview": work_preview,
			"featured_portfolio": featured_portfolio,
			"inquiry_form": inquiry_form,
		},
	)


def portfolio_list(request):
	"""Display the full archive of studio work."""
	items = PortfolioItem.objects.prefetch_related('gallery_images')
	return render(request, "experiences/portfolio_list.html", {"items": items})


def portfolio_detail(request, slug):
	"""Display a focused view of a single portfolio piece."""
	item = get_object_or_404(PortfolioItem.objects.prefetch_related('gallery_images'), slug=slug)

	return render(
		request,
		"experiences/portfolio_detail.html",
		{
			"item": item,
		},
	)


def team(request):
	members = TeamMember.objects.all()
	return render(request, "experiences/team.html", {"team_members": members})


def yalda_hafez_faal(request):
	"""Render the archived Yalda CBC Hafez Faal experience."""
	return render(request, "projects/yalda_hafez_faal.html")


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
