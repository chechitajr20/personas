# Crear el esquema de Ingredientes en cookbook/ingredients/schema.py
import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from people.models import Persona


# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 
class PersonaNode(DjangoObjectType):
    class Meta:
        model = Persona
        filter_fields = ['nombre', 'apellido', 'edad', 'telefono', 'email']
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    persona = relay.Node.Field(PersonaNode)
    all_personas = DjangoFilterConnectionField(PersonaNode)