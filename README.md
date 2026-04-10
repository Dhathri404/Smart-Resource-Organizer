# Smart Academic Filer (AI-Powered)

An automated file organization system for students. This tool uses **Multinomial Naive Bayes** to classify academic documents (PDFs, reports) into subject-specific folders based on content analysis.

## 🚀 Features
* **Real-time Monitoring**: Uses the `watchdog` API to detect new downloads instantly.
* **Hybrid Classification**: Combines heuristic dictionary matching with probabilistic AI prediction using `scikit-learn`.
* **PDF Text Extraction**: Utilizes `PyPDF2` to scrape metadata and content from first-page headers.
* **Temporal Synchronization**: Implements a 2-second write-buffer to handle OS-level file locking.

## 🛠️ Tech Stack
* **Language**: Python 3.x
* **ML Library**: Scikit-learn (MultinomialNB, CountVectorizer)
* **File I/O**: Watchdog, PyPDF2, Shutil

## 📂 Project Structure
- `main.py`: The core application script.
- `keyword.txt`: Configuration file containing subject keywords and course codes.
- `Organized_Files/`: The destination directory for categorized documents.

- Including the Setup and Installation section is vital for GitHub. It proves that your project is reproducible, which is a key requirement in software engineering and AI research.

Here is the updated README.md section to add to your existing one:


## ⚙️ Setup & Installation

Follow these steps to get the AI Organizer running on your local machine.

### 1. Prerequisites
Ensure you have **Python 3.8+** installed. You can check this by running:
```bash
python --version
2. Clone the Repository
Bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
3. Install Dependencies
Install the required libraries for Machine Learning, PDF processing, and File Monitoring:

Bash
pip install scikit-learn watchdog PyPDF2
4. Configuration
Before running, update the keyword.txt file with your subjects and course codes.
Format: CategoryName: keyword1, keyword2, CourseCode

5. Run the Application
Bash
python main.py
🛠️ How it Works 
Training Phase: Upon execution, the script reads keyword.txt and trains a Multinomial Naive Bayes model.

Monitoring Phase: The watchdog Observer begins an event loop to monitor the directory.

Inference Phase: When a file is detected, the system extracts text and predicts the category.

Execution Phase: Files are moved into organized sub-directories using shutil.


