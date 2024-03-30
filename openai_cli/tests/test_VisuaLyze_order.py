import pytest
from abcli.plugins.testing import download_object
from openai_cli.VisuaLyze.order import VisuaLyzeOrder
from openai_cli.env import OPENAI_CLI_VISUALIZE_EXAMPLES_OBJECT


@pytest.mark.parametrize(
    ["order_name"],
    [
        ["onlinefoods"],
    ],
)
def test_VisuaLyze_order(order_name: str):
    assert download_object(OPENAI_CLI_VISUALIZE_EXAMPLES_OBJECT)

    order = VisuaLyzeOrder(name=order_name)

    assert order.prompt
    assert order.description
    assert order.data_filename
    assert len(order.df)
    assert order.valid
