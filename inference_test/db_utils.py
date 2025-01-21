import sqlite3


#create the SQLite database and table
def create_db():

    conn = sqlite3.connect("inference_results.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   resume_text TEXT NOT NULL,
                   predicted_label TEXT NOT NULL
        )        
        """)
    
    conn.commit()
    conn.close()

#save a prediction to the database

def save_prediction(resume_text , predicted_label):
    conn = sqlite3.connect("inference_results.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions (resume_text , predicted_label)
        VALUES(?,?)
        """,(resume_text , predicted_label))
    conn.commit()
    conn.close()