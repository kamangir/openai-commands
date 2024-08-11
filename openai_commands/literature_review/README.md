
# 🛠️ literature review (`@litrev`)

literature review using [OpenAI API](../completion/).

```bash
 > @litrev help
@litrev \
	[question=<question>,dryrun,~download,publish,suffix=<suffix>,~upload] \
	[AMR-vx|<object-name>] \
	[--count <-1>] \
	[--filename <filename>] \
	[--overwrite 1] \
	[--verbose 1]
 . <object-name>/<filename>.csv -literature-review-@-<question.yaml>-> <object-name>-<suffix>/<filename>-<question>.csv.
```

- [test run](./docs/test.md)
- [run at scale (v6)](./docs/v6.md)
- [run at scale (v7)](./docs/v7.md)

|   |   |
| --- | --- |
| [aws_batch](https://github.com/kamangir/notebooks-and-scripts/tree/main/notebooks_and_scripts/workflow/runners/aws_batch.py) | [local](https://github.com/kamangir/notebooks-and-scripts/tree/main/notebooks_and_scripts/workflow/runners/local.py) |
| [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/AMR-v7-test-litrev-multiple-aws_batch-study-type-screening-result/workflow.gif?raw=true&random=bn2bEVsHAbCb9TUn)](https://kamangir-public.s3.ca-central-1.amazonaws.com/AMR-v7-test-litrev-multiple-aws_batch-study-type-screening-result/workflow.gif?raw=true&random=bn2bEVsHAbCb9TUn) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/AMR-v7-test-litrev-multiple-local-study-type-screening-result/workflow.gif?raw=true&random=ngWv2nxjBIBIiKSo)](https://kamangir-public.s3.ca-central-1.amazonaws.com/AMR-v7-test-litrev-multiple-local-study-type-screening-result/workflow.gif?raw=true&random=ngWv2nxjBIBIiKSo) |

---

notes: [1](https://arash-kamangir.medium.com/%EF%B8%8F-open-ai-experiments-146-6d3390da78c3), [2](https://arash-kamangir.medium.com/%EF%B8%8F-open-ai-experiments-145-dc241e47d9e1)

---
built by [`abcli-9.192.1-current`](https://github.com/kamangir/awesome-bash-cli), based on [`openai_commands-3.123.1`](https://github.com/kamangir/openai-commands).
