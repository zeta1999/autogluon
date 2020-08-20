import logging

from pandas import DataFrame

from .identity import IdentityFeatureGenerator
from ..feature_metadata import FeatureMetadata

logger = logging.getLogger(__name__)


class DummyFeatureGenerator(IdentityFeatureGenerator):
    def __init__(self, features_in='empty', feature_metadata_in='empty', **kwargs):
        if features_in == 'empty':
            features_in = []
        if feature_metadata_in == 'empty':
            feature_metadata_in = FeatureMetadata(type_map_raw={})
        super().__init__(features_in=features_in, feature_metadata_in=feature_metadata_in, **kwargs)

    def _transform(self, X: DataFrame) -> DataFrame:
        return self._generate_features_dummy(X)

    @staticmethod
    def get_default_infer_features_in_args() -> dict:
        return dict(valid_raw_types=[])

    @staticmethod
    def _generate_features_dummy(X: DataFrame):
        X_out = DataFrame(index=X.index)
        X_out['__dummy__'] = 0
        return X_out
