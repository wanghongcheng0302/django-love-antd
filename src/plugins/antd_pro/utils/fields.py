def get_field_by_entity(entity, field_name):
    model = entity.__class__
    try:
        return getattr(model, field_name).field
    except AttributeError:
        pass
