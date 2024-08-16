from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from product.models import Product, Review  # Import the Product and Review models


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        user = self.user  # Get the authenticated user
        
        # Fetch a product created by the user (if any)
        product = Product.objects.filter(user=user).first()
        
        # Fetch a review made by the user (if any)
        review = Review.objects.filter(user=user).first()
        
        # Update the token response with additional data
        data.update({
            'user_id': user.id,
            'username': user.username,
            'product_id': product.id if product else None,
            'product_name': product.name if product else None,
            'review_id': review.id if review else None,
            'review_comment': review.comment if review else None,
        })

        return data
    
    
class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'password')

        extra_kwargs = {
            'first_name': {'required':True ,'allow_blank':False},
            'last_name' : {'required':True ,'allow_blank':False},
            'email' : {'required':True ,'allow_blank':False},
            'password' : {'required':True ,'allow_blank':False,'min_length':8}
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'username') 