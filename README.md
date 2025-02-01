# 🛠️ openai-commands (`@openai`)

`@openai` is a command interface to the [OpenAI API](https://beta.openai.com/docs/introduction).

```bash
pip install openai-commands
```

```mermaid
graph LR
    complete["@openai<br>complete<br>&lt;prompt&gt;"]

    text["📜 text"]:::folder

    text --> complete
    complete --> text

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```


|   |   |   |
| --- | --- | --- |
| [`prompt completion`](./openai_commands/completion#%EF%B8%8F-prompt-completion) [![image](https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true)](./openai_commands/completion#%EF%B8%8F-prompt-completion)  | [`vision`](./openai_commands/vision) [![image](https://raw.githubusercontent.com/kamangir/assets/main/vanwatch/2023-11-25-openai-vision/ButeNorthDavie.jpg)](./openai_commands/vision) a command interface to the [OpenAI vision API](https://platform.openai.com/docs/guides/vision). | [`literature review`](./openai_commands/literature_review) [![image](https://github.com/kamangir/assets/blob/main/openai_commands/literature-review/marquee.png?raw=true)](./openai_commands/literature_review) literature review using OpenAI API. |
| [`code generation`](./openai_commands/completion#%EF%B8%8F-code-generation) [![image](https://github.com/kamangir/openai-commands/blob/main/assets/completion_i2i_function.png?raw=true)](./openai_commands/completion#%EF%B8%8F-code-generation) example notebooks to [generate python functions](./notebooks/completion_ai_function_py.ipynb), special case for [image to image python functions](./notebooks/completion_i2i_function.ipynb), and to [write a bash script](./notebooks/completion_ai_function_bash.ipynb) to use a script, for example, [vancouver-watching](https://github.com/kamangir/vancouver-watching). | [`image generation`](./openai_commands/images) [![image](https://github.com/kamangir/openai-commands/blob/main/assets/DALL-E.png?raw=true)](./openai_commands/images) sentence -> image, text -> mural, images |  |

---

🎁 [wish list and bugs](https://github.com/kamangir/openai-commands/issues/13)


[![pylint](https://github.com/kamangir/openai-commands/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/openai-commands/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/openai-commands/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/openai-commands/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/openai-commands/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/openai-commands/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/openai-commands.svg)](https://pypi.org/project/openai-commands/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/openai-commands)](https://pypistats.org/packages/openai-commands)

built by 🌀 [`blue_options-4.200.1`](https://github.com/kamangir/awesome-bash-cli), based on [`openai_commands-3.212.1`](https://github.com/kamangir/openai-commands).
