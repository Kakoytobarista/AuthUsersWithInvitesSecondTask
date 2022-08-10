from django.contrib import admin
from .models import ReferralCode, ReferralRelationship


@admin.register(ReferralCode)
class ReferralCodeAdmin(admin.ModelAdmin):
    pass


@admin.register(ReferralRelationship)
class ReferralRelationship(admin.ModelAdmin):
    pass
