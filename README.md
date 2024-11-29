# Web Scraping AI

This project is a web scraping tool that uses Selenium and BeautifulSoup to extract content from websites. The extracted content is then processed and summarized using a language model from the LangChain library.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/bugmarkey/WebBot.git
   cd WebBot
   ```

2. Create a virtual environment and activate it:

   #### On Windows:

   - Using Command Prompt:
     ```sh
     python -m venv scrape
     scrap\Scripts\activate.bat
     ```
   - Using PowerShell:
     ```sh
     python -m venv scrape
     scrap\Scripts\Activate.ps1
     ```

   #### On macOS and Linux:

   ```sh
   python3 -m venv scrape
   source scrap/bin/activate
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Download the ChromeDriver and place it in the project root directory.
   - You can download it from [here](https://googlechromelabs.github.io/chrome-for-testing/#stable).
   - Make sure the version of the ChromeDriver matches the version of your Chrome browser.

## Ollama Model Installation

1. Install Ollama from the following [link](https://ollama.com/download) based on the OS.

2. Next go to the Ollama Github Repository or use this [link](https://github.com/ollama/ollama).

3. Select a model that matches your system specifications and copy the Download code.

4. In this case `llama3.1` with 8B parameters and size of 4.7GB.

5. Now open the Windows Terminal and type the command `ollama` to see all the actions of ollama.

6. For installing the model locally give the command `ollama pull llama3.1` and the model will be installed.

7. (Optional): To check the model enter the command `ollama run llama3.1` to run the model locally and to exit give `\exit` or `CTRL + D`

## Usage

1. Run the Streamlit application:

   ```sh
   streamlit run main.py
   ```

2. Enter the URL of the website you want to scrape in the input field and click the "Scrape Site" button.

3. View the extracted and cleaned DOM content in the "View DOM Content" expander.

4. Provide a description for summarization and click the "Summarize" button to get the summarized content.

## Files

- `main.py`: The main entry point for the Streamlit application.
- `scrape.py`: Contains functions for scraping and processing website content.
- `parse.py`: Contains functions for parsing and summarizing the content using LangChain.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: This file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
