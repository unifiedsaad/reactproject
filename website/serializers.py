from rest_framework import serializers
from .models import Website


class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Website
        fields = ('website', 'name', 'designation', 'country', 'email', 'phone', 'description', 'facebook', 'twitter',
                  'instagram', 'dribble', 'logo', 'aboutimg')
