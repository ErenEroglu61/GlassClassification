import pickle
import numpy as np
from pathlib import Path

class GlassClassifier:


    def __init__(self):
        model_path = Path("datasets/models")

        try:
            with open(model_path / "classifier.pkl", "rb") as f:
                self.model = pickle.load(f)

            with open(model_path / "scaler.pkl", "rb") as f:
                self.scaler = pickle.load(f)

        except FileNotFoundError:
            print("Model files cannot found")
            print(
                "Please first execute all cells in GlassClassification.ipynb"
            )
            raise

        self.glass_types = {
            1: "Building Windows Float",
            2: "Building Windows Non-Float",
            3: "Vehicle Windows Float",
            4: "Vehicle Windows Non-Float",
            5: "Containers",
            6: "Tableware",
            7: "Headlamps"
        }

    def predict(self, data: dict) -> dict:
        """
        Predict
        """

        features = np.array([[
            data["RI"],
            data["Na"],
            data["Mg"],
            data["Al"],
            data["Si"],
            data["K"],
            data["Ca"]
        ]])

        scaled = self.scaler.transform(features)

        prediction = self.model.predict(scaled)[0]
        probabilities = self.model.predict_proba(scaled)[0]

        confidence_dict = {
            f"Type {i}": float(probabilities[i - 1])
            for i in range(1, 8)
        }

        return {
            "glass_type": self.glass_types.get(
                int(prediction),
                "Unknown"
            ),
            "glass_type_number": int(prediction),
            "probability": float(max(probabilities)),
            "confidence_levels": confidence_dict
        }