from django.contrib import admin

# Register your models here.
from .models import SignUp
from .models import BlogPost
from .forms import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
	list_display=["__unicode__","timestamp","updated"]
	form = SignUpForm
	#class Meta:
	#	model=SignUp
	def __unicode__(self):
   		return unicode(self.some_field) or u''



admin.site.register(SignUp,SignUpAdmin)
admin.site.register(BlogPost)

