from django.db import models
from django.utils import timezone as django_timezone

from uuid import uuid4
from datetime import datetime

from retailer.models import Retailer
from store.models import Store
from category.models import Category
from common.property import Property


class Product (models.Model):
    """
    Product got special price during promotion date.
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    retailer = models.ForeignKey(Retailer, on_delete=models.PROTECT, null=False, related_name='+')
    # Freshchoice and Supervalue can't get product store.
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, related_name='+')

    title = models.CharField(max_length=256)
    # Product brief decription combine with quantity like 3 packs, 250g, 2kg etc. (freshchoice)
    description = models.CharField(max_length=512)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    # product unit, like each(ea), pack, bag, kg.
    unit = models.CharField(max_length=32, null=False, blank=True)
    saved = models.CharField(max_length=64, null=True, blank=False)
    landing_page = models.CharField(max_length=512, null=False, blank=False, db_index=True)

    promotion_start_date = models.PositiveIntegerField(null=False)
    promotion_end_date = models.PositiveIntegerField(null=False)

    # ready field is used to indicate crawl status, a product is ready only if
    # all of its images are downloaded and processed.
    ready = models.BooleanField(default=False)

    # Foursquare, New World and Pakn Save product can't get category information.
    categories = models.ManyToManyField(Category, related_name='+')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    def __repr__(self):
        return 'Product: id={0}, retailer={1}, title={2}, desc={3}, ' \
               'price={4}, unit={5}, saved={6}' \
               'store={7}, ' \
               'prom_start={8}, prom_end={9},' \
               'detail={10}'\
            .format(self.id, self.retailer_id, self.title, self.description,
                    self.price, self.unit, self.saved,
                    self.store_id,
                    self.promotion_start_date, self.promotion_end_date,
                    self.landing_page)


class ProductProperty (Property):
    """
    Product property bag.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, related_name='properties')

    def __repr__(self):
        return 'ProductProperty: id={0}, name={1}, value={2}, product={3}'.format(
            self.pk, self.name, self.value, self.product_id)


class ProductImage (models.Model):
    """
    Product image
    """
    # Pak'n save product has no image. (a product may have 0 or more images.)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, related_name='product_images')
    unique_hash = models.CharField(max_length=64, unique=True, null=False, blank=False)
    original_url = models.CharField(max_length=512, null=False, blank=False)

    def __repr__(self):
        return 'ProductImage: id={0}, hash={1}, product={2}, origin={3}'.format(
            self.pk, self.unique_hash, self.product_id, self.original_url)
