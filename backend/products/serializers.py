from rest_framework import serializers

from . import models


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Picture
        fields = ('id', 'product', 'image')


class ConcisePictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Picture
        fields = ('id', 'image')

class ProductSerializer(serializers.ModelSerializer):

    images = ConcisePictureSerializer(many=True)
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'price', 'description', 'stock_count', 'images')
        # fields = '__all__' - anti practice
        # exclude = ('id',)

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        product = models.Product.objects.create(**validated_data)
        for image_data in images_data:
            models.Picture.objects.create(product=product, **image_data)
        return product
