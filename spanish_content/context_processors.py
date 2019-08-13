from .models import FooterInfo, Menu


def spanish_navbar(request):
    if 'es/' in request.get_full_path():
        english = False
    else:
        english = True
    categories = Menu.objects.all().order_by('order')
    footer = FooterInfo.objects.all()
    return {'spanish_categories': categories, 'english': english, 'spanish_footer': footer}
