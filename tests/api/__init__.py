# -*- coding: utf-8 -*-
#
# Copyright 2019 Ricequant, Inc
#
# * Commercial Usage: please contact public@ricequant.com
# * Non-Commercial Usage:
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from .test_api_base import test_strategies as test_api_base_strategies
from .test_api_stock import test_strategies as test_api_stock_strategies
from .test_api_future import test_strategies as test_api_future_strategies
from .test_config import test_strategies as test_config_strategies

test_strategies = test_api_base_strategies + test_api_stock_strategies + test_api_future_strategies + test_config_strategies

__all__ = [
    "test_strategies"
]
