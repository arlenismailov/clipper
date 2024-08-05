from django.contrib import admin
from .models import *


class UserSocialNetworkLinkInline(admin.TabularInline):
    model = UserSocialNetworkLink
    extra = 1


class UserContactDataInline(admin.TabularInline):
    model = UserContactData
    extra = 1


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [UserSocialNetworkLinkInline, UserContactDataInline]


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(DesignerWork)
admin.site.register(Category)
admin.site.register(DesigneWorkReview)
admin.site.register(CustomUser)
admin.site.register(Chat)
admin.site.register(Message)
