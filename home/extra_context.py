from dynamic.models import Pages


def extra_context_data(request):
    pages = Pages.objects.all()
    context_data = dict(
        pages_url = pages
    )
    return context_data