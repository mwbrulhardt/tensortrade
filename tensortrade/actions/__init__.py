from .action_strategy import ActionStrategy, DTypeString, TradeActionUnion
from .continuous_action_strategy import ContinuousActionStrategy
from .discrete_action_strategy import DiscreteActionStrategy


_registry = {
    'continuous': ContinuousActionStrategy(),
    'discrete': DiscreteActionStrategy()
}


def get(identifier: str) -> ActionStrategy:
    """Gets the `ActionStrategy` that matches with the identifier.

    Arguments:
        identifier: The identifier for the `ActionStrategy`

    Raises:
        KeyError: if identifier is not associated with any `ActionStrategy`
    """
    if identifier not in _registry.keys():
        raise KeyError(f'Identifier {identifier} is not associated with any `ActionStrategy`.')
    return _registry[identifier]
