# 🛠️ openai-commands (`@openai`)

`@openai` is a command interface to the [OpenAI API](https://beta.openai.com/docs/introduction).

```bash
pip install openai-commands
```

```mermaid
graph LR
    openai_complete["@openai<br>complete<br>&lt;prompt&gt;"]

    openai_generate_image["@openai<br>generate_image<br>filename=&lt;filename.png&gt;<br>&lt;prompt&gt;<br>&lt;object-name&gt;"]

    litrev["@litrev<br>question=&lt;question&gt;<br>&lt;object-name&gt;"]
    litrev_multiple["@litrev<br>multiple<br>questions=&lt;question1+question2+...&gt;<br>to=&lt;runner&gt; -<br>&lt;object-name&gt;"]
    litrev_combine["@litrev<br>combine -<br>&lt;object-name-1&gt;<br>&lt;object-name-2&gt;<br>&lt;object-name&gt;"]

    text["📜 text"]:::folder
    image["🖼️ image"]:::folder
    object["object"]:::folder
    object_2["object 2"]:::folder
    object_3["object 3"]:::folder

    text --> openai_complete
    openai_complete --> text

    text --> openai_generate_image
    openai_generate_image --> image

    object --> litrev
    litrev --> object

    object --> litrev_combine
    object_2 --> litrev_combine
    litrev_combine --> object_3

    object --> litrev_multiple
    litrev_multiple --> object

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```


|   |   |
| --- | --- |
| [`literature review`](./openai_commands/literature_review) [![image](https://github.com/kamangir/assets/blob/main/openai_commands/literature-review/marquee.png?raw=true)](./openai_commands/literature_review)  | [`prompt completion`](./openai_commands/prompt_completion) [![image](https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true)](./openai_commands/prompt_completion)  |
| [`image generation`](./openai_commands/images) [![image](https://github.com/kamangir/openai-commands/blob/main/assets/DALL-E.png?raw=true)](./openai_commands/images)  | [`vision`](./openai_commands/vision) [![image](https://raw.githubusercontent.com/kamangir/assets/main/vanwatch/2023-11-25-openai-vision/ButeNorthDavie.jpg)](./openai_commands/vision)  |

---

🎁 [wish list and bugs](https://github.com/kamangir/openai-commands/issues/13)


[![pylint](https://github.com/kamangir/openai-commands/actions/workflows/pylint.yml/badge.svg)](https://github.com/kamangir/openai-commands/actions/workflows/pylint.yml) [![pytest](https://github.com/kamangir/openai-commands/actions/workflows/pytest.yml/badge.svg)](https://github.com/kamangir/openai-commands/actions/workflows/pytest.yml) [![bashtest](https://github.com/kamangir/openai-commands/actions/workflows/bashtest.yml/badge.svg)](https://github.com/kamangir/openai-commands/actions/workflows/bashtest.yml) [![PyPI version](https://img.shields.io/pypi/v/openai-commands.svg)](https://pypi.org/project/openai-commands/) [![PyPI - Downloads](https://img.shields.io/pypi/dd/openai-commands)](https://pypistats.org/packages/openai-commands)

built by 🌀 [`blue_options-4.201.1`](https://github.com/kamangir/awesome-bash-cli), based on [`openai_commands-3.227.1`](https://github.com/kamangir/openai-commands).
