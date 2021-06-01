"""digi_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from digi_web import settings
from digi_web.views import page_home , headre_partial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page_home),
    path('headre_partial', headre_partial , name='headre_partial'),
    path('', include("eshope_account.urls")),
    path('', include("eshope_products.urls")),
    path('', include("eshope_products_category.urls")),
    path('', include("eshope_Subcategory.urls")),
    path('', include("eshope_order.urls")),
]
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
