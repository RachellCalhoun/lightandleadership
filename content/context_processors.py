from .models import FooterInfo, Menu, AnalyticTag

def footer(request):
	footer = FooterInfo.objects.all()
	return {'footer': footer}

def navbar(request):
	if 'es/' in request.get_full_path():
		english = False
	else:
		english = True
	categories = Menu.objects.all().order_by('order')
	return {'categories': categories, 'english': english}

def global_analytic(request):
	analytic_tags = AnalyticTag.objects.all()
	return {'analytic_tags': analytic_tags}
