from rest_framework import routers

from .views import ImageTestTableViewSet

router = routers.SimpleRouter()
router.register('images', ImageTestTableViewSet)

urlpatterns = [

]

urlpatterns += router.urls
