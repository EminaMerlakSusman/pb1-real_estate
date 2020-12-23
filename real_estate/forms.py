from django import forms
from bootstrap4.widgets import RadioSelectButtonGroup
'''Importing regions so we can put them into the form'''
from real_estate.models import Listing
regions_choices = []

regs = open('real_estate/regions.csv', 'r', encoding='utf-8')
for reg_line in regs:
    reg_line = reg_line.split(';')
    id = reg_line[0]
    region = reg_line[1].strip()
    regions_choices.append((id, region))

'''Importing sale types'''
sale_choices = []

sales = open('real_estate/sale_type.csv', 'r', encoding='utf-8')
for sale_l in sales:
    sale_line = sale_l.split(';')
    id = sale_line[0]
    sale_type = sale_line[1].strip()
    sale_choices.append((id, sale_type))

sale_choices.append((3, 'Vseeno'))

'''Importing listing type data to put in the form'''
type_choices = []
types = open('real_estate/listing_types.csv', 'r', encoding='utf-8')


'''Size choices'''
size_choices = [('0x30', '0 - 30 m2'), ('30x60', '30 - 60 m2'), ('60x100', '60 - 100 m2'), ('100x200', '100 - 200 m2'), ('200x500', '200 - 500 m2'), ('500', '500+ m2')]


for type_tup in types:
    type_tup = type_tup.split(';')
    id = type_tup[0]
    l_type = type_tup[1].strip()
    type_choices.append((id, l_type))

class ToFromForm(forms.Form):
    from_field = forms.IntegerField(label="Najnižja cena:", required=False,
                             widget=forms.NumberInput(
             attrs={
                     'class': 'form-control', # applying bootstrap classes to the form
                     'placeholder': 'Cena od:'
             })
            )
    to_field = forms.IntegerField(label='Najvišja cena:', required=False,
                  widget=forms.NumberInput(attrs={
                     'class': 'form-control',
                     'placeholder': 'Cena do:'
             })

            )
    region_choice = forms.MultipleChoiceField(
        required=False,
        choices=regions_choices,
        label="Regija:",
        widget = forms.CheckboxSelectMultiple(attrs={
             'class': 'form-check-input',
         })
         )

    type_choice = forms.MultipleChoiceField(
        required=False,
        choices=type_choices,
        label="Tip nepremičnine:",
        widget=forms.CheckboxSelectMultiple(attrs={
             'class': 'form-check-input',

         })


    )
    sale_type_choice = forms.ChoiceField(
        required=False,
        choices=sale_choices,
        label="Vrsta posredovanja:",
        widget=forms.RadioSelect(attrs={
             'class': 'form-check-input',
             'type':'radio',

         })


    )
    size = forms.ChoiceField(
        required=False,
        choices=size_choices,
        label="Velikost:",
        widget=forms.RadioSelect(attrs={
             'class': 'form-check-input',
             'type': 'radio',


         })


    )

class AddListingForm(forms.Form):

    title = forms.CharField(
        required=True,
        label="Naslov oglasa:",
        widget=forms.TextInput
    )
    region_choice = forms.CharField(
        required=True,
        label="Regija:",
        widget = forms.Select(choices=regions_choices)
         )

    type_choice = forms.CharField(
        required=True,
        label="Tip nepremičnine:",
        widget=forms.Select(choices=type_choices, attrs={'class':"dropdown-toggle"})


    )
    sale_type_choice = forms.ChoiceField(
        required=True,
        choices=sale_choices,
        label="Vrsta posredovanja:",
        widget=forms.RadioSelect(choices=sale_choices)


    )
    size = forms.IntegerField(
        required=True,
        label="Velikost:",


    )
    nu_rooms = forms.DecimalField(
        required=False,
        label="Št. sob",

    )
    price = forms.IntegerField(
        required=True,
        label="Cena:",

    )

    def clean(self): # number of rooms is required on everything that isn't land

        super().clean()
        is_land = self.cleaned_data.get("type_choice")
        nu_rooms = self.cleaned_data.get("nu_rooms")
        if is_land != '3' and nu_rooms == None:
            raise forms.ValidationError("Prosimo vnesite število sob.")
        elif is_land == '3' and nu_rooms != None:
            raise forms.ValidationError("Pri tipu nepremičnine 'Posest' ne morete vnesti števila sob.")