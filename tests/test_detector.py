import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from detector import detect_fake_accounts


def test_detect_fake_accounts_not_implemented():
    with pytest.raises(NotImplementedError):
        detect_fake_accounts([])
