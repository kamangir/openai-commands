# openai

`openai` is a bash cli for [OpenAI API](https://beta.openai.com/docs/introduction).

## Install

Install [`awesome-bash-cli`](https://github.com/kamangir/awesome-bash-cli) (`abcli`), then,

```bash
abcli git clone openai install
openai help verbose
```

![image](./assets/marquee.png)

## Sentence -> Image

```bash
abcli select; \
open .; \
openai generate image \
  ~dryrun,height=1024,width=1024 \
  carrot - \
  "an orange carrot walking on Mars."
```

![image](./assets/carrot.png)

## Text -> Video

```bash
abcli select; \
open .; \
openai generate video \
  ~dryrun,frame_count=5,marker=PART,url \
  https://www.gutenberg.org/cache/epub/51833/pg51833.txt
```

![image](./assets/minds.gif)