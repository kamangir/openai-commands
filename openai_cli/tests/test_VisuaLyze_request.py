import pytest
from openai_cli.VisuaLyze.order import VisuaLyzeOrder


@pytest.mark.parametrize(
    ["order_name"],
    [
        ["onlinefoods"],
    ],
)
def test_VisuaLyze_request(order_name: str):
    order = VisuaLyzeOrder(
        name=order_name,
        load=True,
    )

    assert order.prompt
    assert order.description
    assert order.data_filename
    assert len(order.df)
    assert order.valid
