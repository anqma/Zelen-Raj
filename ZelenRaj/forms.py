from django import forms
from .models import Plant, Order


class PlantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlantForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Plant
        exclude = ("user",)
        labels = {
            'name': 'Име на растението',
            'image': 'Слика од растението',
            'price': 'Цена',
            'care_info': 'Информации за нега на растението',
            'stock': 'Залиха'
        }


class OrderForm(forms.ModelForm):
    PAYMENT_CHOICES = [(True, 'Електронско плаќање'), (False, 'Плаќање во готово при достава')]

    payment_method = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=PAYMENT_CHOICES,
        initial=[False],  # Set "Плаќање во готово при достава" as the initial value because currently the electronic payment option is not available
        label='Начин на плаќање'
    )

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['payment_method'].widget.attrs['class'] = 'payment-method-checkboxes'

        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
        self.visible_fields()[4].field.widget.attrs["class"] = ""
        self.visible_fields()[4].field.widget.attrs["disabled"] = True

    class Meta:
        model = Order
        exclude = ("order_date",)
        labels = {
            'user_name': 'Име и презиме',
            'email': 'Email',
            'delivery_address': 'Адреса на достава',
            'note': 'Забелешка',
            'contact_information': 'Телефонски број за контакт'
        }
