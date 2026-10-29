from retinoblastoma_detection.data import DatasetSplits
from retinoblastoma_detection.testing import run_testing
from retinoblastoma_detection.training import run_training


class RecordingTrainingBackend:
    def fit(self, train_samples, validation_samples):
        assert train_samples == ("train sample",)
        assert validation_samples == ("validation sample",)
        return {"runs": 1.0}


class RecordingTestingBackend:
    def evaluate(self, test_samples):
        assert test_samples == ("test sample",)
        return {"example_metric": 0.5}


def test_training_receives_train_and_validation_splits():
    splits = DatasetSplits(
        train=("train sample",),
        validation=("validation sample",),
        test=("test sample",),
    )

    assert run_training(RecordingTrainingBackend(), splits) == {"runs": 1.0}


def test_testing_receives_only_the_held_out_test_split():
    splits = DatasetSplits(
        train=("train sample",),
        validation=("validation sample",),
        test=("test sample",),
    )

    assert run_testing(RecordingTestingBackend(), splits) == {"example_metric": 0.5}
