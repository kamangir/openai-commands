# 🛠️ sentence -> image

```bash
@select - open; \
@openai generate image \
  ~dryrun,height=1024,width=1024 \
  carrot - \
  "an orange carrot walking on Mars."
```

![image](./assets/carrot.png)

# 🛠️ text -> mural

"[The Laughing Heart](https://allpoetry.com/poem/14326890-The-Laughing-Heart-by-Charles-Bukowski)" by Charles Bukowski, [more examples](http://kamangir.net/private/?object=2023-03-26-19-10-26-51814).

```bash
@select - open; \
DALL-E render  \
  ~dryrun,publish,url,verbose \
  https://allpoetry.com/poem/14326890-The-Laughing-Heart-by-Charles-Bukowski
```

![image](./assets/DALL-E.png)

# 🛠️ images

Implements the [OpenAI Image Generation API](https://platform.openai.com/docs/guides/images/usage?context=python).

Notebook implementation [`./notebooks/images.ipynb`](./notebooks/images.ipynb),

```bash
@select - open; \
@openai images generate - \
	"a person flying through the streets of Vancouver." \
	. --verbose 1
```

![image](https://github.com/kamangir/assets/blob/main/openai_commands/2024-01-20-19-00-28-67378.png?raw=true)

