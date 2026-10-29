"""Model-independent training workflow contract."""

from collections.abc import Mapping, Sequence
from typing import Protocol, TypeVar

from retinoblastoma_detection.data import DatasetSplits

SampleT = TypeVar("SampleT")


class TrainingBackend(Protocol[SampleT]):
    """Interface a future framework-specific trainer can implement."""

    def fit(
        self,
        train_samples: Sequence[SampleT],
        validation_samples: Sequence[SampleT],
    ) -> Mapping[str, float]:
        """Fit on training samples and return optional numeric run summaries."""
        ...


def run_training(
    backend: TrainingBackend[SampleT],
    splits: DatasetSplits[SampleT],
) -> Mapping[str, float]:
    """Forward the training and validation splits to a selected backend."""
    return backend.fit(splits.train, splits.validation)
