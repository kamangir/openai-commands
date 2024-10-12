
# 🛠️ literature review (`@litrev`)

literature review at scale on [AWS Batch](https://aws.amazon.com/batch/) through the [OpenAI API](../completion/).


```bash
 > @litrev help
@litrev \
	[dryrun,~download,publish,question=<question>,suffix=<suffix>,~upload] \
	[AMR-v7|<object-name>] \
	[--count <-1>] \
	[--filename <filename>] \
	[--overwrite 1] \
	[--verbose 1]
 . ask a multiple-choice question about the list of studies in <object-name>.
   input: <object-name>/<filename>.csv, column: Abstract.
   question: <object-name>/<question>.yaml.
   output: <object-name>-<suffix>-<question>/<filename>.csv, column: <question>.
@litrev combine \
	[~download,dryrun,publish,~upload] \
	[...|<object-name-1>] \
	[..|<object-name-2>] \
	[.|<object-name>]
 . <object-name-1> + <object-name-2> -> <object-name>.
@litrev multiple \
	[dryrun,publish,questions=<question1+question2+...>,suffix=<suffix>] \
	[dryrun,to=aws_batch|generic|local] \
	[dryrun,publish] \
	[AMR-v7|<object-name>] \
	[--count <-1>] \
	[--filename <filename>] \
	[--overwrite 1] \
	[--verbose 1]
 . ask multiple multiple-choice questions about the list of studies in <object-name>.
   input: <object-name>/<filename>.csv, column: Abstract.
   questions: <object-name>/<question1>.yaml, <question2>.yaml, ... .
   output: <object-name>-<suffix>-<question1>-<question-2>-<...>/<filename>.csv, columns: <question1>, <question2>, ... .
```

## example runs

- [test run](./docs/test.md)
- [run at scale (v6)](./docs/v6.md)
- [run at scale (v7)](./docs/v7.md)

## tests

|   |   |
| --- | --- |
| [aws_batch](https://github.com/kamangir/notebooks-and-scripts/tree/main/notebooks_and_scripts/workflow/runners/aws_batch.py) | [local](https://github.com/kamangir/notebooks-and-scripts/tree/main/notebooks_and_scripts/workflow/runners/local.py) |
| [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/AMR-v7-test-litrev-multiple-aws_batch-study-type-screening-result/workflow.gif?raw=true&random=DJFYFOCtpy5sKOYI)](https://kamangir-public.s3.ca-central-1.amazonaws.com/AMR-v7-test-litrev-multiple-aws_batch-study-type-screening-result/workflow.gif?raw=true&random=DJFYFOCtpy5sKOYI) | [![image](https://kamangir-public.s3.ca-central-1.amazonaws.com/AMR-v7-test-litrev-multiple-local-study-type-screening-result/workflow.gif?raw=true&random=nVTyI8gFcUvUxdUF)](https://kamangir-public.s3.ca-central-1.amazonaws.com/AMR-v7-test-litrev-multiple-local-study-type-screening-result/workflow.gif?raw=true&random=nVTyI8gFcUvUxdUF) |

---

- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-open-ai-experiments-146-6d3390da78c3)
- [dev notes](https://arash-kamangir.medium.com/%EF%B8%8F-open-ai-experiments-145-dc241e47d9e1)
