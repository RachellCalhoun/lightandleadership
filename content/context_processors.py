from .models import FooterInfo, Menu, AnalyticTag

def footer(request):
	footer = FooterInfo.objects.all()
	return {'footer': footer}

def navbar(request):
	categories = Menu.objects.all().order_by('order')
	return {'categories': categories}

def global_analytic(request):
	global_tag = AnalyticTag.objects.filter(page=AnalyticTag.GLOBAL).first()
	print(global_tag, 'lalksdjfa;lskd')
	return {'global_tag': global_tag}