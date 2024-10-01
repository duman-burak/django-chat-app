Django ile geliştirilmiş gerçek zamanlı sohbet uygulaması. Kullanıcıların farklı sohbet odalarında mesajlaşmasına olanak tanır.

## Özellikler

- Kullanıcı kayıt ve giriş sistemi
- Gerçek zamanlı mesajlaşma
- Birden fazla sohbet odası
- kaydedilen mesajlar

###  Docker ile Redis Kurulumu
Redis'i Docker'da çalıştırmak için:

docker run -p 6379:6379 -d redis:5


## Kurulum

1. Depoyu klonla:

  -git clone https://github.com/duman-burak/django-chat-app.git

   
2. Proje dizinine gir:
   
  -cd django-chat-app


3. Sanal ortam oluştur ve etkinleştir:

   -python -m venv myvenv
   -Windows için: myvenv\Scripts\activate



4.Veritabanı migrasyonlarını çalıştır:

  python manage.py makemigrations
  python manage.py migrate


5.Sunucuyu Çalıştır
  
  python manage.py runserver
