import os
import time
import shutil
import PyPDF2
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


current_folder = os.path.dirname(os.path.abspath(__file__))
base_dest = os.path.join(current_folder, "Organized_Files")
config_file = os.path.join(current_folder, "keyword.txt")


keyword_map = {}
vectorizer = CountVectorizer()
classification = MultinomialNB()

def train_ai():
    global keyword_map, vectorizer, classification
    if not os.path.exists(config_file):
        print("⚠️ keyword.txt not found.")
        return False
    
    training_texts, training_labels = [], []
    with open(config_file, "r") as f:
        for line in f:
            if ":" in line:
                category, words = line.split(":")
                category = category.strip()
                word_list = [w.strip().lower() for w in words.split(",")]
                for word in word_list:
                    keyword_map[word] = category
                training_texts.append(" ".join(word_list))
                training_labels.append(category)

    if training_texts:
        X = vectorizer.fit_transform(training_texts)
        classification.fit(X, training_labels)
        return True
    return False

def extract_pdf(file_path):
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            return reader.pages[0].extract_text().lower() if reader.pages else ""
    except:
        return ""

def file_organize(source_path):
    filename = os.path.basename(source_path)
    if filename.endswith(".py") or "Organized_Files" in source_path or filename == "keyword.txt":
        return

    name_lower = filename.lower()
    extracted_text = extract_pdf(source_path) if filename.endswith(".pdf") else ""
    target = "Others"

 
    for key, folder in keyword_map.items():
        if key in name_lower or key in extracted_text:
            target = folder
            break

   
    if target == "Others" and (name_lower.strip() or extracted_text.strip()):
        try:
            vec = vectorizer.transform([name_lower + " " + extracted_text])
            target = classification.predict(vec)[0]
            print(f"🤖 AI Prediction: {target}")
        except:
            pass

    dest_folder = os.path.join(base_dest, target)
    os.makedirs(dest_folder, exist_ok=True)
    try:
        shutil.move(source_path, os.path.join(dest_folder, filename))
        print(f"✅ Organized: {filename} -> {target}")
    except:
        print(f"❌ Move failed: {filename}")


class SimpleHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            
            time.sleep(2) 
            file_organize(event.src_path)


if __name__ == "__main__":
    if train_ai():
        print("🚀 AI System Live. Monitoring folder...")
        
        handler = SimpleHandler()
        observer = Observer()
        observer.schedule(handler, current_folder, recursive=False)
        
        
        observer.start() 
        
        try:
            
            while True:
                time.sleep(1) 
        except KeyboardInterrupt:
            observer.stop()
            print("\n🛑 Monitor Stopped.")
        observer.join()