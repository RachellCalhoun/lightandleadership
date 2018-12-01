from .models import FooterInfo, Menu, AnalyticTag

def footer(request):
	footer = FooterInfo.objects.all()
	return {'footer': footer}

def navbar(request):
	categories = Menu.objects.all().order_by('order')
	return {'categories': categories}

def global_analytic(request):
	analytic_tags = AnalyticTag.objects.all()
	return {'analytic_tags': analytic_tags}
