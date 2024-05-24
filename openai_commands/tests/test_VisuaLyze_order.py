import pytest
from openai_commands import env
from openai_commands.VisuaLyze.order import VisuaLyzeOrder


@pytest.mark.parametrize(
    ["example_name", "model_name"],
    [
        ["onlinefoods", env.OPENAI_GPT_DEFAULT_MODEL],
    ],
)
def test_VisuaLyze_order(
    example_name: str,
    model_name: str,
):
    order = VisuaLyzeOrder(example_name=example_name)

    assert order.prompt
    assert order.description
    assert order.data_filename
    assert len(order.df)
    assert order.valid

    assert order.complete(model_name=model_name)

    assert order.valid
    assert order.source_code
