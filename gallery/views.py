from datetime import date
from django.shortcuts import render
from django.http import Http404

from .models import Gallery, News, Event, Issue


def home(request):
    issues = Issue.objects.all().order_by('-created_at')[:5]
    gallery_pics = Gallery.objects.order_by('-uploaded_at')[:20]
    latest_news = News.objects.order_by('-published_at')[:5]
    upcoming_events = Event.objects.filter(date__gte=date.today()).order_by('date')[:5]

    context = {
        'gallery_pics': gallery_pics,
        'latest_news': latest_news,
        'issues': issues,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'index.html', context)


def news(request):
    news_articles = News.objects.order_by('-published_at')[:5]
    return render(request, 'news.html', {'news_articles': news_articles})


def event(request):
    upcoming_events = Event.objects.filter(date__gte=date.today()).order_by('date')
    return render(request, 'events.html', {'upcoming_events': upcoming_events})


def issue(request, issue_id):
    try:
        issue = Issue.objects.get(id=issue_id)
    except Issue.DoesNotExist:
        raise Http404("Issue not found")

    context = {'issue': issue}
    return render(request, 'issue_detail.html', context)
