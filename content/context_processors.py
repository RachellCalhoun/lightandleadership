from .models import FooterInfo, Menu, AnalyticTag

def navbar(request):
	if 'es/' in request.get_full_path():
		english = False
	else:
		english = True
	categories = Menu.objects.all().order_by('order')
	footer = FooterInfo.objects.all()
	return {'categories': categories, 'english': english, 'footer': footer}

def global_analytic(request):
	analytic_tags = AnalyticTag.objects.all()
	return {'analytic_tags': analytic_tags}
