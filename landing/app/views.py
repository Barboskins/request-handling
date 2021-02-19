from collections import Counter

from django.shortcuts import render, reverse

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    par = request.GET.get('from-landing')
    if par == 'original':
        counter_click[par] += 1
        print(counter_click[par])
    elif par == 'test':
        counter_click[par] += 1
        print(counter_click[par])
    else:
        None
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    return render(request, 'index.html')


def landing(request):
    param = request.GET.get('ab-test-arg')
    if param == 'original':
        page_html = 'landing.html'
        counter_show[param] += 1
        print(counter_show[param])
    elif param == 'test':
        page_html = 'landing_alternate.html'
        counter_show[param] += 1
        print(counter_show[param])
    else:
        page_html = 'index.html'
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    return render(request, page_html)


def stats(request):
    res_o = counter_click['original']/counter_show['original']
    res_t = counter_click['test']/counter_show['test']

    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    return render(request, 'stats.html', context={
        'test_conversion': res_o,
        'original_conversion': res_t,
    })
