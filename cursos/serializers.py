from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

  class Meta:
    extra_kwargs = {
      'email': {'write_only': True}
    }
    model = Avaliacao
    fields = (
      'id',
      'curso',
      'nome', 
      'email',
      'comentario',
      'avaliacao',
      'criacao',
      'ativo'
    )


class CursoSerializer(serializers.ModelSerializer):
  # abordagem 1
  # Nested relationship
  # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

  # abordagem 2
  # hyperlinked related field
  # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

  # abordagem 3
  # Primary key related field
  avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = Curso
    fields = (
      'id',
      'titulo',
      'url',
      'criacao',
      'ativo',
      'avaliacoes'
    )