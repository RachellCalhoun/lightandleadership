from .models import FooterInfo, Menu

def footer(request):
    footer = FooterInfo.objects.all()
    return {'footer': footer}


def spanish_navbar(request):
    if 'es/' in request.get_full_path():
        english = False
    else:
        english = True
    categories = Menu.objects.all().order_by('order')
    return {'spanish_categories': categories, 'english': english}
