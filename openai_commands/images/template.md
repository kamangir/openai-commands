| | |
|-|-|
| sentence -> image | text -> mural | images |
| ![image](../../assets/carrot.png) | ![image](https://github.com/kamangir/assets/blob/main/openai_commands/2024-01-20-19-00-28-67378.png?raw=true) |

# 🛠️ sentence -> image

```bash
@select - open; \
@openai generate image \
  ~dryrun,height=1024,width=1024 \
  carrot - \
  "an orange carrot walking on Mars."
```

# 🛠️ images

Implements the [OpenAI Image Generation API](https://platform.openai.com/docs/guides/images/usage?context=python).

Notebook implementation [`./notebooks/images.ipynb`](../../notebooks/images_generate.ipynb),

```bash
@select - open; \
@openai images generate - \
	"a person flying through the streets of Vancouver." \
	. --verbose 1
```
