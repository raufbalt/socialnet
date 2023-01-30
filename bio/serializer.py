from rest_framework import serializers

from bio.models import Biography


class BiographySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Biography
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        try:
            if instance.owner.username == 'rauf':
                rep['status'] = 'Admin'
        except AttributeError:
            rep['status'] = 'Basic user'
            return rep
        return rep