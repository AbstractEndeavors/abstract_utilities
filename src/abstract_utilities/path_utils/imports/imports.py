from pathlib import Path
from typing import *
import fnmatch, glob,os,platform,inspect
from ...read_write_utils import read_from_file
from ...string_clean import eatAll
from ...list_utils import make_list
from ...type_utils import get_media_exts, is_media_type
from dataclasses import dataclass, field
