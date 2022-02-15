(venv) PS C:\Users\s-mil\PycharmProjects\NewsPortal\newspaper> python manage.py shell
>>> from django.contrib.auth.models import User
>>> from newspage.models import Author, Category, Postcategory, Post, Comment
>>> import random

>>> peter_user = User.objects.create_user(username = 'ivanov', last_name = 'peter', email = 'ivanovp@mail.ru', password = 'ivanovpeter')
>>> pavel_user = User.objects.create_user(username = 'sidorov', last_name = 'pavel', email = 'sidorovp@mail.ru')

>>> peter = Author.objects.create(user = peter_user)
>>> pavel = Author.objects.create(user = pavel_user)

>>> cat_world = Category.objects.create(name_category = "В мире")
>>> cat_weather = Category.objects.create(name_category = "Погода")
>>> cat_local = Category.objects.create(name_category = "Местные новости")
>>> cat_breaking = Category.objects.create(name_category = "Экстренные новости")
>>> cat_life = Category.objects.create(name_category = "Жизнь")

>>> first_article_peter = """Съешь ещё этих мягких французских булок, да выпей же чаю. Съешь ещё этих мягких французских булок, да выпей же чаю. Съешь ещё этих мягких французских булок, да выпей же чаю."""
>>> post_a_peter = Post.objects.create(author = peter, type_post = Post.article, title = "Первая статья", text = first_article_peter)
>>> first_article_pavel = """Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства. Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства. Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства."""
>>> post_a_pavel = Post.objects.create(author = pavel, type_post = Post.article, title = "Первая статья Павла", text = first_article_pavel)
>>> first_news_pavel = """Завтра в Москве будет солнечно, без осадков. Скорость ветра от 1 метра в секунду до пяти. Восход солнца в пять часов, пять минут, а заход в девятнадцать часов, пятьдесят две минуты. Ночью минус два, утром плюс девять. Днём влажность сорок три процента, плюс девять градусов. Вечером ясно, влажность шестьдесят процентов."""
>>> post_n_pavel = Post.objects.create(author = pavel, type_post = Post.news, title = "О погоде сегодня", text = first_news_pavel)
>>> second_article_peter = """Новость – текст, посвященный какому-либо событию, выходящему за рамки естественного хода жизни. Актуальная для людей информация, важная для принятия решений. Новость – текст, посвященный какому-либо событию, выходящему за рамки естественного хода жизни. Актуальная для людей информация, важная для принятия решений. Новость – текст, посвященный какому-либо событию, выходящему за рамки естественного хода жизни. Актуальная для людей информация, важная для принятия pешении."""
>>> post2_a_peter = Post.objects.create(author = peter, type_post = Post.article, title = "Вторая статья", text = second_article_peter)

>>> Postcategory.objects.create(post = post_a_peter, name_category = cat_local)
>>> Postcategory.objects.create(post = post_a_pavel, name_category = cat_local)
>>> Postcategory.objects.create(post = post_n_pavel, name_category = cat_breaking)
>>> Postcategory.objects.create(post = post_n_pavel, name_category = cat_weather)
>>> Postcategory.objects.create(post = post2_a_peter, name_category = cat_life)

>>> comment1 = Comment.objects.create(post = post_a_peter, author_comment = pavel.user, text ="Спасибо за информацию.")
>>> comment2 = Comment.objects.create(post = post_a_pavel, author_comment = peter.user, text ="Наконец-то.")
>>> comment3 = Comment.objects.create(post = post_n_pavel, author_comment = peter.user, text ="Мы будем готовы.")
>>> comment4 = Comment.objects.create(post = post2_a_peter, author_comment = pavel.user, text ="Познавательно.")



list_for_like = [post_a_peter,
                    post_a_pavel,
                    post_n_pavel,
                    post2_a_peter,
                    comment1,
                    comment2,
                    comment3,
                    comment4]
for i in range(100):
        random_obj = random.choice(list_for_like)
        if i % 2:
            random_obj.like()
        else:
            random_obj.dislike()





rating_peter = (sum([post.rating * 3 for post in Post.objects.filter(author=peter)]) + sum([comment.rating for comment in Comment.objects.filter(author_comment=peter.user)]) + sum([comment.rating for comment in Comment.objects.filter(post__author=peter)]))
peter.update_rating(rating_peter)

rating_pavel = (sum([post.rating * 3 for post in Post.objects.filter(author=pavel)]) + sum([comment.rating for comment in Comment.objects.filter(author_comment=pavel.user)]) + sum([comment.rating for comment in Comment.objects.filter(post__author=pavel)]))
pavel.update_rating(rating_pavel)



best_author = Author.objects.all().order_by('-rating')[0]
print("username:", best_author.user.username)
print("Рейтинг:", best_author.rating)

best_article = Post.objects.filter(type_post=Post.article).order_by('-rating')[0]
print("Дата:", best_article.time_write)
print("Автор:", best_article.author.user.username)
print("Рейтинг:", best_article.rating)
print("Заголовок:", best_article.title)
print("Превью:", best_article.preview())

comment_best_article = Comment.objects.filter(post=best_article)
print("Комментарии к лучшей статье")
for comment_best_article in Comment.objects.filter(post=best_article):
    print("Дата:", comment_best_article.time_write)
    print("Автор:", comment_best_article.author_comment)
    print("Рейтинг:", comment_best_article.rating)
    print("Комментарий:", comment_best_article.text)