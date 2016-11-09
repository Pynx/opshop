# coding=utf-8
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import SaleForm
from app.models import Sale, SaleLine, Transaction


class SaleFormView(CreateView):
    form_class = SaleForm
    model = Sale
    template_name = "app/sale.html"

    def form_valid(self, form):
        ret = super(SaleFormView, self).form_valid(form)
        sl = SaleLine(quantity=1, item=form.cleaned_data['item'], sale=self.object)
        sl.save()
        if self.object.payment_mode == 'credit':
            t = Transaction(user=self.object.user, amount=-self.object.total)
            t.save()
            messages.success(self.request, "{0}€ have been substracted from your total. You now have {1}€ available".format(self.object.total, self.object.user.profile.balance))
        else:
            messages.success(self.request, "Please insert {0}€ in het potje, we are watching you! :D".format(self.object.total))
        return ret

    def get_success_url(self):
        return reverse_lazy('sale')