from django.views.generic.edit import CreateView
from cfp.models import Proposal

class ProposalCreate(CreateView):
    model = Proposal
    template_name = 'cfp.html'
    fields = ['first_name', 'last_name', 'category']
