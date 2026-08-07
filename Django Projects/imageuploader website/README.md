# Django Image Uploader Website

A simple web application built with Django that allows users to upload and display images. This project demonstrates how to work with image uploads in Django using `ImageField`, `MEDIA_URL`, and `MEDIA_ROOT`.

## 📸 Features

- Upload images through a web form
- Store uploaded images in the media directory
- Display uploaded images on the website
- Django Admin integration
- Simple and beginner-friendly project structure

---

## 🛠 Technologies Used

- Python 3
- Django
- HTML5
- CSS3
- SQLite3
- Pillow (for image processing)

---

## 📂 Project Structure

```text
image_uploader/
│
├── app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── media/
├── image_uploader/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-image-uploader.git
cd django-image-uploader
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a requirements file:

```bash
pip install django pillow
```

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## ⚙️ Media Configuration

Add the following settings in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Update `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your URLs
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
```

---

## 📦 Requirements

```txt
Django
Pillow
```

Generate automatically:

```bash
pip freeze > requirements.txt
```

---

## 🎯 Learning Outcomes

This project helped me understand:

- Django Models and `ImageField`
- Handling file uploads in Django
- Working with `MEDIA_URL` and `MEDIA_ROOT`
- Django Forms and Views
- Serving media files during development
- Basic CRUD operations with images

---

## 📷 Screenshots

Add screenshots of your application here:

- Home Page
- Upload Form
- Image Gallery

---

## 👨‍💻 Author

**Faizan Ali**

- GitHub: https://github.com/your-username
- LinkedIn: https://www.linkedin.com/in/your-profile

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub and connect with me on LinkedIn.
