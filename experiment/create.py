# create models and datasets

from lib.models import resnet50_base, resnet101_base
from lib.baselines import resnet50_orig, resnet101_orig
from lib.wildcat import resnet50_wildcat, resnet101_wildcat

from dataset.coco import CocoClassification
from dataset.nus_wide import NUSClassification
from dataset.wider import WiderClassification 
from dataset.voc import Voc2007Classification
from dataset.wish import Wish

model_factory = {
    'ours_50': resnet50_base,
    'ours_101': resnet101_base,
    'baseline_50': resnet50_orig,
    'baseline_101': resnet101_orig,
    'wildcat_50': resnet50_wildcat,
    'wildcat_101': resnet101_wildcat,
}

def create_model(name, *args, **kwargs):
    """
    Create a instance of network.
    Parameters
    ----------
    name : str
        the name of models
    """
    if name not in model_factory:
        raise KeyError("Unknown network:", name)
    return model_factory[name](*args, **kwargs)

dataset_factory = {
    'mscoco': CocoClassification,
    'nus-wide': NUSClassification,
    'wider': WiderClassification,
    'voc': Voc2007Classification,
    'wish': Wish
}

def create_dataset(name, *args, **kwargs):
    """
    Create a instance of dataset.
    Parameters
    ----------
    name : str
        the name of datasets
    """
    if name not in dataset_factory:
        raise KeyError("Unknown dataset:", name)
    return dataset_factory[name](*args, **kwargs)