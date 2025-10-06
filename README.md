# Django Blog

Sebuah platform blog sederhana dan mudah dikembangkan yang dibuat dengan [Django](https://www.djangoproject.com/).  
Proyek ini menampilkan fitur autentikasi pengguna, posting, pencarian, dan kontak, menggunakan praktik terbaik Django serta beberapa paket pihak ketiga populer.

---

## Fitur

- Registrasi, login, dan logout pengguna (menggunakan [django-allauth](https://docs.allauth.org/))
- Membuat, mengedit, menghapus, dan mencari postingan blog
- Formulir kontak
- Formulir responsif dengan [django-crispy-forms](https://django-crispy-forms.readthedocs.io/) dan Bootstrap 5
- Manajemen variabel lingkungan dengan [python-dotenv](https://github.com/theskumar/python-dotenv)
- Upload file media
- Dukungan cache Redis

---

## Cara Memulai

### 1. Kloning repositori

```sh
git clone https://github.com/yourusername/django_blog.git
cd django_blog/Blog-base
```

### 2. Buat dan aktifkan virtual environment

```sh
python -m venv env
env\Scripts\activate
```

### 3. Instalasi dependensi

```sh
pip install -r requirements.txt
```

Atau instal manual:

```sh
pip install Django==5.2.6 django-allauth==65.12.0 django-crispy-forms==2.4 crispy-bootstrap5==2025.6 python-dotenv==1.1.1 django-redis==6.0.0 pillow==11.3.0 redis==6.4.0 requests==2.32.5
```

### 4. Variabel Lingkungan

Buat file `.env` di root proyek untuk menyimpan pengaturan sensitif (lihat `.gitignore` untuk file yang diabaikan):

```
DJANGO_SECRET_KEY = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
GOOGLE_CLIENT_ID = ''
GOOGLE_CLIENT_SECRET = ''
# Tambahkan variabel lain sesuai kebutuhan
```

> **Tips:** Gunakan [python-dotenv](https://github.com/theskumar/python-dotenv) agar variabel ini otomatis dimuat.

---

## Daftar Dependensi Utama

| Paket               | Versi   | Keterangan                             |
| ------------------- | ------- | -------------------------------------- |
| Django              | 5.2.6   | Framework web utama                    |
| django-allauth      | 65.12.0 | Autentikasi & login sosial             |
| django-crispy-forms | 2.4     | Membuat form Django lebih rapi         |
| crispy-bootstrap5   | 2025.6  | Bootstrap 5 untuk crispy-forms         |
| python-dotenv       | 1.1.1   | Memuat variabel lingkungan dari `.env` |
| django-redis        | 6.0.0   | Backend cache Redis untuk Django       |
| pillow              | 11.3.0  | Pengolahan gambar                      |
| redis               | 6.4.0   | Client Python untuk Redis              |
| requests            | 2.32.5  | Library HTTP requests                  |

_Dependensi lain: asgiref, certifi, cffi, charset-normalizer, cryptography, idna, pip, pycparser, PyJWT, sqlparse, tzdata, urllib3_

---

## Menjalankan Proyek

```sh
python manage.py makemigration
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Buka [http://127.0.0.1:8000/](http://127.0.0.1:8000/) di browser Anda.

## Menjalankan Redis dengan Docker

Aplikasi ini menggunakan Redis sebagai backend cache. Jika Anda belum memiliki Redis yang berjalan di komputer, Anda bisa menjalankannya dengan Docker.

### 1. Jalankan Redis dengan Docker

```sh
docker run -d --name redis-blog -p 6379:6379 redis:7
```

Perintah di atas akan:
- Mengunduh image Redis versi 7 (jika belum ada)
- Menjalankan Redis di background (opsi `-d`)
- Membuka port 6379 agar bisa diakses aplikasi Django

### 2. Pastikan Redis Berjalan

Cek dengan perintah berikut:

```sh
docker ps
```

Harus ada container bernama `redis-blog` yang statusnya "Up".

### 3. Konfigurasi Django

Pastikan pengaturan cache di `settings.py` sudah mengarah ke Redis, misalnya:

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

---

> **Catatan:**  
> - Redis harus berjalan sebelum Anda menjalankan aplikasi Django.  
> - Jika menggunakan Docker Compose, Anda bisa mengatur service Redis dan Django sekaligus.
> - Memiliki WSL di docker atau laptop anda