# openai

`openai` is a bash cli for [OpenAI API](https://beta.openai.com/docs/introduction).

🔷  [completion](#Completion) 🔷  [code generation](#code-generation) 🔷  [sentence -> image](#sentence---image) 🔷  [text -> mural](#text---mural) 🔷  [vision](#vision) 🔷 

## Install

Install [`awesome-bash-cli`](https://github.com/kamangir/awesome-bash-cli) (`abcli`), then,

```bash
abcli git clone openai install
```

```bash
 > openai help
🛠️ openai_cli-2.168.1-1.3.4
🛠️ tools for the OpenAI API

openai complete "<prompt>" \
	[-] \
	[--max_tokens <2000>] \
	[--verbose 1]
 . complete <prompt>.
openai completion describe <plugin-name>
 . describe <plugin-name> for openai
openai conda create_env [validate,~recreate]
 . create conda environment.
openai conda validate
 . validate conda environment.
openai dashboard
 . browse openai dashboard.
openai generate image \
	[app=<app-name>,~dryrun,height=<576>,~sign,~tag,width=<768>] \
	[<image>] [<previous-image>] \
	["<sentence>"] \
	[-]
 . <sentence> -[<previous-image>]-> <image>.png.
openai generate video \
	[app=<app-name>,~dryrun,frame_count=16,marker=PART,~publish,~render,resize_to=1280x1024,~sign,slice_by=words|sentences,~upload,url] \
	<filename.txt|url> \
	[-]
 . <filename.txt>|url -> video.mp4
openai generate validate \
	[app=<app-name>,dryrun,what=all|image|video]
 . validate openai.
openai pytest
 . test openai.
openai transform \
	[count=<1>,~dryrun,extension=jpg,~sign,~tag,~upload] \
	[<object-name>] \
	["<sentence>"] \
	[-]
 . <object-name> -<sentence>-> vanwatch-process-dev-2023-11-11-v61.
openai vision "prompt" \
	[auto|low|high,dryrun,~upload] \
	[Davie,~Bute,.jpg] \
	<.|object-name> \
	[--max_count <-1>] \
	[--verbose 1]
 . complete <prompt> given the image(s) in <object-name>.
DALL-E render \
	[brush=tiling|randomwalk,brush_size=256|512|1024,~dryrun,lines=<5>,publish,url,verbose] \
	input.txt|https://allpoetry.com/16-bit-Intel-8088-chip \
	[output.png]<args>
 . render input.txt|url -> output.png.
```

## Completion

```bash
openai complete "describe mathematics"
```

> Mathematics is an abstract science that examines topics such as quantity, structure, space, change, and other topics in various ways. It involves the use of logic, algorithms, and formulas to solve problems. Mathematics can be used to study the natural world, to describe phenomena, and to make predictions about the future. It provides the foundation for the development of a wide range of disciplines in science, technology, engineering, economics, finance, and more.

also works [in a notebook](./notebooks/completion.ipynb).

## Code Generation

Example notebooks to [generate a python functions](./notebooks/completion_ai_function_py.ipynb), special case for [image to image python functions](./notebooks/completion_i2i_function.ipynb), and to [write a bash script](./notebooks/completion_ai_function_bash.ipynb) to use a script, for example, [Vancouver-Watching](https://github.com/kamangir/Vancouver-Watching).

![image](./assets/completion_i2i_function.png)

## Sentence -> Image

```bash
@select - open; \
openai generate image \
  ~dryrun,height=1024,width=1024 \
  carrot - \
  "an orange carrot walking on Mars."
```

![image](./assets/carrot.png)

## Text -> Mural

"[The Laughing Heart](  https://allpoetry.com/poem/14326890-The-Laughing-Heart-by-Charles-Bukowski)" by Charles Bukowski, [more examples](http://kamangir.net/private/?object=2023-03-26-19-10-26-51814).

```bash
@select - open; \
DALL-E render  \
  ~dryrun,publish,url,verbose \
  https://allpoetry.com/poem/14326890-The-Laughing-Heart-by-Charles-Bukowski
```

![image](./assets/DALL-E.png)

## Vision

Implements the [OpenAI vision API](https://platform.openai.com/docs/guides/vision).

> GPT-4 with Vision ... `GPT-4V` or `gpt-4-vision-preview` in the API ... model ... take in images and answer questions about them
... not stateful ... ([more](https://arash-kamangir.medium.com/%EF%B8%8F-openai-vision-1-fb3691bd095a))

Example use on the images ingested from the traffic cameras in downtown Vancouver, using [Vancouver-Watching 🌈](https://github.com/kamangir/Vancouver-Watching),

```bash
openai vision \
    "you are a police offier, what do you see in these images?" \
    - Davie,Bute,.jpg \
    $(vanwatch list area=vancouver,ingest,published \
        --log 0 \
        --count 1 \
        --offset 0) \
    --max_count 10 \
    --verbose 1
```

🔥