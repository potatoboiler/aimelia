# Setup

## Scripts

`character-ai` contains scripts relevant to commentary generation (might get migrated to `Voyager` in the future).

`voyager-commentary-deps` contains the venv and requirements.txt. Activate it before running Voyager.

To run Voyager, see the fork in the submodules and run `Voyager/launch.py`. Make sure you change `mc_port` and put your key in `Voyager/openai_api_key.txt` before running it. The OpenAI API key should have access to GPT-4.

For now, the Voyager fork also outputs to a file, in order to study the LLM prompts.
