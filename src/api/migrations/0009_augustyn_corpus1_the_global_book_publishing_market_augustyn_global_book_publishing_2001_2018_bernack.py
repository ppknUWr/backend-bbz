# Generated by Django 3.2 on 2021-05-21 12:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_auto_20210521_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='nabialczyk_bibliografia_o_iinib_UWr',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_author', models.CharField(default='Bez autora', max_length=512, verbose_name='Autor książki')),
                ('co_authors', models.CharField(default='Bez współtwórcy.', max_length=256, verbose_name='Współtwórca')),
                ('editor', models.CharField(default='Bez redaktora.', max_length=256, verbose_name='Redaktor')),
                ('title', models.TextField(default='Brak Tytułu.', verbose_name='Tytuł')),
                ('subtitle', models.TextField(default='Bez podtytułu', verbose_name='Podtytuł')),
                ('original_edition', models.TextField(default='Bez wydania oryginalnego.', verbose_name='Wydanie oryginalne')),
                ('series', models.TextField(default='Bez numeru serii.', verbose_name='Numer serii')),
                ('publication_date', models.TextField(default='Brak roku wydania.', verbose_name='Rok wydania')),
                ('publication', models.TextField(default='Bez wydania.', verbose_name='Wydanie')),
                ('publication_place', models.TextField(default='Bez miejsca wydania.', verbose_name='Miejsce wydania')),
                ('publisher', models.TextField(default='Bez wydawcy.', verbose_name='Wydawca')),
                ('source', models.TextField(default='Bez źródła.', verbose_name='Źródło')),
                ('number', models.TextField(default='Bez numeru.', verbose_name='Numer')),
                ('notebook', models.TextField(default='Bez zeszytu.', verbose_name='Zeszyt')),
                ('pages', models.TextField(default='0', verbose_name='Ilość stron')),
                ('language', models.TextField(default='Bez języka.', verbose_name='Język')),
                ('isbn_or_issn_number', models.TextField(default='Bez numeru ISBN/ISSN.', verbose_name='Numer ISBN/ISSN')),
                ('doi_number', models.TextField(default='Bez numeru DOI.', verbose_name='Numer DOI')),
                ('link', models.URLField(max_length=1024, verbose_name='Link/Załącznik')),
                ('keywords_and_content', models.TextField(default='Bez słów kluczowych/zawratości.', verbose_name='Słowa kluczowe')),
                ('comments', models.TextField(default='Bez komentarzy.', verbose_name='Komentarze')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Test',
                'db_table': 'nabialczyk_bibliografia_o_iinib_UWr',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='lubocki_bibliografia_przedmiotowa_stefanii_grodzienskiej',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_author', models.CharField(default='Bez autora', max_length=512, verbose_name='Autor książki')),
                ('co_authors', models.CharField(default='Bez współtwórcy.', max_length=256, verbose_name='Współtwórca')),
                ('editor', models.CharField(default='Bez redaktora.', max_length=256, verbose_name='Redaktor')),
                ('title', models.TextField(default='Brak Tytułu.', verbose_name='Tytuł')),
                ('subtitle', models.TextField(default='Bez podtytułu', verbose_name='Podtytuł')),
                ('original_edition', models.TextField(default='Bez wydania oryginalnego.', verbose_name='Wydanie oryginalne')),
                ('series', models.TextField(default='Bez numeru serii.', verbose_name='Numer serii')),
                ('publication_date', models.TextField(default='Brak roku wydania.', verbose_name='Rok wydania')),
                ('publication', models.TextField(default='Bez wydania.', verbose_name='Wydanie')),
                ('publication_place', models.TextField(default='Bez miejsca wydania.', verbose_name='Miejsce wydania')),
                ('publisher', models.TextField(default='Bez wydawcy.', verbose_name='Wydawca')),
                ('source', models.TextField(default='Bez źródła.', verbose_name='Źródło')),
                ('number', models.TextField(default='Bez numeru.', verbose_name='Numer')),
                ('notebook', models.TextField(default='Bez zeszytu.', verbose_name='Zeszyt')),
                ('pages', models.TextField(default='0', verbose_name='Ilość stron')),
                ('language', models.TextField(default='Bez języka.', verbose_name='Język')),
                ('isbn_or_issn_number', models.TextField(default='Bez numeru ISBN/ISSN.', verbose_name='Numer ISBN/ISSN')),
                ('doi_number', models.TextField(default='Bez numeru DOI.', verbose_name='Numer DOI')),
                ('link', models.URLField(max_length=1024, verbose_name='Link/Załącznik')),
                ('keywords_and_content', models.TextField(default='Bez słów kluczowych/zawratości.', verbose_name='Słowa kluczowe')),
                ('comments', models.TextField(default='Bez komentarzy.', verbose_name='Komentarze')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Test',
                'db_table': 'lubocki_bibliografia_przedmiotowa_stefanii_grodzienskiej',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='lubocki_bibliografia_podmiotowa_stefanii_grodzienskiej',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_author', models.CharField(default='Bez autora', max_length=512, verbose_name='Autor książki')),
                ('co_authors', models.CharField(default='Bez współtwórcy.', max_length=256, verbose_name='Współtwórca')),
                ('editor', models.CharField(default='Bez redaktora.', max_length=256, verbose_name='Redaktor')),
                ('title', models.TextField(default='Brak Tytułu.', verbose_name='Tytuł')),
                ('subtitle', models.TextField(default='Bez podtytułu', verbose_name='Podtytuł')),
                ('original_edition', models.TextField(default='Bez wydania oryginalnego.', verbose_name='Wydanie oryginalne')),
                ('series', models.TextField(default='Bez numeru serii.', verbose_name='Numer serii')),
                ('publication_date', models.TextField(default='Brak roku wydania.', verbose_name='Rok wydania')),
                ('publication', models.TextField(default='Bez wydania.', verbose_name='Wydanie')),
                ('publication_place', models.TextField(default='Bez miejsca wydania.', verbose_name='Miejsce wydania')),
                ('publisher', models.TextField(default='Bez wydawcy.', verbose_name='Wydawca')),
                ('source', models.TextField(default='Bez źródła.', verbose_name='Źródło')),
                ('number', models.TextField(default='Bez numeru.', verbose_name='Numer')),
                ('notebook', models.TextField(default='Bez zeszytu.', verbose_name='Zeszyt')),
                ('pages', models.TextField(default='0', verbose_name='Ilość stron')),
                ('language', models.TextField(default='Bez języka.', verbose_name='Język')),
                ('isbn_or_issn_number', models.TextField(default='Bez numeru ISBN/ISSN.', verbose_name='Numer ISBN/ISSN')),
                ('doi_number', models.TextField(default='Bez numeru DOI.', verbose_name='Numer DOI')),
                ('link', models.URLField(max_length=1024, verbose_name='Link/Załącznik')),
                ('keywords_and_content', models.TextField(default='Bez słów kluczowych/zawratości.', verbose_name='Słowa kluczowe')),
                ('comments', models.TextField(default='Bez komentarzy.', verbose_name='Komentarze')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Test',
                'db_table': 'lubocki_bibliografia_podmiotowa_stefanii_grodzienskiej',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='lubocki_Bibliografia_elementarzy_1945_2012_przedmiotowa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_author', models.CharField(default='Bez autora', max_length=512, verbose_name='Autor książki')),
                ('co_authors', models.CharField(default='Bez współtwórcy.', max_length=256, verbose_name='Współtwórca')),
                ('editor', models.CharField(default='Bez redaktora.', max_length=256, verbose_name='Redaktor')),
                ('title', models.TextField(default='Brak Tytułu.', verbose_name='Tytuł')),
                ('subtitle', models.TextField(default='Bez podtytułu', verbose_name='Podtytuł')),
                ('original_edition', models.TextField(default='Bez wydania oryginalnego.', verbose_name='Wydanie oryginalne')),
                ('series', models.TextField(default='Bez numeru serii.', verbose_name='Numer serii')),
                ('publication_date', models.TextField(default='Brak roku wydania.', verbose_name='Rok wydania')),
                ('publication', models.TextField(default='Bez wydania.', verbose_name='Wydanie')),
                ('publication_place', models.TextField(default='Bez miejsca wydania.', verbose_name='Miejsce wydania')),
                ('publisher', models.TextField(default='Bez wydawcy.', verbose_name='Wydawca')),
                ('source', models.TextField(default='Bez źródła.', verbose_name='Źródło')),
                ('number', models.TextField(default='Bez numeru.', verbose_name='Numer')),
                ('notebook', models.TextField(default='Bez zeszytu.', verbose_name='Zeszyt')),
                ('pages', models.TextField(default='0', verbose_name='Ilość stron')),
                ('language', models.TextField(default='Bez języka.', verbose_name='Język')),
                ('isbn_or_issn_number', models.TextField(default='Bez numeru ISBN/ISSN.', verbose_name='Numer ISBN/ISSN')),
                ('doi_number', models.TextField(default='Bez numeru DOI.', verbose_name='Numer DOI')),
                ('link', models.URLField(max_length=1024, verbose_name='Link/Załącznik')),
                ('keywords_and_content', models.TextField(default='Bez słów kluczowych/zawratości.', verbose_name='Słowa kluczowe')),
                ('comments', models.TextField(default='Bez komentarzy.', verbose_name='Komentarze')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Test',
                'db_table': 'lubocki_Bibliografia_elementarzy_1945_2012_przedmiotowa',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='lubocki_bibliografia_elementarzy_1945_2012_podmiotowa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_author', models.CharField(default='Bez autora', max_length=512, verbose_name='Autor książki')),
                ('co_authors', models.CharField(default='Bez współtwórcy.', max_length=256, verbose_name='Współtwórca')),
                ('editor', models.CharField(default='Bez redaktora.', max_length=256, verbose_name='Redaktor')),
                ('title', models.TextField(default='Brak Tytułu.', verbose_name='Tytuł')),
                ('subtitle', models.TextField(default='Bez podtytułu', verbose_name='Podtytuł')),
                ('original_edition', models.TextField(default='Bez wydania oryginalnego.', verbose_name='Wydanie oryginalne')),
                ('series', models.TextField(default='Bez numeru serii.', verbose_name='Numer serii')),
                ('publication_date', models.TextField(default='Brak roku wydania.', verbose_name='Rok wydania')),
                ('publication', models.TextField(default='Bez wydania.', verbose_name='Wydanie')),
                ('publication_place', models.TextField(default='Bez miejsca wydania.', verbose_name='Miejsce wydania')),
                ('publisher', models.TextField(default='Bez wydawcy.', verbose_name='Wydawca')),
                ('source', models.TextField(default='Bez źródła.', verbose_name='Źródło')),
                ('number', models.TextField(default='Bez numeru.', verbose_name='Numer')),
                ('notebook', models.TextField(default='Bez zeszytu.', verbose_name='Zeszyt')),
                ('pages', models.TextField(default='0', verbose_name='Ilość stron')),
                ('language', models.TextField(default='Bez języka.', verbose_name='Język')),
                ('isbn_or_issn_number', models.TextField(default='Bez numeru ISBN/ISSN.', verbose_name='Numer ISBN/ISSN')),
                ('doi_number', models.TextField(default='Bez numeru DOI.', verbose_name='Numer DOI')),
                ('link', models.URLField(max_length=1024, verbose_name='Link/Załącznik')),
                ('keywords_and_content', models.TextField(default='Bez słów kluczowych/zawratości.', verbose_name='Słowa kluczowe')),
                ('comments', models.TextField(default='Bez komentarzy.', verbose_name='Komentarze')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Test',
                'db_table': 'lubocki_bibliografia_elementarzy_1945_2012_podmiotowa',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='hojka_slowniki_dla_dzieci_1989_2015',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_author', models.CharField(default='Bez autora', max_length=512, verbose_name='Autor książki')),
                ('co_authors', models.CharField(default='Bez współtwórcy.', max_length=256, verbose_name='Współtwórca')),
                ('editor', models.CharField(default='Bez redaktora.', max_length=256, verbose_name='Redaktor')),
                ('title', models.TextField(default='Brak Tytułu.', verbose_name='Tytuł')),
                ('subtitle', models.TextField(default='Bez podtytułu', verbose_name='Podtytuł')),
                ('original_edition', models.TextField(default='Bez wydania oryginalnego.', verbose_name='Wydanie oryginalne')),
                ('series', models.TextField(default='Bez numeru serii.', verbose_name='Numer serii')),
                ('publication_date', models.TextField(default='Brak roku wydania.', verbose_name='Rok wydania')),
                ('publication', models.TextField(default='Bez wydania.', verbose_name='Wydanie')),
                ('publication_place', models.TextField(default='Bez miejsca wydania.', verbose_name='Miejsce wydania')),
                ('publisher', models.TextField(default='Bez wydawcy.', verbose_name='Wydawca')),
                ('source', models.TextField(default='Bez źródła.', verbose_name='Źródło')),
                ('number', models.TextField(default='Bez numeru.', verbose_name='Numer')),
                ('notebook', models.TextField(default='Bez zeszytu.', verbose_name='Zeszyt')),
                ('pages', models.TextField(default='0', verbose_name='Ilość stron')),
                ('language', models.TextField(default='Bez języka.', verbose_name='Język')),
                ('isbn_or_issn_number', models.TextField(default='Bez numeru ISBN/ISSN.', verbose_name='Numer ISBN/ISSN')),
                ('doi_number', models.TextField(default='Bez numeru DOI.', verbose_name='Numer DOI')),
                ('link', models.URLField(max_length=1024, verbose_name='Link/Załącznik')),
                ('keywords_and_content', models.TextField(default='Bez słów kluczowych/zawratości.', verbose_name='Słowa kluczowe')),
                ('comments', models.TextField(default='Bez komentarzy.', verbose_name='Komentarze')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Test',
                'db_table': 'hojka_slowniki_dla_dzieci_1989_2015',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='cislo_irlandia',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_author', models.CharField(default='Bez autora', max_length=512, verbose_name='Autor książki')),
                ('co_authors', models.CharField(default='Bez współtwórcy.', max_length=256, verbose_name='Współtwórca')),
                ('editor', models.CharField(default='Bez redaktora.', max_length=256, verbose_name='Redaktor')),
                ('title', models.TextField(default='Brak Tytułu.', verbose_name='Tytuł')),
                ('subtitle', models.TextField(default='Bez podtytułu', verbose_name='Podtytuł')),
                ('original_edition', models.TextField(default='Bez wydania oryginalnego.', verbose_name='Wydanie oryginalne')),
                ('series', models.TextField(default='Bez numeru serii.', verbose_name='Numer serii')),
                ('publication_date', models.TextField(default='Brak roku wydania.', verbose_name='Rok wydania')),
                ('publication', models.TextField(default='Bez wydania.', verbose_name='Wydanie')),
                ('publication_place', models.TextField(default='Bez miejsca wydania.', verbose_name='Miejsce wydania')),
                ('publisher', models.TextField(default='Bez wydawcy.', verbose_name='Wydawca')),
                ('source', models.TextField(default='Bez źródła.', verbose_name='Źródło')),
                ('number', models.TextField(default='Bez numeru.', verbose_name='Numer')),
                ('notebook', models.TextField(default='Bez zeszytu.', verbose_name='Zeszyt')),
                ('pages', models.TextField(default='0', verbose_name='Ilość stron')),
                ('language', models.TextField(default='Bez języka.', verbose_name='Język')),
                ('isbn_or_issn_number', models.TextField(default='Bez numeru ISBN/ISSN.', verbose_name='Numer ISBN/ISSN')),
                ('doi_number', models.TextField(default='Bez numeru DOI.', verbose_name='Numer DOI')),
                ('link', models.URLField(max_length=1024, verbose_name='Link/Załącznik')),
                ('keywords_and_content', models.TextField(default='Bez słów kluczowych/zawratości.', verbose_name='Słowa kluczowe')),
                ('comments', models.TextField(default='Bez komentarzy.', verbose_name='Komentarze')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Test',
                'db_table': 'cislo_irlandia',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='bernacki_miedzywojenna_fantastyka',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_author', models.CharField(default='Bez autora', max_length=512, verbose_name='Autor książki')),
                ('co_authors', models.CharField(default='Bez współtwórcy.', max_length=256, verbose_name='Współtwórca')),
                ('editor', models.CharField(default='Bez redaktora.', max_length=256, verbose_name='Redaktor')),
                ('title', models.TextField(default='Brak Tytułu.', verbose_name='Tytuł')),
                ('subtitle', models.TextField(default='Bez podtytułu', verbose_name='Podtytuł')),
                ('original_edition', models.TextField(default='Bez wydania oryginalnego.', verbose_name='Wydanie oryginalne')),
                ('series', models.TextField(default='Bez numeru serii.', verbose_name='Numer serii')),
                ('publication_date', models.TextField(default='Brak roku wydania.', verbose_name='Rok wydania')),
                ('publication', models.TextField(default='Bez wydania.', verbose_name='Wydanie')),
                ('publication_place', models.TextField(default='Bez miejsca wydania.', verbose_name='Miejsce wydania')),
                ('publisher', models.TextField(default='Bez wydawcy.', verbose_name='Wydawca')),
                ('source', models.TextField(default='Bez źródła.', verbose_name='Źródło')),
                ('number', models.TextField(default='Bez numeru.', verbose_name='Numer')),
                ('notebook', models.TextField(default='Bez zeszytu.', verbose_name='Zeszyt')),
                ('pages', models.TextField(default='0', verbose_name='Ilość stron')),
                ('language', models.TextField(default='Bez języka.', verbose_name='Język')),
                ('isbn_or_issn_number', models.TextField(default='Bez numeru ISBN/ISSN.', verbose_name='Numer ISBN/ISSN')),
                ('doi_number', models.TextField(default='Bez numeru DOI.', verbose_name='Numer DOI')),
                ('link', models.URLField(max_length=1024, verbose_name='Link/Załącznik')),
                ('keywords_and_content', models.TextField(default='Bez słów kluczowych/zawratości.', verbose_name='Słowa kluczowe')),
                ('comments', models.TextField(default='Bez komentarzy.', verbose_name='Komentarze')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Test',
                'db_table': 'bernacki_miedzywojenna_fantastyka',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='augustyn_global_book_publishing_2001_2018',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_author', models.CharField(default='Bez autora', max_length=512, verbose_name='Autor książki')),
                ('co_authors', models.CharField(default='Bez współtwórcy.', max_length=256, verbose_name='Współtwórca')),
                ('editor', models.CharField(default='Bez redaktora.', max_length=256, verbose_name='Redaktor')),
                ('title', models.TextField(default='Brak Tytułu.', verbose_name='Tytuł')),
                ('subtitle', models.TextField(default='Bez podtytułu', verbose_name='Podtytuł')),
                ('original_edition', models.TextField(default='Bez wydania oryginalnego.', verbose_name='Wydanie oryginalne')),
                ('series', models.TextField(default='Bez numeru serii.', verbose_name='Numer serii')),
                ('publication_date', models.TextField(default='Brak roku wydania.', verbose_name='Rok wydania')),
                ('publication', models.TextField(default='Bez wydania.', verbose_name='Wydanie')),
                ('publication_place', models.TextField(default='Bez miejsca wydania.', verbose_name='Miejsce wydania')),
                ('publisher', models.TextField(default='Bez wydawcy.', verbose_name='Wydawca')),
                ('source', models.TextField(default='Bez źródła.', verbose_name='Źródło')),
                ('number', models.TextField(default='Bez numeru.', verbose_name='Numer')),
                ('notebook', models.TextField(default='Bez zeszytu.', verbose_name='Zeszyt')),
                ('pages', models.TextField(default='0', verbose_name='Ilość stron')),
                ('language', models.TextField(default='Bez języka.', verbose_name='Język')),
                ('isbn_or_issn_number', models.TextField(default='Bez numeru ISBN/ISSN.', verbose_name='Numer ISBN/ISSN')),
                ('doi_number', models.TextField(default='Bez numeru DOI.', verbose_name='Numer DOI')),
                ('link', models.URLField(max_length=1024, verbose_name='Link/Załącznik')),
                ('keywords_and_content', models.TextField(default='Bez słów kluczowych/zawratości.', verbose_name='Słowa kluczowe')),
                ('comments', models.TextField(default='Bez komentarzy.', verbose_name='Komentarze')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Test',
                'db_table': 'augustyn_global_book_publishing_2001_2018',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='augustyn_corpus1_the_global_book_publishing_market',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_author', models.CharField(default='Bez autora', max_length=512, verbose_name='Autor książki')),
                ('co_authors', models.CharField(default='Bez współtwórcy.', max_length=256, verbose_name='Współtwórca')),
                ('editor', models.CharField(default='Bez redaktora.', max_length=256, verbose_name='Redaktor')),
                ('title', models.TextField(default='Brak Tytułu.', verbose_name='Tytuł')),
                ('subtitle', models.TextField(default='Bez podtytułu', verbose_name='Podtytuł')),
                ('original_edition', models.TextField(default='Bez wydania oryginalnego.', verbose_name='Wydanie oryginalne')),
                ('series', models.TextField(default='Bez numeru serii.', verbose_name='Numer serii')),
                ('publication_date', models.TextField(default='Brak roku wydania.', verbose_name='Rok wydania')),
                ('publication', models.TextField(default='Bez wydania.', verbose_name='Wydanie')),
                ('publication_place', models.TextField(default='Bez miejsca wydania.', verbose_name='Miejsce wydania')),
                ('publisher', models.TextField(default='Bez wydawcy.', verbose_name='Wydawca')),
                ('source', models.TextField(default='Bez źródła.', verbose_name='Źródło')),
                ('number', models.TextField(default='Bez numeru.', verbose_name='Numer')),
                ('notebook', models.TextField(default='Bez zeszytu.', verbose_name='Zeszyt')),
                ('pages', models.TextField(default='0', verbose_name='Ilość stron')),
                ('language', models.TextField(default='Bez języka.', verbose_name='Język')),
                ('isbn_or_issn_number', models.TextField(default='Bez numeru ISBN/ISSN.', verbose_name='Numer ISBN/ISSN')),
                ('doi_number', models.TextField(default='Bez numeru DOI.', verbose_name='Numer DOI')),
                ('link', models.URLField(max_length=1024, verbose_name='Link/Załącznik')),
                ('keywords_and_content', models.TextField(default='Bez słów kluczowych/zawratości.', verbose_name='Słowa kluczowe')),
                ('comments', models.TextField(default='Bez komentarzy.', verbose_name='Komentarze')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Test',
                'db_table': 'augustyn_corpus1_the_global_book_publishing_market',
                'abstract': False,
            },
        ),
    ]
