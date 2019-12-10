from django.db import models
from django.utils import timezone
import datetime
from django.forms import ModelForm
from django.conf import settings
################
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)
    is_active= models.BooleanField(default=True)
    def __str__(self):
        return self.name

def pre_save_category_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		slug = slugify(instance.name)

		instance.slug = slug

pre_save.connect(pre_save_category_slug,sender=Category)

class Subcategories(models.Model):
    subcategories_name=models.CharField(max_length=40)
    is_active= models.BooleanField(default=True)
    def __str__(self):
        return self.subcategories_name

class Brand(models.Model):
    brand_name=models.CharField(max_length=20)
    is_active= models.BooleanField(default=True)
    def __str__(self):
        return self.brand_name

class ProductManager(models.Manager):
	"""docstring for ProductManager"""
	def all(self, *args, **kwargs):
		return super(ProductManager, self).get_queryset().filter(available=True)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    subcategories_name = models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    product_name=models.CharField( max_length=50,blank=True, default=None, null=True)
    product_description = models.TextField(blank=True, default=None, null=True)
    product_price=models.FloatField(blank=True, default=None, null=True)
    discount = models.IntegerField(default=0)
    male="Man"
    female="Woman"
    kids="Kid"
    gender_product=(
                   (male,"Man"),
                   (female,"Women"),
                   (kids, "Kid")
    )
    product_num_size = models.IntegerField(blank=True, default=None, null=True, validators=[MaxValueValidator(45), MinValueValidator(12)])
    product_gender = models.CharField(max_length=5, choices=gender_product, default=male)
    eXtraSmall='XS'
    small="S"
    medium='M'
    large='L'
    eXtraLarge='XL'
    eXtra_eXtraLarge='XXL'
    size_choice=(
                 (eXtraSmall,"XS"),
                 (small, "S"),
                 (medium, "M"),
                 (large, "L"),
                 (eXtraLarge, "XL"),
                 (eXtra_eXtraLarge, "XXL")
    )
    product_size=models.CharField(max_length=3,choices=size_choice,default=small, blank=True, null=True)
    product_quantity=models.PositiveIntegerField()
    available = models.BooleanField(default=True, verbose_name="Доступен")
    # objects = ProductManager()
    # product_pub_date = models.DateTimeField( default = timezone.now, editable = False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return (self.product_name +" " + str(self.product_price)+' Tg')

class Like(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    heart_click= models.IntegerField(default=0)

class ProductImage(models.Model):
    product=models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="products/", blank = True)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.id


# class Shoe(models.Model):
#     shoe_name=models.CharField('Name of Shoe', max_length=50)
#     shoe_price=models.FloatField('Price of Shoe, Tg')
#     shoe_image = models.ImageField(upload_to="images/", blank = True)
#     male="Man"
#     female="Woman"
#     kids="Kid"
#     gender_product=(
#                    (male,"Man"),
#                    (female,"Women"),
#                    (kids, "Kid")
#     )
#     shoe_gender = models.CharField('Gender', max_length=5, choices=gender_product, default=male)
#     shoe_size=models.CharField('Size',max_length=2,validators=[MaxValueValidator(45), MinValueValidator(12)])
#     shoe_quantity=models.PositiveIntegerField("Quantity of products")
#     shoe_pub_date = models.DateTimeField("product Date and Time" , default = timezone.now, editable = False)
#     def __str__(self):
#         return (self.shoe_name +" " + str(self.shoe_price)+'Tg')

class Comment(models.Model):
    comment_text = models.TextField("Comment text")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_pub_date = models.DateTimeField("Coment Date and Time" , default = timezone.now, editable = False)
    def __str__(self):
        return self.comment_text


class CartItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)
    item_total=models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return "Cart item for product{0}".format(self.products.title)

class Cart(models.Model):

	items = models.ManyToManyField(CartItem, blank=True)
	cart_total = models.DecimalField(max_digits=9,decimal_places=2,default=0.00)



	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		return reverse('product_details', kwargs={'product_slug': self.slug})


	def add_to_cart(self,product_slug):
		cart = self
		product = Product.objects.get(slug=product_slug)
		new_item, _ =CartItem.objects.get_or_create(product=product,item_total=product.price)
		# cart = Cart.objects.first()

		if new_item  in cart.items.all():

			return HttpResponseRedirect('Этот товап имеется')


		if new_item not in cart.items.all():
			cart.items.add(new_item)
			cart.save()
			return HttpResponseRedirect('/cart/')

	def remove_from_cart(self,product_slug):
		cart = self
		product = Product.objects.get(slug=product_slug)

		for cart_item in cart.items.all():
			if cart_item.product == product:
				cart.items.remove(cart_item)
				cart.save()
				return HttpResponseRedirect('/cart/')

		# cart = Cart.objects.first()
