#!/usr/bin/python
# -*- coding: utf8 -*-
# python imports
import os

# django imports
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.webdesign.lorem_ipsum import paragraph, sentence, words

# lfs imports
from lfs.core.models import Action, Shop
from lfs.catalog.models import Category, Product, Image, DeliveryTime
from lfs.catalog.settings import DELIVERY_TIME_UNIT_DAYS
from lfs.core.fields.thumbs import ImageWithThumbsField
from lfs.marketing.models import Topseller, FeaturedProduct
from lfs.criteria.models import WeightCriterion, CriteriaObjects, CountryCriterion
from lfs.criteria.settings import LESS_THAN_EQUAL, IS, IS_NOT, GREATER_THAN
from lfs.shipping.models import ShippingMethod, ShippingMethodPrice
from lfs.tax.models import Tax
from portlets.models import PortletAssignment, Slot, PortletRegistration
from lfs.portlet.models import CartPortlet, CategoriesPortlet, PagesPortlet, RecentProductsPortlet, RelatedProductsPortlet, TextPortlet, PagesPortlet
from lfs.payment.models import PaymentMethod

# other imports
from countries.models import Country

DIRNAME=os.path.dirname(__file__)


def load_data():
    
    site = Site.objects.all()[0]
    site.name = site.domain = "www.example.com"
    site.save()
    
    ie = Country.objects.get(iso="IE")
    gb = Country.objects.get(iso="GB")
    de = Country.objects.get(iso="DE")
    us = Country.objects.get(iso="US")
    fr = Country.objects.get(iso="FR")
    
    shop, created = Shop.objects.get_or_create(name="lfs test", shop_owner="John Doe",
                                      default_country=ie)
    shop.save()
    shop.countries.add(ie)
    shop.countries.add(gb)
    shop.countries.add(de)
    shop.countries.add(us)
    shop.countries.add(fr)
    shop.save()
    
    tax = Tax.objects.create(rate = 21)

    direct_debit = PaymentMethod.objects.create(
            name="Direct Debit",
            active=True,
            tax=tax,
        )

    cod = PaymentMethod.objects.create(
        name="Cash on delivery",
        active=True,
        tax=tax,
    )

    paypal = PaymentMethod.objects.create(
        name="PayPal",
        active=True,
        tax=tax,
    )

    prepayment = PaymentMethod.objects.create(
        name="Prepayment",
        active=True,
        tax=tax,
    )

    by_invoice = PaymentMethod.objects.create(
        name="By invoice",
        active=True,
        tax=tax,
    )

    categories = ['animals', 'transport', 'food']
    for cat in categories:    
        category, created = Category.objects.get_or_create(name=cat, slug=slugify(cat))
        
    
    products = ["Cat", "Dog", "Mouse", "Surfboard", "Car", "Ship",
                 "Chocolate", "Apple", "Orange"]
    i = 0
    for p in products:
        product, created = Product.objects.get_or_create(name=p, slug=slugify(p), price=(i+1)*10.0, 
                                                                 sku=i, active=True, manage_stock_amount=False)
        product.description = paragraph()
        product.save()
        
        category = Category.objects.all()[i/3]
        category.products.add(product)
        category.save()        
        ts, created = Topseller.objects.get_or_create(product=product, position=i)
        fp, created = FeaturedProduct.objects.get_or_create(product=product, position=i)
        i = i + 1

    
    # shipping prices setup
    delivery_time, created = DeliveryTime.objects.get_or_create(min=2, max=7, unit=DELIVERY_TIME_UNIT_DAYS, description="2 to 7 for delivery")
            
    # criterion for geo-specific delivery charges    
    cc_ie_uk = CountryCriterion.objects.create(operator=IS)
    cc_ie_uk.countries.add(ie)
    cc_ie_uk.countries.add(gb)
    cc_ie_uk.save()
    
    cc_not_ie_uk = CountryCriterion.objects.create(operator=IS_NOT)
    cc_not_ie_uk.countries.add(ie)
    cc_not_ie_uk.countries.add(gb)
    cc_not_ie_uk.save()
    
    #Rest of World >1kg ?16.95    
    smp_1095, created = ShippingMethod.objects.get_or_create(name="Ireland & UK", price=10.95, active=True, delivery_time=delivery_time, priority=1)    
    smp_1500, created = ShippingMethod.objects.get_or_create(name="International", price=15.00, active=True, delivery_time=delivery_time, priority=1)
        
    co = CriteriaObjects(criterion=cc_ie_uk, content=smp_1095)
    co.save()
    
    co = CriteriaObjects(criterion=cc_not_ie_uk, content=smp_1500)
    co.save()    
    
    # Tax
    thirteen_percent = Tax.objects.get_or_create(rate=13.5, description="13.5% rate")
    twentyone_percent = Tax.objects.get_or_create(rate=21, description="21% rate")
        
        
    left_slot, created = Slot.objects.get_or_create(name="Left")     
    right_slot, created = Slot.objects.get_or_create(name="Right")
    
    cart_portlet, created = CartPortlet.objects.get_or_create(title="Cart")
    pages_portlet, created = PagesPortlet.objects.get_or_create(title="Information")
    categories_portlet, created = CategoriesPortlet.objects.get_or_create(title="Products")
    relatedproducts_portlet, created = RelatedProductsPortlet.objects.get_or_create(title="Related Products")
    recentproducts_portlet, created = RecentProductsPortlet.objects.get_or_create(title="Recent Products")
    
    PortletAssignment.objects.create(slot_id=left_slot.id, content=shop, portlet=categories_portlet, position=10)    
    PortletAssignment.objects.create(slot_id=left_slot.id, content=shop, portlet=pages_portlet, position=15)
    PortletAssignment.objects.create(slot_id=right_slot.id, content=shop, portlet=cart_portlet, position=10)
    PortletAssignment.objects.create(slot_id=right_slot.id, content=shop, portlet=recentproducts_portlet, position=20)
    PortletAssignment.objects.create(slot_id=right_slot.id, content=shop, portlet=relatedproducts_portlet, position=30)
    
    
def run():
    load_data()
