from decimal import Decimal
from django.db import models

from django_countries.fields import CountryField

from accounts.models import Account

VAT_AMOUNT = (('0.00', '0%'),
              ('0.05', '5%'),
              ('0.08', '8%'),
              ('0.23', '23%'))

UNITS = (('1', 'Days'),
         ('2', 'Deliveries'),
         ('3', 'Cartons'),
         ('4', 'Boxes'),
         ('5', 'Kilograms'),
         ('6', 'Kilometers'),
         ('7', 'Cubic Meter'),
         ('8', 'Square Meters'),
         ('9', 'Liters'),
         ('10', 'Months'),
         ('11', 'Meters'),
         ('12', 'Packages'),
         ('13', 'Sessions'),
         ('14', 'Pieces'),
         ('15', 'Sets'),
         ('16', 'Hours'),
         ('17', 'Weeks'))

EMPLOYMENT_SIZE = (('1-9', '1-9'),
                   ('10-19', '10-19'),
                   ('20-49', '20-49'),
                   ('250+', '250+'))

JOB_INDUSTRIES = (('Accounting', 'Accounting'),
                  ('Airlines/Aviation', 'Airlines/Aviation'),
                  ('Alternative Dispute Resolution', 'Alternative Dispute Resolution'),
                  ('Alternative Medicine', 'Alternative Medicine'),
                  ('Animation', 'Animation'),
                  ('Apparel & Fashion', 'Apparel & Fashion'),
                  ('Architecture & Planning', 'Architecture & Planning'),
                  ('Arts and Crafts', 'Arts and Crafts'),
                  ('Automotive', 'Automotive'),
                  ('Aviation & Aerospace', 'Aviation & Aerospace'),
                  ('Banking', 'Banking'),
                  ('Biotechnology', 'Biotechnology'),
                  ('Broadcast Media', 'Broadcast Media'),
                  ('Building Materials', 'Building Materials'),
                  ('Business Supplies and Equipment', 'Business Supplies and Equipment'),
                  ('Capital Markets', 'Capital Markets'),
                  ('Chemicals', 'Chemicals'),
                  ('Civic & Social Organization', 'Civic & Social Organization'),
                  ('Civil Engineering', 'Civil Engineering'),
                  ('Commercial Real Estate', 'Commercial Real Estate'),
                  ('Computer & Network Security', 'Computer & Network Security'),
                  ('Computer Games', 'Computer Games'),
                  ('Computer Hardware', 'Computer Hardware'),
                  ('Computer Networking', 'Computer Networking'),
                  ('Computer Software', 'Computer Software'),
                  ('Construction', 'Construction'),
                  ('Consumer Electronics', 'Consumer Electronics'),
                  ('Consumer Goods', 'Consumer Goods'),
                  ('Consumer Services', 'Consumer Services'),
                  ('Cosmetics', 'Cosmetics'),
                  ('Dairy', 'Dairy'),
                  ('Defense & Space', 'Defense & Space'),
                  ('Design', 'Design'),
                  ('Education Management', 'Education Management'),
                  ('E-Learning', 'E-Learning'),
                  ('Electrical/Electronic Manufacturing', 'Electrical/Electronic Manufacturing'),
                  ('Entertainment', 'Entertainment'),
                  ('Environmental Services', 'Environmental Services'),
                  ('Events Services', 'Events Services'),
                  ('Executive Office', 'Executive Office'),
                  ('Facilities Services', 'Facilities Services'),
                  ('Farming', 'Farming'),
                  ('Financial Services', 'Financial Services'),
                  ('Fine Art', 'Fine Art'),
                  ('Fishery', 'Fishery'),
                  ('Food & Beverages', 'Food & Beverages'),
                  ('Food Production', 'Food Production'),
                  ('Fund-Raising', 'Fund-Raising'),
                  ('Furniture', 'Furniture'),
                  ('Gambling & Casinos', 'Gambling & Casinos'),
                  ('Glass, Ceramics & Concrete', 'Glass, Ceramics & Concrete'),
                  ('Government Administration', 'Government Administration'),
                  ('Government Relations', 'Government Relations'),
                  ('Graphic Design', 'Graphic Design'),
                  ('Health, Wellness and Fitness', 'Health, Wellness and Fitness'),
                  ('Higher Education', 'Higher Education'),
                  ('Hospital & Health Care', 'Hospital & Health Care'),
                  ('Hospitality', 'Hospitality'),
                  ('Human Resources', 'Human Resources'),
                  ('Import and Export', 'Import and Export'),
                  ('Individual & Family Services', 'Individual & Family Services'),
                  ('Industrial Automation', 'Industrial Automation'),
                  ('Information Services', 'Information Services'),
                  ('Information Technology and Services', 'Information Technology and Services'),
                  ('Insurance', 'Insurance'),
                  ('International Affairs', 'International Affairs'),
                  ('International Trade and Development', 'International Trade and Development'),
                  ('Internet', 'Internet'),
                  ('Investment Banking', 'Investment Banking'),
                  ('Investment Management', 'Investment Management'),
                  ('Judiciary', 'Judiciary'),
                  ('Law Enforcement', 'Law Enforcement'),
                  ('Law Practice', 'Law Practice'),
                  ('Legal Services', 'Legal Services'),
                  ('Legislative Office', 'Legislative Office'),
                  ('Leisure, Travel & Tourism', 'Leisure, Travel & Tourism'),
                  ('Libraries', 'Libraries'),
                  ('Logistics and Supply Chain', 'Logistics and Supply Chain'),
                  ('Luxury Goods & Jewelry', 'Luxury Goods & Jewelry'),
                  ('Machinery', 'Machinery'),
                  ('Management Consulting', 'Management Consulting'),
                  ('Maritime', 'Maritime'),
                  ('Marketing and Advertising', 'Marketing and Advertising'),
                  ('Market Research', 'Market Research'),
                  # Longest (36 words)
                  ('Mechanical or Industrial Engineering', 'Mechanical or Industrial Engineering'),
                  ('Media Production', 'Media Production'),
                  ('Medical Devices', 'Medical Devices'),
                  ('Medical Practice', 'Medical Practice'),
                  ('Mental Health Care', 'Mental Health Care'),
                  ('Military', 'Military'),
                  ('Mining & Metals', 'Mining & Metals'),
                  ('Motion Pictures and Film', 'Motion Pictures and Film'),
                  ('Museums and Institutions', 'Museums and Institutions'),
                  ('Music', 'Music'),
                  ('Nanotechnology', 'Nanotechnology'),
                  ('Newspapers', 'Newspapers'),
                  ('Nonprofit Organization Management', 'Nonprofit Organization Management'),
                  ('Oil & Energy', 'Oil & Energy'),
                  ('Online Media', 'Online Media'),
                  ('Outsourcing/Offshoring', 'Outsourcing/Offshoring'),
                  ('Package/Freight Delivery', 'Package/Freight Delivery'),
                  ('Packaging and Containers', 'Packaging and Containers'),
                  ('Paper & Forest Products', 'Paper & Forest Products'),
                  ('Performing Arts', 'Performing Arts'),
                  ('Pharmaceuticals', 'Pharmaceuticals'),
                  ('Philanthropy', 'Philanthropy'),
                  ('Photography', 'Photography'),
                  ('Plastics', 'Plastics'),
                  ('Political Organization', 'Political Organization'),
                  ('Primary/Secondary Education', 'Primary/Secondary Education'),
                  ('Printing', 'Printing'),
                  ('Professional Training & Coaching', 'Professional Training & Coaching'),
                  ('Program Development', 'Program Development'),
                  ('Public Policy', 'Public Policy'),
                  ('Public Relations and Communications', 'Public Relations and Communications'),
                  ('Public Safety', 'Public Safety'),
                  ('Publishing', 'Publishing'),
                  ('Railroad Manufacture', 'Railroad Manufacture'),
                  ('Ranching', 'Ranching'),
                  ('Real Estate', 'Real Estate'),
                  ('Recreational Facilities and Services', 'Recreational Facilities and Services'),
                  ('Religious Institutions', 'Religious Institutions'),
                  ('Renewables & Environment', 'Renewables & Environment'),
                  ('Research', 'Research'),
                  ('Restaurants', 'Restaurants'),
                  ('Retail', 'Retail'),
                  ('Security and Investigations', 'Security and Investigations'),
                  ('Semiconductors', 'Semiconductors'),
                  ('Shipbuilding', 'Shipbuilding'),
                  ('Sporting Goods', 'Sporting Goods'),
                  ('Sports', 'Sports'),
                  ('Staffing and Recruiting', 'Staffing and Recruiting'),
                  ('Supermarkets', 'Supermarkets'),
                  ('Telecommunications', 'Telecommunications'),
                  ('Textiles', 'Textiles'),
                  ('Think Tanks', 'Think Tanks'),
                  ('Tobacco', 'Tobacco'),
                  ('Translation and Localization', 'Translation and Localization'),
                  ('Transportation/Trucking/Railroad', 'Transportation/Trucking/Railroad'),
                  ('Utilities', 'Utilities'),
                  ('Venture Capital & Private Equity', 'Venture Capital & Private Equity'),
                  ('Veterinary', 'Veterinary'),
                  ('Warehousing', 'Warehousing'),
                  ('Wholesale', 'Wholesale'),
                  ('Wine and Spirits', 'Wine and Spirits'),
                  ('Wireless', 'Wireless'),
                  ('Writing and Editing', 'Writing and Editing'))

CURRENCIES = (('AED', 'AED'),
              ('AFN', 'AFN'),
              ('ALL', 'ALL'),
              ('AMD', 'AMD'),
              ('ANG', 'ANG'),
              ('AOA', 'AOA'),
              ('ARS', 'ARS'),
              ('AUD', 'AUD'),
              ('AWG', 'AWG'),
              ('AZN', 'AZN'),
              ('BAM', 'BAM'),
              ('BBD', 'BBD'),
              ('BDT', 'BDT'),
              ('BGN', 'BGN'),
              ('BHD', 'BHD'),
              ('BIF', 'BIF'),
              ('BMD', 'BMD'),
              ('BND', 'BND'),
              ('BOB', 'BOB'),
              ('BRL', 'BRL'),
              ('BSD', 'BSD'),
              ('BTN', 'BTN'),
              ('BWP', 'BWP'),
              ('BYN', 'BYN'),
              ('BZD', 'BZD'),
              ('CAD', 'CAD'),
              ('CDF', 'CDF'),
              ('CHF', 'CHF'),
              ('CLP', 'CLP'),
              ('CNY', 'CNY'),
              ('COP', 'COP'),
              ('CRC', 'CRC'),
              ('CUC', 'CUC'),
              ('CUP', 'CUP'),
              ('CVE', 'CVE'),
              ('CZK', 'CZK'),
              ('DJF', 'DJF'),
              ('DKK', 'DKK'),
              ('DOP', 'DOP'),
              ('DZD', 'DZD'),
              ('EGP', 'EGP'),
              ('ERN', 'ERN'),
              ('ETB', 'ETB'),
              ('EUR', 'EUR'),
              ('FJD', 'FJD'),
              ('FKP', 'FKP'),
              ('GBP', 'GBP'),
              ('GEL', 'GEL'),
              ('GGP', 'GGP'),
              ('GHS', 'GHS'),
              ('GIP', 'GIP'),
              ('GMD', 'GMD'),
              ('GNF', 'GNF'),
              ('GTQ', 'GTQ'),
              ('GYD', 'GYD'),
              ('HKD', 'HKD'),
              ('HNL', 'HNL'),
              ('HRK', 'HRK'),
              ('HTG', 'HTG'),
              ('HUF', 'HUF'),
              ('IDR', 'IDR'),
              ('ILS', 'ILS'),
              ('IMP', 'IMP'),
              ('INR', 'INR'),
              ('IQD', 'IQD'),
              ('IRR', 'IRR'),
              ('ISK', 'ISK'),
              ('JEP', 'JEP'),
              ('JMD', 'JMD'),
              ('JOD', 'JOD'),
              ('JPY', 'JPY'),
              ('KES', 'KES'),
              ('KGS', 'KGS'),
              ('KHR', 'KHR'),
              ('KID', 'KID'),
              ('KMF', 'KMF'),
              ('KPW', 'KPW'),
              ('KRW', 'KRW'),
              ('KWD', 'KWD'),
              ('KYD', 'KYD'),
              ('KZT', 'KZT'),
              ('LAK', 'LAK'),
              ('LBP', 'LBP'),
              ('LKR', 'LKR'),
              ('LRD', 'LRD'),
              ('LSL', 'LSL'),
              ('LYD', 'LYD'),
              ('MAD', 'MAD'),
              ('MDL', 'MDL'),
              ('MGA', 'MGA'),
              ('MKD', 'MKD'),
              ('MMK', 'MMK'),
              ('MNT', 'MNT'),
              ('MOP', 'MOP'),
              ('MRU', 'MRU'),
              ('MUR', 'MUR'),
              ('MVR', 'MVR'),
              ('MWK', 'MWK'),
              ('MXN', 'MXN'),
              ('MYR', 'MYR'),
              ('MZN', 'MZN'),
              ('NAD', 'NAD'),
              ('NGN', 'NGN'),
              ('NIO', 'NIO'),
              ('NOK', 'NOK'),
              ('NPR', 'NPR'),
              ('NZD', 'NZD'),
              ('OMR', 'OMR'),
              ('PAB', 'PAB'),
              ('PEN', 'PEN'),
              ('PGK', 'PGK'),
              ('PHP', 'PHP'),
              ('PKR', 'PKR'),
              ('PLN', 'PLN'),
              ('PRB', 'PRB'),
              ('PYG', 'PYG'),
              ('QAR', 'QAR'),
              ('RON', 'RON'),
              ('RSD', 'RSD'),
              ('RUB', 'RUB'),
              ('RWF', 'RWF'),
              ('SAR', 'SAR'),
              ('SEK', 'SEK'),
              ('SGD', 'SGD'),
              ('SHP', 'SHP'),
              ('SLL', 'SLL'),
              ('SLS', 'SLS'),
              ('SOS', 'SOS'),
              ('SRD', 'SRD'),
              ('SSP', 'SSP'),
              ('STN', 'STN'),
              ('SYP', 'SYP'),
              ('SZL', 'SZL'),
              ('THB', 'THB'),
              ('TJS', 'TJS'),
              ('TMT', 'TMT'),
              ('TND', 'TND'),
              ('TOP', 'TOP'),
              ('TRY', 'TRY'),
              ('TTD', 'TTD'),
              ('TVD', 'TVD'),
              ('TWD', 'TWD'),
              ('TZS', 'TZS'),
              ('UAH', 'UAH'),
              ('UGX', 'UGX'),
              ('USD', 'USD'),
              ('UYU', 'UYU'),
              ('UZS', 'UZS'),
              ('VES', 'VES'),
              ('VND', 'VND'),
              ('VUV', 'VUV'),
              ('WST', 'WST'),
              ('XAF', 'XAF'),
              ('XCD', 'XCD'),
              ('XOF', 'XOF'),
              ('XPF', 'XPF'),
              ('ZAR', 'ZAR'),
              ('ZMW', 'ZMW'),
              ('ZWB', 'ZWB'))


class Client(models.Model):
    """
        This is for the client of an user. To make it easy to choose the individual client
        to invoice, add expenses from etc.
    """
    PAYMENT_METHOD = (
        ('IP', 'Invoice Paid'),
        ('RM', 'Recurring Monthly'),
        ('NE', 'Netto'),
        ('NC', 'Netto Cash')
    )

    # Company details
    co_logo = models.ImageField(upload_to="dashboard/logos", blank=True, null=True)
    user = models.ForeignKey(Account, default=None, on_delete=models.CASCADE, related_name='clients')
    co_nip_number = models.CharField(max_length=10)
    co_name = models.CharField(max_length=60)
    co_address = models.CharField(max_length=100)
    co_zip = models.CharField(max_length=10)
    co_city = models.CharField(max_length=30)
    co_country = CountryField(max_length=50)
    co_telephone = models.CharField(max_length=20)
    co_email = models.CharField(max_length=50)
    co_website = models.CharField(max_length=35)
    co_att_person = models.CharField(max_length=60)
    co_ean_number = models.CharField(max_length=30, null=True, blank=True)
    co_payment_method = models.CharField(max_length=2, choices=PAYMENT_METHOD, default='NE')
    # Invoice details
    in_currency = models.CharField(max_length=3, choices=CURRENCIES, default='PLN')
    in_sendto_mail = models.EmailField()
    in_sendto_subject = models.CharField(max_length=250)
    in_sendto_content = models.TextField()
    in_cc_mails = models.CharField(max_length=500)
    in_bcc_mails = models.CharField(max_length=500)
    # Advanced Details
    ad_employment_size = models.CharField(max_length=5, choices=EMPLOYMENT_SIZE)
    ad_company_industry = models.CharField(max_length=36, choices=JOB_INDUSTRIES)
    ad_company_type = models.CharField(max_length=50)

    def __str__(self):
        return self.co_name


class Invoice(models.Model):
    """
        This is for the overall invoice
    """
    client = models.ForeignKey(Client, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, default=None, on_delete=models.CASCADE, related_name='invoice')
    invoice_id = models.IntegerField(default=1, null=True, blank=True)
    place = models.CharField(max_length=40)
    created_at = models.DateTimeField(verbose_name='date', auto_now_add=True)
    date_sent = models.DateTimeField(verbose_name='date sent by mail', auto_now=True)
    date_deadline = models.DateTimeField(verbose_name='payment deadline', auto_now=False, null=True, blank=True)
    bank_number = models.CharField(max_length=40)
    iban_number = models.CharField(max_length=40)
    swift_bic = models.CharField(max_length=40)
    total = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=40)
    paid_status = models.BooleanField(default=False)
    custom_comment = models.CharField(max_length=40)
    reverse_charge = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) if self.user else ''

    def created_year(self):
        return self.created_at.strftime('%Y')

    def total_sum(self):
        return self.total

    class Meta:
        # Ensure a user can't submit parallel forms and get same invoice_id
        unique_together = ['invoice_id', 'user']


class InvoiceItem(models.Model):
    """
        This is for every individual service that will be added to an invoice
    """

    invoice = models.ForeignKey(Invoice, related_name='items', unique=False, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=0, default=1)
    vat_rule = models.CharField(choices=VAT_AMOUNT, default='0.23', max_length=4)
    unit = models.CharField(max_length=2, choices=UNITS, default=16)
    item_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.service

    def get_total_unit_price(self):
        # Gets the total price of an form field object (unit * quantity * vat)
        result = Decimal(self.vat_rule)
        item_total = self.unit_price * self.quantity * (1 + result / 100)
        overall_item_total = round(item_total, 2)

        return overall_item_total


class ExpensesPaid(models.Model):
    """
    This is for expenses that are paid, such as
    restaurant visits, transport or groceries shopping
    """
    VAT_AMOUNT = (
        ('0.00', '0%'),
        ('0.05', '5%'),
        ('0.08', '8%'),
        ('0.23', '23%')
    )

    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True, related_name='expenses_paid')
    purchase_date = models.DateField()
    bought_from = CountryField()  # Country
    description = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    vat_rule = models.CharField(choices=VAT_AMOUNT, default='0.23', max_length=4)

    def __str__(self):
        return str(self.user) if self.user else ''


class ExpensesToPay(models.Model):
    """
    This is for expenses that doesn't have to be paid same day.
    Typically an invoice from a supplier with a payment deadline on
    """
    VAT_AMOUNT = (
        ('0.00', '0%'),
        ('0.05', '5%'),
        ('0.08', '8%'),
        ('0.23', '23%')
    )

    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True, related_name='expenses_to_pay')
    invoice_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    payment_date = models.DateField()
    bought_from = CountryField()  # Country
    description = models.CharField(max_length=250)
    vat_rule = models.CharField(choices=VAT_AMOUNT, default='0.23', max_length=4)
    client = models.ForeignKey(Client, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) if self.user else ''
