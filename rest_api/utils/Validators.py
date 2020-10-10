from rest_framework.validators import UniqueTogetherValidator


class BillingRecordSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        # Apply custom validation either here, or in the view.

    class Meta:
        fields = ['client', 'date', 'amount']
        extra_kwargs = {'client': {'required': False}}
        validators = []  # Remove a default "unique together" constraint.


class ExampleSerializer(serializers.Serializer):
    # ...
    class Meta:
        # ToDo items belong to a parent list, and have an ordering defined
        # by the 'position' field. No two items in a given list may share
        # the same position.
        validators = [
            UniqueTogetherValidator(
                queryset=ToDoItem.objects.all(),
                fields=['list', 'position']
            )
        ]
