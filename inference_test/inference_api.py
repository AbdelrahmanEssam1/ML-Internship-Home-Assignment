from flask import Flask , request , jsonify
from db_utils import create_db , save_prediction
from data_ml_assignment.constants import LABELS_MAP
from data_ml_assignment.training.train_pipeline import TrainingPipeline

app = Flask(__name__)

#Ensure the database and table exist
create_db()

# Load the training pipeline
pipeline = TrainingPipeline()
pipeline.train(serialize=False)  # Ensure the model is trained

@app.route("/api/inference" , methods=["POST"])

def save_inference():

    try:
        data = request.get_json()
        resume_text = data.get("text")

        if not resume_text:
            return jsonify({"error": "the 'text' field is required"}), 400
        
        #run inference
        predicted_label_index = pipeline.model.predict([resume_text])[0]
        predicted_label = LABELS_MAP.get(int(predicted_label_index))

        #save predictions to the database
        save_prediction(resume_text , predicted_label)

        return jsonify({"predicted_label": predicted_label}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#run the flask app
if __name__== "__main__":
    app.run(host="0.0.0.0" , port=9000, debug= True)