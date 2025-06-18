from django.db.models import FloatField, Func, Value


class DistanceBase(Func):
    output_field = FloatField()

    def __init__(self, expression, vector, **extra):
        if not hasattr(vector, 'resolve_expression'):
            raise NotImplementedError("Not implemented. Use full pgvector library instead.")
            
        super().__init__(expression, vector, **extra)


class BitDistanceBase(Func):
    output_field = FloatField()

    def __init__(self, expression, vector, **extra):
        if not hasattr(vector, 'resolve_expression'):
            vector = Value(vector)
        super().__init__(expression, vector, **extra)


class L2Distance(DistanceBase):
    function = ''
    arg_joiner = ' <-> '


class MaxInnerProduct(DistanceBase):
    function = ''
    arg_joiner = ' <#> '


class CosineDistance(DistanceBase):
    function = ''
    arg_joiner = ' <=> '


class L1Distance(DistanceBase):
    function = ''
    arg_joiner = ' <+> '


class HammingDistance(BitDistanceBase):
    function = ''
    arg_joiner = ' <~> '


class JaccardDistance(BitDistanceBase):
    function = ''
    arg_joiner = ' <%%> '
