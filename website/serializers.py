from rest_framework import serializers
from .models import Website, portfolio, Blog


class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Website
        fields = (
            'website', 'name', 'designation', 'country', 'email', 'phone', 'description', 'facebook', 'twitter',
            'clients',
            'projects', 'coffee', 'design', 'strategy', 'code',
            'instagram', 'dribble', 'logo', 'aboutimg', 'navbarimg')


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    website = WebsiteSerializer()

    class Meta:
        model = portfolio
        fields = ('website', 'category', 'title', 'description', 'image')


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    website = WebsiteSerializer()

    class Meta:
        model = Blog
        fields = ('website', 'title', 'description', 'image', 'created_at')
