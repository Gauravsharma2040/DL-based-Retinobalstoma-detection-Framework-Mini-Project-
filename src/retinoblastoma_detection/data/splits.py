"""Model-independent container for supervised-learning data splits."""

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Generic, TypeVar

SampleT = TypeVar("SampleT")


@dataclass(frozen=True)
class DatasetSplits(Generic[SampleT]):
    """Samples for fitting, validation, and held-out testing."""

    train: Sequence[SampleT]
    validation: Sequence[SampleT]
    test: Sequence[SampleT]
