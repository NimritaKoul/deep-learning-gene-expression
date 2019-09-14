import logging
import pandas as pd
import time

from selection import correlation_with_class, fisher, ttest, random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

features_methods = {
    'fisher': fisher,
    'corr': correlation_with_class,
    'ttest': ttest,
    'random': random
}


def execute_selection(selection_methods: list(), data: pd.DataFrame, num_features=100, force=True):
    selected_features = dict()
    for selection_method in selection_methods:
        start = time.time()
        logger.info('Making feature selection with [%s] method...', selection_method)
        selected_features[selection_method] = features_methods[selection_method].select(data, num_features=num_features, force=force)
        totalTime = (time.time() - start) * 1000
        logger.info('[%s] feature selection last %d ms.', selection_method, totalTime)
    return selected_features


def apply_selection(selection_method: str, data: pd.DataFrame, num_features=100):
    selected_features = features_methods[selection_method].select(data, num_features=num_features, force=False)
    return selected_features
