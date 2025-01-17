from django.db import models
from services.choices import CHOICES
from services.uploader import Uploader
from services.mixin import DateMixin, SlugMixin
from services.generator import Generator
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
from accounts.models import MyUser
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from django.core.validators import RegexValidator

User = MyUser()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Countries(DateMixin, SlugMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Country"
        verbose_name_plural = 'Countries'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Countries)
        super(Countries, self).save(*args, **kwargs)


class Cities(models.Model):
    name = models.CharField(max_length=100, )
    country = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name





class Restaurants(DateMixin, SlugMixin):
    owner = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=200, )
    country_of_restaurant = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=200, )
    type_r = models.CharField(max_length=100, choices=CHOICES, null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0, editable=False,
                                 null=True, blank=True)
    number = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    opened = models.TimeField(null=True, blank=True, default='None')
    closed = models.TimeField(null=True, blank=True, default='None')
    available_seats = models.IntegerField(null=True, blank=True, default=0)
    wishlist = models.ManyToManyField(User, blank=True, related_name="wishlist", )
    has_permission = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('booking:menu', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Restaurants)

        super(Restaurants, self).save(*args, **kwargs)


class RestaurantImages(DateMixin, SlugMixin):
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE, )
    images = models.FileField(upload_to=Uploader.upload_images_to_restaurants, )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=RestaurantImages)

        if not self.images:
            img = Image.open(self.images.path)
            if img.height > 300 or img.width > 300:
                new_img = (626, 600)
                img.thumbnail(new_img)
                img.save(self.images.path)

        super(RestaurantImages, self).save(*args, **kwargs)


class RestaurantMenu(DateMixin, SlugMixin):
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE, )
    menu_images = models.FileField(upload_to=Uploader.upload_images_for_menu, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=RestaurantMenu)

        if not self.menu_images:
            img = Image.open(self.images.path)
            if img.height > 300 or img.width > 300:
                new_img = (626, 600)
                img.thumbnail(new_img)
                img.save(self.menu_images.path)

        super(RestaurantMenu, self).save(*args, **kwargs)


class CooperationCompanies(DateMixin, SlugMixin):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=Uploader.upload_images_for_cooperation)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Cooperation-Company"
        verbose_name_plural = "Cooperation-Companies"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=CooperationCompanies)
        super(CooperationCompanies, self).save(*args, **kwargs)


class BlogModel(DateMixin, SlugMixin):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=Uploader.upload_images_for_blog)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Blog Model"
        verbose_name_plural = "Blog models"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=BlogModel)
        super(BlogModel, self).save(*args, **kwargs)

class Comment(MPTTModel, DateMixin, SlugMixin):
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE, null=True, blank=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='commentuser')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    body = models.TextField(null=True, blank=True)
    likers = models.ManyToManyField(User, default=None, blank=True, related_name='likers')

    def __str__(self):
        return self.restaurant.name

    def user_like_status(self, user):
        if Likes.objects.filter(user=user, comment=self).exists():
            return "Unlike"
        else:
            return "Like"

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    @property
    def num_likes(self):
        return self.likers.all().count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Comment)
        super(Comment, self).save(*args, **kwargs)




class Likes(DateMixin, SlugMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="comment_likes")
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return self.user.email

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Likes)
        super(Likes, self).save(*args, **kwargs)


class Rating(DateMixin, SlugMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE, related_name="restaurant")
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)

    def __str__(self):
        return f"{self.rate} --> ulduz --> {self.restaurant.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Rating)
        super(Rating, self).save(*args, **kwargs)


class Reserve(DateMixin, SlugMixin):
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    full_name = models.CharField(max_length=100, )
    count_of_guest = models.IntegerField(default=1)
    phone_number = models.TextField()
    passport_number = models.CharField(max_length=100)
    date = models.DateTimeField()
    notes = models.TextField()
    reserved = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Reserve"
        verbose_name_plural = "Reserves"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Reserve)

        super(Reserve, self).save(*args, **kwargs)


class Contact(DateMixin, SlugMixin):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} -->>> {self.subject}"

    class Meta:
        ordering = ("-created_at", )
        verbose_name = "Əlaqə yaratmaq istəyən şəxs"
        verbose_name_plural = "Əlaqə yaratmaq istəyən şəxslər"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Generator.create_slug_shortcode(size=15, model_=Contact)

        super(Contact, self).save(*args, **kwargs)

