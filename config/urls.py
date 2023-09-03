from datetime import datetime
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def index(request):
    now = datetime.now()
    html = f"""
    <html>
        <body>
            <h1>Hello from AWS!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    """
    return HttpResponse(html)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", index),
]
