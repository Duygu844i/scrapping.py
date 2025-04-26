iPhone Models Scrapping

This Python project scrapes all available iPhone models, prices, and product links from the website trendyol.az and saves them into a clean Excel file.

Features
	•	Scrapes multiple pages (you can set how many).
	•	Collects:
	•	iPhone model names,
	•	Prices,
	•	Product links.
	•	Saves the data into an Excel (.xlsx) file.
	•	Works on Mac, Windows, and Linux.

Requirements

Make sure you have Python 3 installed.

Install the required Python libraries:


How to Use
	1.	Clone or download this project to your computer.
	2.	Open the project folder in VS Code or any code editor.
	3.	Open the Terminal inside the project folder.
	4.	Run the script
     5.	After running, you will see a file called iphone_models_full.xlsx in the project folder.
	6.	Open it:
	•	On Mac: Right-click → Reveal in Finder → Double-click to open with Excel or Numbers app.
	•	On Windows: Double-click to open with Excel.  



Project Structure
tkinter_project/
│
├── scrapping.py         # Main scraping script
├── README.md             # This file (documentation)
└── iphone_models_full.xlsx  # Output (after running the script)

Notes
	•	If the website structure changes, the scraper may need to be updated.
	•	Use the script responsibly and avoid too many rapid requests.

