# Crear el esquema de Ingredientes en cookbook/ingredients/schema.py
import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from people.models import Persona

class PersonaType(DjangoObjectType):
    class Meta:
        model = Persona

class Query(ObjectType):
    persona = graphene.Field(PersonaType, id=graphene.Int())
    personas = graphene.List(PersonaType)

    def resolve_persona(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Persona.objects.get(pk=id)

        return None
    
    def resolve_personas(self, info, **kwargs):
        return Persona.objects.all()

class PersonaInput(graphene.InputObjectType):
    id = graphene.ID()
    nombre = graphene.String()
    apellido = graphene.String()
    edad = graphene.String()
    telefono = graphene.String()
    email = graphene.String()

class CreatePersona(graphene.Mutation):
    class Arguments:
        input = PersonaInput(required=True)

    ok = graphene.Boolean()
    persona = graphene.Field(PersonaType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        persona_instance = Persona(nombre=input.nombre, apellido=input.apellido, edad=input.edad, telefono=input.telefono, email=input.email)
        persona_instance.save()
        return CreatePersona (ok=ok, persona=persona_instance)
    
class UpdatePersona(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PersonaInput(required=True)

    ok = graphene.Boolean()
    persona = graphene.Field(PersonaType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        persona_instance = Persona.objects.get(pk=id)
        if persona_instance:
            ok = True
            persona_instance.nombre = input.nombre
            persona_instance.apellido = input.apellido
            persona_instance.edad = input.edad
            persona_instance.telefono = input.telefono
            persona_instance.email = input.email
            persona_instance.save()
            return UpdatePersona(ok=ok, persona=persona_instance)
        return UpdatePersona(ok=ok, persona=None)

class Mutation(graphene.ObjectType):
    create_persona = CreatePersona.Field()
    update_persona = UpdatePersona.Field()

schema = graphene.Schema(query = Query, mutation = Mutation)