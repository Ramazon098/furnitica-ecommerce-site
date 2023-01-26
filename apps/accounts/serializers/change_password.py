from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers


# Create your serializers here.

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        validators=[validate_password],
    )

    new_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        validators=[validate_password],
    )

    confirm_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        validators=[validate_password],
    )

    class Meta:
        fields = [
            'ol_password',
            'new_password',
            'confirm_password',
        ]

    def validate_old_password(self, value):
        user = self.context['request'].user

        if not user.check_password(value):
            raise serializers.ValidationError({
                "password_error": "Your old password was entered incorrectly. Please enter it again.",
            })

        return value

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                "password_error": "New password fields didn't match.",
            })

        return attrs

    def save(self, **kwargs):
        password = self.validated_data['new_password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()

        return user
