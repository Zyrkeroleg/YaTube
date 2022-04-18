from datetime import date


def year(request):
    return {
        'year': date.today().year
    }
