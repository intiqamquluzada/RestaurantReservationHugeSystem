from django.urls import path
from .views import (home_view, about_view, list_view,
                    blog_view, contact_view, saved_restaurants,
                    reserved_view, restaurant_detail_view,
                    reserve_restaurant, menu_restaurant, like_and_unlike,
                    wishlist_create_view, reserve_delete_view, single_blog
                    )

app_name = "booking"

urlpatterns = [
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('restaurants/', list_view, name='list'),
    path('blog/', blog_view, name='blog'),
    path('blog/<slug>/', single_blog, name='singleBlog'),
    path('contact/', contact_view, name='contact'),
    path('saved/', saved_restaurants, name='saved'),
    path('reserved/', reserved_view, name='reserved'),
    path('reserve/delete/<slug>/', reserve_delete_view, name='deletereserve'),
    path('restaurant/detail/<slug>/', restaurant_detail_view, name='restaurant_detail'),
    path('reserve-restaurant/<slug>/', reserve_restaurant, name='reserve'),
    path('menu/<slug>/', menu_restaurant, name='menu'),
    path('like/', like_and_unlike, name='like'),
    path('create/wishlist/', wishlist_create_view, name='create-wishlist'),



]