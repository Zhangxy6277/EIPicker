from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .sample.ddd import DddDataset
from .sample.exdet import EXDetDataset
from .sample.ctdet import CTDetDataset
from .sample.multi_pose import MultiPoseDataset

from .dataset.coco import COCO
from .dataset.pascal import PascalVOC
from .dataset.kitti import KITTI
from .dataset.coco_hp import COCOHP
from .dataset.proteasome import PROTEASOME
from .dataset.proteasome_512 import PROTEASOME_512
from .dataset.GspDvc_1024 import GSPDVC_1024
from .dataset.TrpV1_1024 import TRPV1_1024
from .dataset.TandP_1024 import TandP_1024
from .dataset.EMPIAR_10017 import EMPIAR_10017
from .dataset.Pand10017 import Pand10017
from .dataset.Pand17and89and57 import Pand17and89and57
from .dataset.Tand10017 import Tand10017
from .dataset.E10058 import E10058
from .dataset.E10057 import E10057
from .dataset.E10089 import E10089
from .dataset.all6 import all6
from .dataset.Pand10089 import Pand10089
from .dataset.particle import Particle
dataset_factory = {
  'coco': COCO,
  'particle': Particle,
  'pascal': PascalVOC,
  'kitti': KITTI,
  'coco_hp': COCOHP,
  'proteasome': PROTEASOME,
  'proteasome_512': PROTEASOME_512,
  'GspDvc_1024': GSPDVC_1024,
  'TrpV1_1024': TRPV1_1024,
  'TandP': TandP_1024,
  'EMPIAR-10017':EMPIAR_10017,
  'Pand10017':Pand10017,
  'Tand10017': Tand10017,
  'E10057': E10057,
  'E10058': E10058,
  'E10089': E10089,
  'Pand17and89and57':Pand17and89and57,
  'Pand10089': Pand10089,
  'all6':all6
}

_sample_factory = {
  'exdet': EXDetDataset,
  'ctdet': CTDetDataset,
  'ddd': DddDataset,
  'multi_pose': MultiPoseDataset
}


def get_dataset(dataset, task):
  class Dataset(dataset_factory[dataset], _sample_factory[task]):
    pass
  return Dataset
  
