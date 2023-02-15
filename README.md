# github-readme-openai-text-edit
Python script that reads the output of Scribehow README into OpenAI textedit to re-write as more concise.

### Usage ###
Needs an OpenAI key set as OPENAI_API_KEY environment variable:
https://elephas.app/blog/how-to-create-openai-api-keys-cl5c4f21d281431po7k8fgyol0

Looks for README generated from ScribeHow in current directory and uses that.

Uses GPT-3 text-davinci-edit-001 model:
* https://platform.openai.com/docs/api-reference/edits

Can control the speed with the sleep variable. I use 30 because free version OpenAI will limit you otherwise.

Can control the prompt with the var_instruction variable. The one I use by default seems to work.

No output happens in the console when you run the script. It logs all STDOUT to a results.txt file in the working directory. 

Tail -f results.txt to see the output.
