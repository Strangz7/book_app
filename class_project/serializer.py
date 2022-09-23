from rest_framework import serializers

from class_project.models import Book, Publisher


# exclude = []


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'email', 'url']
        # field = '__all__'
        # exclude = []

class BookSerializer(serializers.ModelSerializer):  # noqa
    # book_title = serializers.CharField(max_length=255, source='title')
    # publisher = serializers.PrimaryKeyRelatedField(read_only=True)
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name='first_app:publisher-detail'
    # )

    class Meta:
        model = Book
        fields = ['title', 'description', 'isbn', 'price', 'publisher']
