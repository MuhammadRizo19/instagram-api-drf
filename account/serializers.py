from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.serializers import EmailField, CharField	
from django.db.models import Q
from django.core.exceptions import ValidationError

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = [
            'username',
            'email',
            'last_name',
            'first_name' 
		]

class UserSerializer(serializers.ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')
    
    class Meta:
	    model = User
	    fields = [
	       'username',
	       'email',
	       'email2', 
	       'password'
	    ]
	    extra_kwargs = {'password': {'write_only': True}}
 
    def validate_email1(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise ValidationError('emails must match')
        return value    	
   

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise ValidationError('emails must match')
        return value    	
  
    def create(self, validated_data):
	    username = validated_data['username']
	    email = validated_data['email']	
	    password = validated_data['password']
	    user_obj = User(username=username, email=email)
	    user_obj.set_password(password)
	    user_obj.save()
	    return validated_data

class UserLoginSerializer(serializers.ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address', required=False,allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]
	
    def validate(self,data):
	    user_obj = None
	    email = data.get('email', None)
	    username = data.get('username', None)
	    password = data['password']
	    if not email and not username:
	        raise ValidationError('a username or email is required to login')

	    user = User.objects.filter(
	                  Q(email=email) |
	                  Q(username=username)  
	    ).distinct()
	    user = user.exclude(email__isnull=True).exclude(email__iexact='')
	    if user.exists() and user.count() == 1:
	        user_obj = user.first()
	    else:
	        raise ValidationError('username or email is not valid')

	    if user_obj:
	        if not user_obj.check_password(password):
	            raise ValidationError('incorrect credentials please try again')                                
	    data['token'] = 'SOME RANDOM TOKEN'
	    return data         