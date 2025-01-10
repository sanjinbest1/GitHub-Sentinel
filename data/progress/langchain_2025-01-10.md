# langchain - 2025-01-10

## Issues
- docs: fix import error in documentation: https://github.com/langchain-ai/langchain/pull/29124
- Add lindorm as new integration: https://github.com/langchain-ai/langchain/pull/29123
- added onepage custom tools: https://github.com/langchain-ai/langchain/pull/29122
- langchain_community is missing a dependency: https://github.com/langchain-ai/langchain/issues/29121
- replace all LANGCHAIN_ flags with LANGSMITH_ flags: https://github.com/langchain-ai/langchain/pull/29120
- docs[patch]: update docs for langchain-openai==0.3: https://github.com/langchain-ai/langchain/pull/29119
- Additional kwargs key prompt_tokens already exists in left dict and value has unsupported type <class 'int'> in langchain-core/utils/_merge.py merge_dict() function when running with anthropic.claude-3-sonnet: https://github.com/langchain-ai/langchain/issues/29116
- Pipeshift - Langchain integration of pipeshift: https://github.com/langchain-ai/langchain/pull/29114
- docs[patch]: fix links in partner package table: https://github.com/langchain-ai/langchain/pull/29112
- SurrealDBStore returns error `ImportError: cannot import name 'Surreal' from 'surrealdb'`: https://github.com/langchain-ai/langchain/issues/29111
- Langchain_community: Fix issue with missing backticks in arango client: https://github.com/langchain-ai/langchain/pull/29110
- Update word in databricks_vector_search.ipynb from "cna" to "can": https://github.com/langchain-ai/langchain/pull/29109
-  UnstructuredMarkdownLoader#zipfile.BadZipFile: File is not a zip file: https://github.com/langchain-ai/langchain/issues/29108
- [Community]: Small Fix in google_firestore memory notebook: https://github.com/langchain-ai/langchain/pull/29107
- langchain-cli for MacOS unable to load required files: https://github.com/langchain-ai/langchain/issues/29106
- poetry 2 see how much breaks: https://github.com/langchain-ai/langchain/pull/29105
- docs: add Docling loader docs: https://github.com/langchain-ai/langchain/pull/29104
- langchain: allow runnables as prompt: https://github.com/langchain-ai/langchain/pull/29103
- community: add init for unstructured epub/image/markdown/pdf/ppt/word: https://github.com/langchain-ai/langchain/pull/29101
- openai[minor]: release 0.3: https://github.com/langchain-ai/langchain/pull/29100
- docs: Add upstage document parse loader to pdf loaders: https://github.com/langchain-ai/langchain/pull/29099
- docs: Adding voyage-3-large to the .ipynb file: https://github.com/langchain-ai/langchain/pull/29098
- openai[patch]: remove optional defaults: https://github.com/langchain-ai/langchain/pull/29097
- docs: Remove additional ` in heading: https://github.com/langchain-ai/langchain/pull/29096
- DOC: <Issue related to  --upgrade  flag in the lang chain documentation / >: https://github.com/langchain-ai/langchain/issues/29095
- DOC: <Issue related to /v0.2/docs/tutorials/rag/>: https://github.com/langchain-ai/langchain/issues/29094
- partner: Update Upstage Model Names and Remove Deprecated Model: https://github.com/langchain-ai/langchain/pull/29093
- community: add init for `UnstructuredHTMLLoader` to solve pathlib paths: https://github.com/langchain-ai/langchain/pull/29091
- UnstructuredHTMLLoader fail when given `Path` type document: https://github.com/langchain-ai/langchain/issues/29090
- community: fix "confluence-loader" enable include_labels for documents loaded via CQL: https://github.com/langchain-ai/langchain/pull/29089

## Pull Requests
- docs: fix import error in documentation: https://github.com/langchain-ai/langchain/pull/29124
- Add lindorm as new integration: https://github.com/langchain-ai/langchain/pull/29123
- added onepage custom tools: https://github.com/langchain-ai/langchain/pull/29122
- replace all LANGCHAIN_ flags with LANGSMITH_ flags: https://github.com/langchain-ai/langchain/pull/29120
- docs[patch]: update docs for langchain-openai==0.3: https://github.com/langchain-ai/langchain/pull/29119
- Pipeshift - Langchain integration of pipeshift: https://github.com/langchain-ai/langchain/pull/29114
- poetry 2 see how much breaks: https://github.com/langchain-ai/langchain/pull/29105
- langchain: allow runnables as prompt: https://github.com/langchain-ai/langchain/pull/29103
- community: add init for unstructured epub/image/markdown/pdf/ppt/word: https://github.com/langchain-ai/langchain/pull/29101
- openai[minor]: release 0.3: https://github.com/langchain-ai/langchain/pull/29100
- rfc core: basemessage.text: https://github.com/langchain-ai/langchain/pull/29078
- openai[patch]: support optional fields in dict structured output with method="json_schema": https://github.com/langchain-ai/langchain/pull/29075
- core: Handle unterminated escape character when parsing partial JSON: https://github.com/langchain-ai/langchain/pull/29065
- Refactoring PDF loaders: 02 PyMuPDF: https://github.com/langchain-ai/langchain/pull/29063
- rfc: bind_tools(response_format): https://github.com/langchain-ai/langchain/pull/29051
- rfc: AIMessage.parsed: https://github.com/langchain-ai/langchain/pull/29050
- rfc: used AIMessage.parsed: https://github.com/langchain-ai/langchain/pull/29049
- core: Use Blockbuster to detect blocking calls in asyncio during tests: https://github.com/langchain-ai/langchain/pull/29043
- community: Add "headers" parameter support to OpenAPI tools: https://github.com/langchain-ai/langchain/pull/29007
- Support for Gemini Tool Calling and Correct usage metadata in ChatOpenAI: https://github.com/langchain-ai/langchain/pull/29002
- text-splitters: Add JSFrameworkTextSplitter for Handling JavaScript Framework Code: https://github.com/langchain-ai/langchain/pull/28972
- Refactoring PDF loaders: all: https://github.com/langchain-ai/langchain/pull/28970
- partner: Update aiohttp in langchain pinecone.: https://github.com/langchain-ai/langchain/pull/28863
- core: improved method tools: https://github.com/langchain-ai/langchain/pull/28695
- partners: Add the additonnal kward 'context' for openai: https://github.com/langchain-ai/langchain/pull/28472
- core[patch]: dont deep copy merge_message_runs: https://github.com/langchain-ai/langchain/pull/28454
- core:  Fixed inspecting schema issue when working with InjectedToolArg annotations: https://github.com/langchain-ai/langchain/pull/28435
- core: fix issue with runnable parallel schema being empty when children runnable input schemas use TypedDict's: https://github.com/langchain-ai/langchain/pull/28196
- core: Allow nested prompt templates: https://github.com/langchain-ai/langchain/pull/28024
- Core: Handle Failed Cache Reads For Non-Serializable Objects: https://github.com/langchain-ai/langchain/pull/27989

## Commits
- docs[patch]: fix links in partner package table (#29112)

Integrations in external repos are not built into [API
ref](https://python.langchain.com/api_reference/), so currently [the
table](https://python.langchain.com/docs/integrations/providers/#integration-packages)
includes broken links. Here we update the links for this type of package
to point to PyPi.: https://github.com/langchain-ai/langchain/commit/facfd42768485d92777608e5d62d705550c1a5c4
- openai[patch]: support streaming with json_schema response format (#29044)

- Stream JSON string content. Final chunk includes parsed representation
(following OpenAI
[docs](https://platform.openai.com/docs/guides/structured-outputs#streaming)).
- Mildly (?) breaking change: if you were using streaming with
`response_format` before, usage metadata will disappear unless you set
`stream_usage=True`.

## Response format

Before:

![Screenshot 2025-01-06 at 11 59
01 AM](https://github.com/user-attachments/assets/e54753f7-47d5-421d-b8f3-172f32b3364d)


After:

![Screenshot 2025-01-06 at 11 58
13 AM](https://github.com/user-attachments/assets/34882c6c-2284-45b4-92f7-5b5b69896903)


## with_structured_output

For pydantic output, behavior of `with_structured_output` is unchanged
(except for warning disappearing), because we pluck the parsed
representation straight from OpenAI, and OpenAI doesn't return it until
the stream is completed. Open to alternatives (e.g., parsing from
content or intermediate dict chunks generated by OpenAI).

Before:

![Screenshot 2025-01-06 at 12 38
11 PM](https://github.com/user-attachments/assets/913d320d-f49e-4cbb-a800-b394ae817fd1)

After:

![Screenshot 2025-01-06 at 12 38
58 PM](https://github.com/user-attachments/assets/f7a45dd6-d886-48a6-8d76-d0e21ca767c6): https://github.com/langchain-ai/langchain/commit/815bfa1913d0f42eec2a6c39b18c7abe07295c6c
- docs: add Docling loader docs (#29104)

### Description
This adds the docs for the Docling document loader.
[Docling](https://github.com/DS4SD/docling) parses PDF, DOCX, PPTX,
HTML, and other formats into a rich unified representation including
document layout, tables etc., making them ready for generative AI
workflows like RAG.

Some references:
- https://research.ibm.com/blog/docling-generative-AI
-
https://www.redhat.com/en/blog/docling-missing-document-processing-companion-generative-ai
- [Docling Technical Report](https://arxiv.org/abs/2408.09869)

The introduced `DoclingLoader` enables users to:
- use various document types in their LLM applications with ease and
speed, and
- leverage Docling's rich representation for advanced, document-native
grounding.

### Issue
Replacing PR #27987 as discussed with @efriis
[here](https://github.com/langchain-ai/langchain/pull/27987#issuecomment-2489354930).

### Dependencies
None

---------

Signed-off-by: Panos Vagenas <35837085+vagenas@users.noreply.github.com>: https://github.com/langchain-ai/langchain/commit/858f655a25619639097c31714fd3eef117a37945
- docs: Adding voyage-3-large to the .ipynb file (#29098)

**Description:**
Adding voyage-3-large model to the .ipynb file (its just extending a
list, so not even a code change)


- [ ] **Add tests and docs**: If you're adding a new integration, please
include
1. a test for the integration, preferably unit tests that do not rely on
network access,
2. an example notebook showing its use. It lives in
`docs/docs/integrations` directory.


- [ ] **Lint and test**: Run `make format`, `make lint` and `make test`
from the root of the package(s) you've modified. See contribution
guidelines for more: https://python.langchain.com/docs/contributing/

Additional guidelines:
- Make sure optional dependencies are imported within a function.
- Please do not add dependencies to pyproject.toml files (even optional
ones) unless they are required for unit tests.
- Most PRs should not touch more than one package.
- Changes should be backwards compatible.
- If you are adding something to community, do not re-import it in
langchain.

If no one reviews your PR within a few days, please @-mention one of
baskaryan, efriis, eyurtsev, ccurme, vbarda, hwchase17.: https://github.com/langchain-ai/langchain/commit/cc55e32924b20449e154fd0504931464b3c37bb4
- Update word in databricks_vector_search.ipynb from "cna" to "can" (#29109)

fix to word "can"

Thank you for contributing to LangChain!

- [ ] **PR title**: "package: description"
- Where "package" is whichever of langchain, community, core, etc. is
being modified. Use "docs: ..." for purely docs changes, "infra: ..."
for CI changes.
  - Example: "community: add foobar LLM"


- [ ] **PR message**: ***Delete this entire checklist*** and replace
with
    - **Description:** a description of the change
    - **Issue:** the issue # it fixes, if applicable
    - **Dependencies:** any dependencies required for this change
- **Twitter handle:** if your PR gets announced, and you'd like a
mention, we'll gladly shout you out!


- [ ] **Add tests and docs**: If you're adding a new integration, please
include
1. a test for the integration, preferably unit tests that do not rely on
network access,
2. an example notebook showing its use. It lives in
`docs/docs/integrations` directory.


- [ ] **Lint and test**: Run `make format`, `make lint` and `make test`
from the root of the package(s) you've modified. See contribution
guidelines for more: https://python.langchain.com/docs/contributing/

Additional guidelines:
- Make sure optional dependencies are imported within a function.
- Please do not add dependencies to pyproject.toml files (even optional
ones) unless they are required for unit tests.
- Most PRs should not touch more than one package.
- Changes should be backwards compatible.
- If you are adding something to community, do not re-import it in
langchain.

If no one reviews your PR within a few days, please @-mention one of
baskaryan, efriis, eyurtsev, ccurme, vbarda, hwchase17.: https://github.com/langchain-ai/langchain/commit/287abd9e0d97d221ded11861e85313c96a92d1d0
- [Community]: Small Fix in google_firestore memory notebook (#29107)

- **Description:** Just a small fix in google_firestore memory notebook
- **Issue:** @29095: https://github.com/langchain-ai/langchain/commit/a46c2bce51a334532c5acbf20219d3084eca1cea
- Langchain_community: Fix issue with missing backticks in arango client (#29110)

- **Description:** Adds backticks to generate_schema function in the
arango graph client
- **Issue:** We experienced an issue with the generate schema function
when talking to our arango database where these backticks were missing
    - **Dependencies:** none
    - **Twitter handle:** @anangelofgrace: https://github.com/langchain-ai/langchain/commit/00dcc44739ceade0ad96108e82401e26afe3a170
- docs: Add upstage document parse loader to pdf loaders (#29099)

Add upstage document parse loader to pdf loaders

Additional guidelines:
- Make sure optional dependencies are imported within a function.
- Please do not add dependencies to pyproject.toml files (even optional
ones) unless they are required for unit tests.
- Most PRs should not touch more than one package.
- Changes should be backwards compatible.
- If you are adding something to community, do not re-import it in
langchain.

If no one reviews your PR within a few days, please @-mention one of
baskaryan, efriis, eyurtsev, ccurme, vbarda, hwchase17.: https://github.com/langchain-ai/langchain/commit/fa6f08faa172695a8efc45d57c2995bed8f5e4c6
- community: add init for `UnstructuredHTMLLoader` to solve pathlib paths (#29091)

## Description
Add `__init__` for `UnstructuredHTMLLoader` to restrict the input type
to `str` or `Path`, and transfer the `self.file_path` to `str` just like
`UnstructuredXMLLoader` does.

## Issue
Fix #29090 

## Dependencies
No changes.: https://github.com/langchain-ai/langchain/commit/2b09f798e1de1717c6389e5d9f5c34c7c3248be6
- community: fix "confluence-loader" enable include_labels for documents loaded via CQL (#29089)

## Description
This PR enables label inclusion for documents loaded via CQL in the
confluence-loader.

- Updated _lazy_load to pass the include_labels parameter instead of
False in process_pages calls for documents loaded via CQL.
- Ensured that labels can now be fetched and added to the metadata for
documents queried with cql.

## Related Modification History
This PR builds on the previous functionality introduced in
[#28259](https://github.com/langchain-ai/langchain/pull/28259), which
added support for including labels with the include_labels option.
However, this functionality did not work as expected for CQL queries,
and this PR fixes that issue.

If the False handling was intentional due to another issue, please let
me know. I have verified with our Confluence instance that this change
allows labels to be correctly fetched for documents loaded via CQL.

## Issue
Fixes #29088


## Dependencies
No changes.

## Twitter Handle
[@zenoengine](https://x.com/zenoengine): https://github.com/langchain-ai/langchain/commit/c8ca1cd42fea0c5f336aff379f1e432a87e29c14
- partner: Update Upstage Model Names and Remove Deprecated Model (#29093)

This PR updates model names in the upstage library to reflect the latest
naming conventions and removes deprecated models.

Changes:

Renamed Models:
- `solar-1-mini-chat` -> `solar-mini`
- `solar-1-mini-embedding-query` -> `embedding-query`

Removed Deprecated Models:
- `layout-analysis` (replaced to `document-parse`)

Reference:
- https://console.upstage.ai/docs/getting-started/overview
-
https://github.com/langchain-ai/langchain-upstage/releases/tag/libs%2Fupstage%2Fv0.5.0

Additional guidelines:
- Make sure optional dependencies are imported within a function.
- Please do not add dependencies to pyproject.toml files (even optional
ones) unless they are required for unit tests.
- Most PRs should not touch more than one package.
- Changes should be backwards compatible.
- If you are adding something to community, do not re-import it in
langchain.

If no one reviews your PR within a few days, please @-mention one of
baskaryan, efriis, eyurtsev, ccurme, vbarda, hwchase17.: https://github.com/langchain-ai/langchain/commit/9d290abccd8f448eeec373bb16134da30b3a014d
- docs: Remove additional ` in heading (#29096)

Remove the additional ` in the pipe operator heading: https://github.com/langchain-ai/langchain/commit/9f5fa50bbf376aabb6f81889d285ebf4215e6672
- Kùzu package integration docs (#29076)

## Langchain Kùzu

### Description
 
This PR adds docs for the `langchain-kuzu` package [on
PyPI](https://pypi.org/project/langchain-kuzu/) that was recently
published, allowing Kùzu users to more easily use and work with
LangChain QA chains. The package will also make it easier for the Kùzu
team to continue supporting and updating the integration over future
releases.

### Twitter Handle

Please tag [@kuzudb](https://x.com/kuzudb) on Twitter once this PR is
merged, so LangChain users can be notified!

---------

Co-authored-by: Erick Friis <erickfriis@gmail.com>: https://github.com/langchain-ai/langchain/commit/b1dafaef9b2c32151acb42367012e0a7d35067e3
- partners/groq: release 0.2.3 (#29081): https://github.com/langchain-ai/langchain/commit/cc0f81f40f00fabfa72dbc2fe3c739263631ac0c
- multiple: disable socket for unit tests (#29080): https://github.com/langchain-ai/langchain/commit/fcc9cdd1007780e307beb6a9a94688d28d985098
- groq: user agent (#29079): https://github.com/langchain-ai/langchain/commit/539ebd5431ff4670747ac8ffdd2faa2a15893a8d
- pinecone: bump core version (#29077): https://github.com/langchain-ai/langchain/commit/c5bee0a544206e8851adf2f811151a6876322e51
- pinecone: Review pinecone tests (#29073)

Title: langchain-pinecone: improve test structure and async handling

Description: This PR improves the test infrastructure for the
langchain-pinecone package by:
1. Implementing LangChain's standard test patterns for embeddings
2. Adding comprehensive configuration testing
3. Improving async test coverage
4. Fixing integration test issues with namespaces and async markers

The changes make the tests more robust, maintainable, and aligned with
LangChain's testing standards while ensuring proper async behavior in
the embeddings implementation.

Key improvements:
- Added standard EmbeddingsTests implementation
- Split custom configuration tests into a separate test class
- Added proper async test coverage with pytest-asyncio
- Fixed namespace handling in vector store integration tests
- Improved test organization and documentation

Dependencies: None (uses existing test dependencies)

Tests and Documentation:
- ✅ Added standard test implementation following LangChain's patterns
- ✅ Added comprehensive unit tests for configuration and async behavior
- ✅ All tests passing locally
- No documentation changes needed (internal test improvements only)

Twitter handle: N/A

---------

Co-authored-by: Erick Friis <erick@langchain.dev>: https://github.com/langchain-ai/langchain/commit/ce9e9f93149ca264ac92e7481f42b6e4cdafae6e
- infra[patch]: drop prompty from core dependents (#29068): https://github.com/langchain-ai/langchain/commit/d9c51b71c4a4a1e7acc6d9c13ec2549944547e56
- community[patch]: Refactoring PDF loaders: 01 prepare (#29062)

- **Refactoring PDF loaders step 1**: "community: Refactoring PDF
loaders to standardize approaches"

- **Description:** Declare CloudBlobLoader in __init__.py. file_path is
Union[str, PurePath] anywhere
- **Twitter handle:** pprados

This is one part of a larger Pull Request (PR) that is too large to be
submitted all at once.
This specific part focuses to prepare the update of all parsers.

For more details, see [PR
28970](https://github.com/langchain-ai/langchain/pull/28970).

@eyurtsev it's the start of a PR series.: https://github.com/langchain-ai/langchain/commit/2921597c71d7ddda34b1a510705ab1bdddb19811
- Add Google Vertex AI Vector Search Hybrid Search Documentation (#29064)

Add examples in the documentation to use hybrid search in Vertex AI
[Vector
Search](https://github.com/langchain-ai/langchain-google/pull/628): https://github.com/langchain-ai/langchain/commit/a49448a7c9ef8200022ee1870b20ca9f890d869b
- [docs] Update indexing.ipynb (#29055)

According to https://github.com/langchain-ai/langchain/pull/21127, now
`AzureSearch` should be compatible with LangChain indexer.: https://github.com/langchain-ai/langchain/commit/0d226de25c246305782c7e95639a6cd37bb1c50b
- text-splitters[patch]: release 0.3.5 (#29054)

Resolves https://github.com/langchain-ai/langchain/issues/29053: https://github.com/langchain-ai/langchain/commit/55677e31f7b6b279c1d6752d1a8c3f1aad523a41
- Revert "integrations[patch]: remove non-required chat param defaults" (#29048)

Reverts langchain-ai/langchain#26730

discuss best way to release default changes (esp openai temperature): https://github.com/langchain-ai/langchain/commit/187131c55c1b788da38124c6e7917151249746d6
- integrations[patch]: remove non-required chat param defaults (#26730)

anthropic:
  - max_retries

openai:
  - n
  - temperature
  - max_retries

fireworks
  - temperature

groq
  - n
  - max_retries
  - temperature

mistral
  - max_retries
  - timeout
  - max_concurrent_requests
  - temperature
  - top_p
  - safe_mode

---------

Co-authored-by: Erick Friis <erick@langchain.dev>: https://github.com/langchain-ai/langchain/commit/3d7ae8b5d21672c992a65b064e392c27caccda8b
- DOC: Improve human input prompt in FewShotChatMessagePromptTemplate example (#29023)

Fixes #29010 

This PR updates the example for FewShotChatMessagePromptTemplate by
modifying the human input prompt to include a more descriptive and
user-friendly question format ('What is {input}?') instead of just
'{input}'. This change enhances clarity and usability in the
documentation example.

Co-authored-by: Erick Friis <erick@langchain.dev>: https://github.com/langchain-ai/langchain/commit/b9db8e99210ae153876b9c2839bf608ef2416d94
- voyageai[patch]: release 0.1.4 (#29046): https://github.com/langchain-ai/langchain/commit/1f78d4faf4b0efd035ef85ada60388e4ca8b54f1
- docs: add langchain-pull-md Markdown loader (#29024)

- [x] **PR title**: "docs: add langchain-pull-md Markdown loader"

- [x] **PR message**: 
- **Description:** This PR introduces the `langchain-pull-md` package to
the LangChain community. It includes a new document loader that utilizes
the pull.md service to convert URLs into Markdown format, particularly
useful for handling web pages rendered with JavaScript frameworks like
React, Angular, or Vue.js. This loader helps in efficient and reliable
Markdown conversion directly from URLs without local rendering, reducing
server load.
    - **Issue:** NA
    - **Dependencies:** requests >=2.25.1
    - **Twitter handle:** https://x.com/eugeneevstafev?s=21

- [x] **Add tests and docs**: 
1. Added unit tests to verify URL checking and conversion
functionalities.
2. Created a comprehensive example notebook detailing the usage of the
new loader.

- [x] **Lint and test**: 
- Completed local testing using `make format`, `make lint`, and `make
test` commands as per the LangChain contribution guidelines.


**Related Links:**
- [Package Repository](https://github.com/chigwell/langchain-pull-md)
- [PyPI Package](https://pypi.org/project/langchain-pull-md/)

---------

Co-authored-by: Erick Friis <erick@langchain.dev>: https://github.com/langchain-ai/langchain/commit/6a152ce245f3c89ef340cebf6faebdd58353f337
- community: Fix redundancy in code. (#29022)

In my previous PR (#28953), I added an unwanted condition for validating
the Azure ML Endpoint. In this PR, I have rectified the issue.: https://github.com/langchain-ai/langchain/commit/20a715a103e9a048bf91414f4a68fca1493f04a3
- Update index.mdx (#29029)

spell check

Thank you for contributing to LangChain!

- [ ] **PR title**: "package: description"
- Where "package" is whichever of langchain, community, core, etc. is
being modified. Use "docs: ..." for purely docs changes, "infra: ..."
for CI changes.
  - Example: "community: add foobar LLM"


- [ ] **PR message**: ***Delete this entire checklist*** and replace
with
    - **Description:** a description of the change
    - **Issue:** the issue # it fixes, if applicable
    - **Dependencies:** any dependencies required for this change
- **Twitter handle:** if your PR gets announced, and you'd like a
mention, we'll gladly shout you out!


- [ ] **Add tests and docs**: If you're adding a new integration, please
include
1. a test for the integration, preferably unit tests that do not rely on
network access,
2. an example notebook showing its use. It lives in
`docs/docs/integrations` directory.


- [ ] **Lint and test**: Run `make format`, `make lint` and `make test`
from the root of the package(s) you've modified. See contribution
guidelines for more: https://python.langchain.com/docs/contributing/

Additional guidelines:
- Make sure optional dependencies are imported within a function.
- Please do not add dependencies to pyproject.toml files (even optional
ones) unless they are required for unit tests.
- Most PRs should not touch more than one package.
- Changes should be backwards compatible.
- If you are adding something to community, do not re-import it in
langchain.

If no one reviews your PR within a few days, please @-mention one of
baskaryan, efriis, eyurtsev, ccurme, vbarda, hwchase17.: https://github.com/langchain-ai/langchain/commit/c8d6f9d52b3421cafb797c29dec181e8d990c3a7
