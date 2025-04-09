"""Test configuration for the Helmfile MCP server."""

import pytest
from unittest.mock import AsyncMock, patch

@pytest.fixture(autouse=True)
def mock_subprocess():
    """Mock subprocess calls for testing."""
    with patch('asyncio.create_subprocess_shell') as mock:
        yield mock

@pytest.fixture
def mock_process():
    """Create a mock process for testing."""
    process = AsyncMock()
    process.communicate.return_value = (b"mock output", b"")
    process.returncode = 0
    return process 