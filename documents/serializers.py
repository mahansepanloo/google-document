from rest_framework import serializers
from .models import DocumentModel




class DocSerializers(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = "__all__"




class CreateDocSerializers(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = ['title']

    # def validate_name(self, value):
    #     doc = DocumentModel.objects.filter(name=value)
    #     if doc.exists():
    #         raise serializers.ValidationError('نام تکراری است')
    #     return value



    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if instance.file:
    #         representation['content'] = instance.file.read().decode('utf-8')
    #         instance.file.seek(0)
    #     return representation


class CreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = ['document','title']