# 🛠️ openai-commands (`@openai`)

`@openai` is a command interface to the [OpenAI API](https://beta.openai.com/docs/introduction).

```bash
pip install openai-commands
```

```mermaid
graph LR
    complete["@openai complete <prompt>"]
    generate_image["@openai generate_image filename=<filename.png> <prompt> <object-name>"]

    text["📜 text"]:::folder
    image["🖼️ image"]:::folder

    text --> complete
    complete --> text

    text --> generate_image
    generate_image --> image

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```


--table--

---

🎁 [wish list and bugs](https://github.com/kamangir/openai-commands/issues/13)

--signature--