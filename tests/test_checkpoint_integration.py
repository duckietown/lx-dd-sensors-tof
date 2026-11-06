"""Exercise actual notebook identities and their integrated checkpoint data."""

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from packages import checkpoint_self_check as helper

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((ROOT / "notebooks").glob("*.ipynb"))


@pytest.mark.parametrize("notebook_path", NOTEBOOKS, ids=lambda p: p.stem)
def test_notebook_identity_loads_and_reveals_answers(notebook_path):
    class Kernel:
        def get_parent(self):
            return {
                "metadata": {
                    "cellId": (
                        "vscode-notebook-cell://workspace/notebooks/"
                        f"{notebook_path.name}#checkpoint"
                    ),
                },
            }

    class Shell:
        kernel = Kernel()

    with (
        patch.object(helper, "get_ipython", return_value=Shell()),
        patch.object(helper, "display") as display,
    ):
        name = helper.get_checkpoint_name_from_notebook_context()
        helper.display_checkpoint_self_checks()
        assert display.called
        assert "unavailable" not in str(display.call_args_list).lower()

    path = ROOT / "checkpoint_data" / f"{name}.json"
    definitions = helper.load_checkpoint_definitions(path)
    data = json.loads(path.read_text())
    assert len(definitions) == len(data["checkpoints"])
    for number, (question, identifier, choices) in enumerate(definitions, 1):
        widget = helper.CheckpointSelfCheck(
            number, question, identifier, path, len(definitions), choices,
        )
        assert widget.reveal_button.disabled
        assert widget.text_answer is not None
        widget.text_answer.value = "An experimental response."
        assert not widget.reveal_button.disabled
        widget.reveal_button.click()
        assert widget.model_answer.value
        assert widget.model_answer.layout.display != "none"
        assert "unavailable" not in widget.status.value.lower()
        widget.retry_button.click()
        assert not widget.model_answer.value
        assert widget.reveal_button.disabled
