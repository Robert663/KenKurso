from rest_framework import serializers
from .models import School_Record


class SchoolRecordSerializers(serializers.ModelSerializer):

    class Meta:
        model = School_Record
        fields = "__all__"
        read_only_fields = ["id"]
