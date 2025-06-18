from django import forms
from django.db.models import Field


# https://docs.djangoproject.com/en/5.0/howto/custom-model-fields/
class VectorField(Field):
    description = 'Vector'
    empty_strings_allowed = False

    def __init__(self, *args, dimensions=None, **kwargs):
        self.dimensions = dimensions
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.dimensions is not None:
            kwargs['dimensions'] = self.dimensions
        return name, path, args, kwargs

    def db_type(self, connection):
        if self.dimensions is None:
            return 'vector'
        return 'vector(%d)' % self.dimensions

    def from_db_value(self, value, expression, connection):
        return None

    def to_python(self, value):
        if isinstance(value, list):
            raise NotImplementedError("Not implemented. Use full pgvector library instead.")
        return None

    def get_prep_value(self, value):
        return None

    def value_to_string(self, obj):
        return self.get_prep_value(self.value_from_object(obj))

    def validate(self, value, model_instance):
        if isinstance(value, list):
            raise NotImplementedError("Not implemented. Use full pgvector library instead.")
        super().validate(value, model_instance)

    def run_validators(self, value):
        if isinstance(value, list):
            raise NotImplementedError("Not implemented. Use full pgvector library instead.")
        super().run_validators(value)

    def formfield(self, **kwargs):
        return super().formfield(form_class=VectorFormField, **kwargs)


class VectorWidget(forms.TextInput):
    def format_value(self, value):
        if isinstance(value, list):
            raise NotImplementedError("Not implemented. Use full pgvector library instead.")
        return super().format_value(value)


class VectorFormField(forms.CharField):
    widget = VectorWidget

    def has_changed(self, initial, data):
        if isinstance(initial, list):
            raise NotImplementedError("Not implemented. Use full pgvector library instead.")
        return super().has_changed(initial, data)

    def to_python(self, value):
        if isinstance(value, str) and value == '':
            return None
        return super().to_python(value)
