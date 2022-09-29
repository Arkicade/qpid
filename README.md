# qpid

#### SETUP
First, download all the requirements using
  `pip install -r requirements.txt`

Then you need to get the dataset from which GPT-2 will train on. You can use night_text.txt (590 lines of goodnight texts) or adjust the scraper (scrape_texts.py) to get new goodnight texts.

Afterward you can run qpid.ipynb in Jupyter Notebook and it will generate the goodnight texts!

#### NOTES ON THE QPID PROJECT
In order to train the dataset, you need to consider that you should be training on a GPU instead of a CPU. What could take 3 hours in a CPU could take 5 minutes on a GPU. If you don't have a GPU, you can alternatively use Google Collab's GPU (it may be a bit slower) which is online and free so use it later.

This was developed with Python 3.9.12 and Jupyter Notebook 6.4.12 with Visual Studio Code as a text editor.

#### NOTES ON DIFFERENT VERSIONS OF GPT-2
qpid uses a version of OpenAI's GPT-2 (the original one) which was extended by nshepperd. It can be found in the following link https://github.com/nshepperd/gpt-2 which allows for model finetuning. There's alternatively gpt-2-simple (which combines nshepperd with textgenrnn, an openAI's repo) and huggingface.
