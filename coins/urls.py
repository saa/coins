from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from coins.bank import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'accounts', views.AccountViewSet, base_name='account')
router.register(r'payments', views.PaymentViewSet, base_name='payment')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^docs/', include_docs_urls(title='Bank API', public=True)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
