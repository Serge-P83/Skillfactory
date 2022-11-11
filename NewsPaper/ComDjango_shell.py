from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

import random


def todo():
    User.objects.all().delete()
    Category.objects.all().delete()

    jack_user = User.objects.create_user(username='jack', email='jack@mail.ru', password='jack_password')
    mary_user = User.objects.create_user(username='mary', email='mary@mail.ru', password='mary_password')

    jack = Author.objects.create(user=jack_user)
    mary = Author.objects.create(user=mary_user)

    cat_weather = Category.objects.create(name="Погода")
    cat_books = Category.objects.create(name="Книги")
    cat_movies = Category.objects.create(name="Кино")
    cat_food = Category.objects.create(name="Еда")

    text_article_weather_movies = """статья_погода_кино_Джек__статья_погода_кино_Джек__статья_погода_кино_Джек_
                                   _статья_погода_кино_Джек__статья_погода_кино_Джек__"""

    text_article_books = """статья_книги_Мэри__статья_книги_Мэри__статья_книги_Мэри_
                            _статья_книги_Мэри__статья_книги_Мэри__"""

    text_news_food = """новость_Еда_Мэри__новость_Еда_Мэри__новость_Еда_Мэри__новость_Еда_Мэри__
                    новость_Еда_Мэри__новость_Еда_Мэри__новость_Еда_Мэри__новость_Еда_Мэри__"""

    article_jack = Post.objects.create(author=jack, post_type=Post.article, title="статья_погода_кино_Джек",
                                       text=text_article_weather_movies)
    article_mary = Post.objects.create(author=mary, post_type=Post.article, title="статья_книги_Мэри",
                                       text=text_article_books)
    news_mary = Post.objects.create(author=mary, post_type=Post.news, title="новость_Еда_Мэри", text=text_news_food)

    PostCategory.objects.create(post=article_jack, category=cat_weather)
    PostCategory.objects.create(post=article_jack, category=cat_movies)
    PostCategory.objects.create(post=article_mary, category=cat_books)
    PostCategory.objects.create(post=news_mary, category=cat_food)

    comment1 = Comment.objects.create(post=article_jack, user=mary.user, text="комментарий №1 Мэри к статье Джека")
    comment2 = Comment.objects.create(post=article_mary, user=jack.user, text="комментарий №2 Джека к статье Мэри")
    comment3 = Comment.objects.create(post=news_mary, user=mary.user, text="комментарий №3 Мэри к новости Мэри")
    comment4 = Comment.objects.create(post=news_mary, user=jack.user, text="комментарий №4 Джека к новости Мэри")

    list_for_like = [article_jack,
                     article_mary,
                     news_mary,
                     comment1,
                     comment2,
                     comment3,
                     comment4]

    for i in range(50):
        random_obj = random.choice(list_for_like)
        if i % 2:
            random_obj.like()
        else:
            random_obj.dislike()

    rating_jack = (sum([post.rating * 3 for post in Post.objects.filter(author=jack)])
                   + sum([comment.rating for comment in Comment.objects.filter(user=jack.user)])
                   + sum([comment.rating for comment in Comment.objects.filter(post__author=jack)]))
    jack.update_rating(rating_jack)

    rating_mary = (sum([post.rating * 3 for post in Post.objects.filter(author=mary)])
                   + sum([comment.rating for comment in Comment.objects.filter(user=mary.user)])
                   + sum([comment.rating for comment in Comment.objects.filter(post__author=mary)]))
    mary.update_rating(rating_mary)

    best_author = Author.objects.all().order_by('-rating')[0]

    print("Лучший автор")
    print("username:", best_author.user.username)
    print("Рейтинг:", best_author.rating)
    print("")

    best_article = Post.objects.filter(post_type=Post.article).order_by('-rating')[0]
    print("Лучшая статья")
    print("Дата:", best_article.created)
    print("Автор:", best_article.author.user.username)
    print("Рейтинг:", best_article.rating)
    print("Заголовок:", best_article.title)
    print("Превью:", best_article.preview())
    print("")

    print("Комментарии к ней")
    for comment in Comment.objects.filter(post=best_article):
        print("Дата:", comment.created)
        print("Автор:", comment.user.username)
        print("Рейтинг:", comment.rating)
        print("Комментарий:", comment.text)
        print("")
