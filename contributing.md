⚠️ **Note:**
- Contributions are only open to current students
- These contribution instructions were largely composed by ChatGPT

## Adding a file to the repository 
1. Navigate to this repository: [https://github.com/NM-TAFE/learn-to-code-visual-assistant](https://github.com/NM-TAFE/learn-to-code-visual-assistant) 
2. From the top-right corner, select **Fork** and follow the prompts.
3. Open the terminal (Command Prompt or Git Bash on Windows) and navigate the desired parent folder for this project.
4. Clone the forked repository:

```bash

git clone https://github.com/YOUR_USERNAME/learn-to-code-visual-assistant.git
```



Replace `YOUR_USERNAME` with your GitHub username.

5. Navigate to the cloned repository:

```bash

cd learn-to-code-visual-assistant
```


6. Create a new branch:

```bash

git checkout -b add-chatgpt-transcript
```

 
7. Open the "transcripts" folder and add your `pfx-chatgpt-transcript.md` file, with your ChatGPT interaction
8. Stage the new file:

```bash

git add chatgpt-transcript
```


9. Commit the changes:

```bash

git commit -m "Add chatgpt-transcript"
```


10. Push the changes:

```bash

git push origin add-chatgpt-transcript
```


11. Create a pull request on GitHub.
## Proposing suggestions to the main program via pull requests (optional)
1. Create a new branch:

```bash

git checkout -b propose-suggestion
```


2. Edit the relevant files using a text editor.
3. Stage the modified files:

```bash

git add modified-file-path
```



Replace `modified-file-path` with the path to the modified file.

4. Commit the changes:

```bash

git commit -m "Propose changes to the main program"
```


5. Push the changes:

```bash

git push origin propose-suggestion
```


6. Create a pull request on GitHub.
