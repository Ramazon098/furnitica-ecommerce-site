import os

from django.core.exceptions import ValidationError


# Create your validators here.

def validate_image_extension(value):
    extensions = os.path.splitext(value.name)[1]
    validate_extensions = ['.jpg', '.png', '.jpeg', '.gif', '.raw']

    if not extensions.lower() in validate_extensions:
        raise ValidationError({
            'extension_error': 'You can only upload images here.',
        })
