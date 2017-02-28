from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        self.flatten = kwargs.pop('flatten', False)
        fields = kwargs.pop('fields', None)
        added = kwargs.pop('explicitly_included_fields', None)
        self.show_all = kwargs.pop('show_all', False)

        if not hasattr(self, 'optional_fields'):
            self.optional_fields = []

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        elif self.optional_fields and not self.show_all:
            for field_name in set(self.optional_fields) - set(added or []):
                self.fields.pop(field_name)

    def get_fields(self):
        fields = super(DynamicFieldsModelSerializer, self).get_fields()
        for field_name, field in fields.items():
            if getattr(field, 'flatten', False):
                del fields[field_name]
                for nested_field_name, nested_field in field.fields.iteritems():
                    nested_field.source = (field_name + '.' +
                                           (nested_field.source or nested_field_name))
                    nested_field_name = field_name.split('_')[0] +'_'+nested_field_name # this is kinda hacky may not be what we want...
                    fields[nested_field_name] = nested_field

        return fields

class DynamicFieldsSerializer(serializers.Serializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        self.flatten = kwargs.pop('flatten', False)
        fields = kwargs.pop('fields', None)
        added = kwargs.pop('explicitly_included_fields', None)
        self.show_all = kwargs.pop('show_all', False)

        if not hasattr(self, 'optional_fields'):
            self.optional_fields = []

        # Instantiate the superclass normally
        super(DynamicFieldsSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        elif self.optional_fields and self.show_all:
            for field_name in set(self.optional_fields) - set(added or []):
                self.fields.pop(field_name)

    def get_fields(self):
        fields = super(DynamicFieldsSerializer, self).get_fields()
        for field_name, field in fields.items():
            if getattr(field, 'flatten', False):
                del fields[field_name]
                for nested_field_name, nested_field in field.fields.iteritems():
                    nested_field.source = (field_name + '.' +
                                           (nested_field.source or nested_field_name))
                    nested_field_name = field_name.split('_')[
                                            0] + '_' + nested_field_name  # this is kinda hacky may not be what we want...
                    fields[nested_field_name] = nested_field
        return fields

class DynamicField(RecursiveField):
    pass
