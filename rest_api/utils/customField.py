class Color:
    """
    A color represented in the RGB colorspace.
    """

    def __init__(self, red, green, blue):
        assert(red >= 0 and green >= 0 and blue >= 0)
        assert(red < 256 and green < 256 and blue < 256)
        self.red, self.green, self.blue = red, green, blue


class ColorField(serializers.Field):
    """
    Color objects are serialized into 'rgb(#, #, #)' notation.
    """

    def to_representation(self, value):
        return "rgb(%d, %d, %d)" % (value.red, value.green, value.blue)

    # 1.
    def to_internal_value(self, data):
        data = data.strip('rgb(').rstrip(')')
        red, green, blue = [int(col) for col in data.split(',')]
        return Color(red, green, blue)

    # 2.
    # def to_internal_value(self, data):
    # if not isinstance(data, str):
    #    msg = 'Incorrect type. Expected a string, but got %s'
    #    raise ValidationError(msg % type(data).__name__)

    # if not re.match(r'^rgb\([0-9]+,[0-9]+,[0-9]+\)$', data):
    #    raise ValidationError('Incorrect format. Expected `rgb(#,#,#)`.')

    #data = data.strip('rgb(').rstrip(')')
    #red, green, blue = [int(col) for col in data.split(',')]

    # if any([col > 255 or col < 0 for col in (red, green, blue)]):
    #    raise ValidationError('Value out of range. Must be between 0 and 255.')

    # return Color(red, green, blue)

    # 3.
    # default_error_messages = {
    #    'incorrect_type': 'Incorrect type. Expected a string, but got {input_type}',
    #    'incorrect_format': 'Incorrect format. Expected `rgb(#,#,#)`.',
    #    'out_of_range': 'Value out of range. Must be between 0 and 255.'
    # }

    # def to_internal_value(self, data):
    #    if not isinstance(data, str):
    #        self.fail('incorrect_type', input_type=type(data).__name__)

    #    if not re.match(r'^rgb\([0-9]+,[0-9]+,[0-9]+\)$', data):
    #        self.fail('incorrect_format')

    #    data = data.strip('rgb(').rstrip(')')
    #    red, green, blue = [int(col) for col in data.split(',')]

    #    if any([col > 255 or col < 0 for col in (red, green, blue)]):
    #        self.fail('out_of_range')

    #    return Color(red, green, blue)


class DataPoint(models.Model):
    label = models.CharField(max_length=50)
    x_coordinate = models.SmallIntegerField()
    y_coordinate = models.SmallIntegerField()


class CoordinateField(serializers.Field):

    def to_representation(self, value):
        ret = {
            "x": value.x_coordinate,
            "y": value.y_coordinate
        }
        return ret

    def to_internal_value(self, data):
        ret = {
            "x_coordinate": data["x"],
            "y_coordinate": data["y"],
        }
        return ret


class DataPointSerializer(serializers.ModelSerializer):
    coordinates = CoordinateField(source='*')

    class Meta:
        model = DataPoint
        fields = ['label', 'coordinates']
