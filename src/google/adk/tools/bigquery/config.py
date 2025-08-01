# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel

from ...utils.feature_decorator import experimental


class WriteMode(Enum):
  """Write mode indicating what levels of write operations are allowed in BigQuery."""

  BLOCKED = 'blocked'
  """No write operations are allowed.

  This mode implies that only read (i.e. SELECT query) operations are allowed.
  """

  PROTECTED = 'protected'
  """Only protected write operations are allowed in a BigQuery session.

  In this mode write operations in the anonymous dataset of a BigQuery session
  are allowed. For example, a temporaray table can be created, manipulated and
  deleted in the anonymous dataset during Agent interaction, while protecting
  permanent tables from being modified or deleted. To learn more about BigQuery
  sessions, see https://cloud.google.com/bigquery/docs/sessions-intro.
  """

  ALLOWED = 'allowed'
  """All write operations are allowed."""


@experimental('Config defaults may have breaking change in the future.')
class BigQueryToolConfig(BaseModel):
  """Configuration for BigQuery tools."""

  write_mode: WriteMode = WriteMode.BLOCKED
  """Write mode for BigQuery tools.

  By default, the tool will allow only read operations. This behaviour may
  change in future versions.
  """

  max_query_result_rows: int = 50
  """Maximum number of rows to return from a query.

  By default, the query result will be limited to 50 rows."""
