import graphene
import json

class Query(graphene.ObjectType):
    is_staff = graphene.Boolean()

    def resolve_is_stuff(self, info):
        return True


schema = graphene.Schema(query=Query)

results = schema.execute(
        '''
        {
            isStaff
        }
        '''
)

print(results.data.items())


