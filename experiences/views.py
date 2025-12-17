from django.shortcuts import render


def home(request):
	"""Render the studio showcase landing page with placeholder content."""
	studio_profile = {
		"tagline": "Immersive environments for bold cultural moments",
		"intro": (
			"Giftorium Studio collaborates with museums, brands, and cultural leaders "
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
		},
	)
