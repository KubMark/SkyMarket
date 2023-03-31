from rest_framework import serializers

from ads.models import Ad


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"

    author_first_name = serializers.CharField(source="author.first_name")
    author_last_name = serializers.CharField(source="author.last_name")

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author_id"] = request.user.pk
        return super().create(validated_data)


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name", "author_id"]

    author_first_name = serializers.CharField(source="author.first_name")
    author_last_name = serializers.CharField(source="author.last_name")
    phone = serializers.CharField(source="author.phone", required=False)
