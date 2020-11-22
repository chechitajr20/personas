import graphene

import people.schema


class Query(people.schema.Query, graphene.ObjectType):
    """
    docstring
    """
    pass

class Mutation(people.schema.Mutation, graphene.ObjectType):
    """
    docstring
    """
    pass
schema = graphene.Schema(query=Query, mutation = Mutation)