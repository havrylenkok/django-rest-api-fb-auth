from django.db import models

from util.models import CommonAbstractModel


class Place(CommonAbstractModel):

    TYPES = (
        (0, 'user_not_been'),
        (1, 'user_been')
    )

    """Model for places displayed """
    name = models.CharField(max_length=50, blank=True)
    long_position = models.DecimalField(max_digits=10, decimal_places=7)
    lat_position = models.DecimalField(max_digits=10, decimal_places=7)
    avatar = models.ImageField(upload_to='places', null=True, blank=True)
    type = models.SmallIntegerField(choices=TYPES, default=TYPES[0][0])

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return "/static/default-place.jpg"
