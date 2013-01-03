# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from signup.models import SignupQueue
from signup.forms import ApplyLicenseForm, UploadSignedForm

class ApplyView(CreateView):
    form_class = ApplyLicenseForm
    model = SignupQueue
    success_url = '/step2'
    
    def form_valid(self, form):
        # form.send_email()
        return super(ApplyView, self).form_valid(form)
    
    
class UploadView(UpdateView):
    form_class = UploadSignedForm
    model = SignupQueue
    success_url = '/step3'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super(UploadView, self).form_valid(form)