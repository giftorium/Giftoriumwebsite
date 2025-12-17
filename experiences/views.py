from django.http import Http404
from django.shortcuts import render


PORTFOLIO_ITEMS = [
	{
		"slug": "chromatic-reverie",
		"title": "Chromatic Reverie",
		"medium": "Sensorial atrium takeover",
		"description": "Layered light columns, kinetic drapery, and bespoke soundscapes for a three-night museum residency.",
		"image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80",
		"location": "New Museum, NYC",
		"year": "2025",
		"scope": [
			"Spatial concepting",
			"Lighting direction",
			"Multisensory score",
		],
		"outcome": "Immersed 6k guests across three evenings, extending visitation hours and driving 40% more merch sales for the gift store.",
		"gallery": [
			"https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=1800&q=80",
			"https://images.unsplash.com/photo-1500534310680-164391d4bb2f?auto=format&fit=crop&w=1800&q=80",
		],
	},
	{
		"slug": "nebula-listening-lounge",
		"title": "Nebula Listening Lounge",
		"medium": "Immersive pop-up bar",
		"description": "Analog hi-fi ritual featuring holographic hosts, reactive resin furniture, and custom scent moments.",
		"image": "https://images.unsplash.com/photo-1489515217757-5fd1be406fef?auto=format&fit=crop&w=1200&q=80",
		"location": "Los Angeles Arts District",
		"year": "2024",
		"scope": [
			"Experience strategy",
			"Interactive tech prototyping",
			"On-site show direction",
		],
		"outcome": "A sold-out nine-night run with a 92% repeat guest rate thanks to rotating sonic chapters.",
		"gallery": [
			"https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&w=1800&q=80",
			"https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=1800&q=80",
		],
	},
	{
		"slug": "tidepool-pavilion",
		"title": "Tidepool Pavilion",
		"medium": "Outdoor cultural pavilion",
		"description": "Reflective pools, responsive LEDs, and tactile textiles choreographed with live performance.",
		"image": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=1200&q=80",
		"location": "Dubai Design Week",
		"year": "2023",
		"scope": [
			"Environmental storytelling",
			"Partner management",
			"Technical direction",
		],
		"outcome": "Extended dwell time by 3x for festival visitors and secured new patron funding for the pavilion tour.",
		"gallery": [
			"https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1800&q=80",
			"https://images.unsplash.com/photo-1500534620840-430dde0d4a95?auto=format&fit=crop&w=1800&q=80",
		],
	},
]


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

	projects = [
		{
			"title": "Solstice Convergence",
			"location": "Brooklyn Navy Yard",
			"summary": "Interactive projection ritual fusing poetry, scent, and motion tracking.",
		},
		{
			"title": "Desert Bloom Pavilion",
			"location": "Dubai Design Week",
			"summary": "Modular oasis lounge with responsive light columns and tactile textiles.",
		},
		{
			"title": "Orbit Social Club",
			"location": "Los Angeles Arts District",
			"summary": "Pop-up listening bar featuring holographic storytellers and analog hi-fi."
		},
	]

	services = [
		"Experience strategy & narrative",
		"Spatial concepting + set design",
		"Interactive technology prototyping",
		"On-site production leadership",
	]

	testimonials = [
		{
			"quote": "They transformed our event into a living story. Guests are still talking about it.",
			"author": "Nadia Rahimi • Program Director, Aurora Forum",
		},
		{
			"quote": "Meticulous craft plus fearless experimentation—exactly what we needed.",
			"author": "Leo Martinez • Creative Lead, Lumen Labs",
		},
	]

	return render(
		request,
		"experiences/home.html",
		{
			"studio_profile": studio_profile,
			"projects": projects,
			"services": services,
			"testimonials": testimonials,
			"portfolio": PORTFOLIO_ITEMS,
			"featured_portfolio": PORTFOLIO_ITEMS[0],
		},
	)


def portfolio_detail(request, slug):
	"""Display a focused view of a single portfolio piece."""
	item = next((entry for entry in PORTFOLIO_ITEMS if entry["slug"] == slug), None)
	if item is None:
		raise Http404("Portfolio piece not found.")

	return render(
		request,
		"experiences/portfolio_detail.html",
		{
			"item": item,
			"other_items": [entry for entry in PORTFOLIO_ITEMS if entry["slug"] != slug],
		},
	)
