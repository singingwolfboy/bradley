import graphene
from bradley.schema.mutation.auth import Login, Register, RefreshToken
from bradley.schema.mutation.contacts import (
    CreateContact, MutateContact, DestroyContact
)
from bradley.schema.mutation.tag import (
    CreateTag, MutateTag, DestroyTag
)


class Mutation(graphene.ObjectType):
    login = Login.Field()
    register = Register.Field()
    refresh_token = RefreshToken.Field()
    create_contact = CreateContact.Field()
    mutate_contact = MutateContact.Field()
    destroy_contact = DestroyContact.Field()
    create_tag = CreateTag.Field()
    mutate_tag = MutateTag.Field()
    destroy_tag = DestroyTag.Field()
