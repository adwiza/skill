import peewee
import datetime

# Создаем новую БД, для подключения используем SQLite

database = peewee.SqliteDatabase('python_snippets/external_data/music.db')


class BaseTable(peewee.Model):
    # В подклассе Meta указываем подключение к той или иной БД
    class Meta:
        database = database


# Чтобы создать таблицу в нашей БД, нам нужно создать класс
class Artist(BaseTable):
    name = peewee.CharField()  # От типа столбца зависит тип данный, которые мы можем в него записать


class Album(BaseTable):
    artist = peewee.ForeignKeyField(Artist)
    title = peewee.CharField()
    release_date = peewee.DateTimeField()
    publisher = peewee.CharField()
    media_type = peewee.CharField()


# Создание таблиц
database.create_tables([Artist, Album])

# Запись данных в таблицы:
# Первый способ с явным save()
new_artist = Artist(name="Newsboys")
new_artist.save()
# # Второй способ без явного save()
# album_one = Album.create(artist=new_artist,
#                          title="Read All About It",
#                          release_date=datetime.date(1988, 12, 1),
#                          publisher="Refuge",
#                          media_type="CD")

# Запись нескольких объектов
albums = [
    {
         "artist": new_artist,
         "title": "Hell is for Wimps",
         "release_date": datetime.date(1990, 7, 31),
         "publisher": "Sparrow",
         "media_type": "CD"
    },
    {
         "artist": new_artist,
         "title": "Love Liberty Disco",
         "release_date": datetime.date(1990, 7, 31),
         "publisher": "Sparrow",
         "media_type": "CD"
    },
    {
         "artist": new_artist,
         "title": "Thrive",
         "release_date": datetime.date(2002, 3, 26),
         "publisher": "Sparrow",
         "media_type": "CD"
    }]
# Один из способов
albums_in_db = Album.insert_many(albums).execute()
# Второй
bands = ["MXPX", "Kutles", "Thousand Foot Krutch"]
for band in bands:
    artist = Artist.create(name=band)

# Получение одной записи из БД
# Первый способ
# print(f'Название альбома от издателя "Refuge": {Album.select().where(Album.publisher == "Refuge").get().title}')  # или
# print(f'Название альбома от издателя "Refuge": {Album.select().where(Album.publisher == "Refuge")[0].title}')
# Операция выборки имеет схожие команды с теми, которые мы встречали в языке запросов (select, where)
# print(f'Название издателя альбома "Read All About It": {Album.get(Album.title == "Read All About It").publisher} ')

# Получение нескольких записей из БД
# for album in Album.select(): или
for album in Album.select(Album, Artist).join(Artist):
    print(f'Имя исполнителя: {album.artist.name} Название альбома: {album.title} Дата релиза: {album.release_date}')
    # album.title += '!'
    # album.save()
Album.delete().where(Album.id > 5).execute()
