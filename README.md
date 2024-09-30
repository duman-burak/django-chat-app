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

   git clone https://github.com/duman-burak/django-chat-app.git

   
2. Proje dizinine gir:
   
  cd django-chat-app


3. Sanal ortam oluştur ve etkinleştir:

   python -m venv env
   source env/bin/activate  # Windows için: env\Scripts\activate


4.Gerekli bağımlılıkları yükle:
   
  pip install -r requirements.txt


5.Veritabanı migrasyonlarını çalıştır:

  python manage.py makemigrations
  python manage.py migrate


6.Sunucuyu Çalıştır
  
  python manage.py runserver
