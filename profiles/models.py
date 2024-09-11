from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    # to get human readably name we can use User.get_role_display()
    class FamilyRole(models.IntegerChoices):
        MUM = 1, "Mum"
        DAD = 2, "Dad"
        SON = 3, "Son"
        DAUGHTER = 4, "Daughter"
        GRANDMA = 5, "Grandma"
        GRANDPA = 6, "Grandpa"
        UNDEFINED = 7, "Undefined"

    role = models.IntegerField(choices=FamilyRole, default=FamilyRole.UNDEFINED)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

