"""Model-independent held-out testing workflow contract."""

from collections.abc import Mapping, Sequence
from typing import Protocol, TypeVar

from retinoblastoma_detection.data import DatasetSplits

SampleT = TypeVar("SampleT")


class TestingBackend(Protocol[SampleT]):
    """Interface a future framework-specific evaluator can implement."""

    def evaluate(self, test_samples: Sequence[SampleT]) -> Mapping[str, float]:
        """Evaluate held-out samples and return numeric metrics."""
        ...


def run_testing(
    backend: TestingBackend[SampleT],
    splits: DatasetSplits[SampleT],
) -> Mapping[str, float]:
    """Forward only the held-out test split to a selected backend."""
    return backend.evaluate(splits.test)
