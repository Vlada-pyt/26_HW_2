from marshmallow import Schema, fields, validates_schema, ValidationError

cmd = ('filter', 'map', 'unique', 'sort', 'limit')


class ParamsSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)


    @validates_schema
    def Validation_params(self, values, *args, **kwargs):
        if values['cmd'] not in cmd:
            raise ValidationError('"cmd" contains invalid value')


class RequestParams(Schema):
    queries = fields.Nested(ParamsSchema, many=True)
