from rest_framework import serializers

from myApp.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'email', 'url']


class BookSerializer(serializers.ModelSerializer):
    # publisher = PublisherSerializer()
    # publisher = serializers.HyperlinkedRelatedField(
    #     # to implement HATEOAS: such that we give the user together with the link to avoid much query calls
    #     queryset=Publisher.objects.all(),
    #     view_name='myApp:publisher-details'
    # )
    publisher = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'description', 'isbn', 'price', 'date_published', 'publisher']  # or "__all__"
