import os
from tempfile import TemporaryDirectory

from mcp.types import Tool

from agent_scan.Storage import Storage


def test_scanned_entities_are_persisted():
    with TemporaryDirectory() as tempdir:
        path = os.path.join(tempdir, "storage.json")
        storage_file = Storage(path)

        storage_file.check_and_update(
            "demo-server",
            Tool(name="test-tool", description="test description", inputSchema={"type": "object"}),
        )
        storage_file.save()

        # test reload
        storage_file = Storage(path)
        assert len(storage_file.scanned_entities.root) == 1
        assert "demo-server.tool.test-tool" in storage_file.scanned_entities.root
