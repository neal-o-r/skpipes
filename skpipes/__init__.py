from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import TransformerMixin

def pipe_rshift(self, rhs):

    lhs_pipe = self.steps
    rhs_pipe = (rhs.__str__().split('(')[0], rhs)

    pipe = lhs_pipe + [rhs_pipe]
    return Pipeline(pipe)

def transformer_rshift(self, rhs):

    lhs_pipe = [self.__str__().split('(')[0], self]
    rhs_pipe = [rhs.__str__().split('(')[0], rhs]

    pipe = [tuple(lhs_pipe), tuple(rhs_pipe)]
    return Pipeline(pipe)


def transformer_add(self, rhs):

    lhs_pipe = [self.__str__().split('(')[0], self]
    rhs_pipe = [rhs.__str__().split('(')[0], rhs]

    pipe = [tuple(lhs_pipe), tuple(rhs_pipe)]
    return FeatureUnion(pipe)


def pipe_add(self, rhs):

    lhs_pipe = self.steps
    rhs_pipe = (rhs.__str__().split('(')[0], rhs)

    pipe = lhs_pipe + [rhs_pipe]
    return FeatureUnion(pipe)


Pipeline.__rshift__ = pipe_rshift
Pipeline.__add__ = pipe_add
TransformerMixin.__rshift__ = transformer_rshift
TransformerMixin.__add__ = transformer_add
