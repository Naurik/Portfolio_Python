from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from .forms import CommentForm
from django.template.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth


# Create your views here.

# def basic_one(request):
#     view = "basic_one"
#     html = "<html><body>This is %s view</html></body>" % view
#     return HttpResponse(html)

# def template_two(request):
#     view = "template_two"
#     t = get_template('myview.html')
#     html = t.render(Context({'name': view}))
#     return HttpResponse(html)
#
# def template_three_simple(request):
#     view = "template_three"
#     return render(request,'myview.html', {'name': view})

def articles(request):
    all_articles = Article.objects.all()
    return render(request, 'article/articles.html', {'articles': all_articles, 'username': auth.get_user(request).username})

def article(request, article_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render(request, 'article/article.html', args)


def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/comment/get/%s' % article_id)



