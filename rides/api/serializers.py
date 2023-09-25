from accounts.models import Profile
from rides.models import Ride
from django.contrib.auth.models import User
from rest_framework import serializers


class CarregaDadosPassageirosSerializer(serializers.ModelSerializer):
    class Meta:
        nome_usuario = serializers.SerializerMethodField()
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email']

        def get_nome_usuario(self, obj):
            return obj.nome.username


class ProfileSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only = True)
    
    class Meta:
        model = Profile
        fields = '__all__'
        
        def save_senha(self,validated_data):
            # Extraia a senha do payload validado
            senha = validated_data.pop('senha', None)
            
             # Crie um novo usuário com os outros dados fornecidos
            user = User(**validated_data)

        # Use set_senha para criptografar e definir a senha
            if senha is not None:
                user.set_senha(senha)

        # Salve a senha no  banco de dados
            user.save()
            return user


class RidesSerializer(serializers.ModelSerializer):
    passageiros = CarregaDadosPassageirosSerializer(many=True, required=False)
    # passageiros_id = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all(),source='passageiros')

    class Meta:
        model = Ride
        fields = '__all__'

    def update(self, instance, validated_data):
        passageiros = validated_data.pop('passageiros')
        instance = super(RidesSerializer, self).update(
            instance, validated_data)
        instance.passageiros.clear()
        for passageiro in passageiros:
            instance.passageiros.add(passageiro)
            return instance

    def get_nome_passageiros(self, obj):
        return obj.nome.passageiros
