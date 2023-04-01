from rest_framework import serializers

from ads.models import Ad, Comment


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name",
                  "author_id"]

    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    phone = serializers.CharField(source="author.phone", required=False)


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name",
                  "author_id"]

    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    phone = serializers.CharField(source="author.phone", required=False)
    author_id = serializers.IntegerField()


class AdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name",
                  "author_id"]

    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    phone = serializers.CharField(source="author.phone", required=False)
    author_id = serializers.IntegerField(read_only=True)

#comments serializers


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", required=False)
    author_last_name = serializers.CharField(source="author.last_name", required=False)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["author_id"] = request.user
        return super().create(validated_data)

    class Meta:
        model = Comment
        fields = "__all__"





