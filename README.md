# AI Crop Recommendation System

This project is an AI-powered recommendation system that suggests the **most suitable crop to cultivate** based on environmental and soil conditions such as **N, P, K**, temperature, humidity, pH, and rainfall. It uses a **Random Forest Classifier** trained on real-world agricultural data.

---

## Key Features

- Recommends crops based on user input
- Built with **Streamlit** for a fast and interactive web interface
- Trained using **Random Forest Classifier**
- Based on soil nutrients and climate conditions

---

## How to Run the App Locally

### 1. Clone the repository

```bash
git clone https://github.com/HIMAVARSHINI-AHV/AI Crop Recommendation System.git
cd AI Crop Recommendation System
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run app.py
```

---

## Input Parameters

| Feature      | Description                              |
|--------------|------------------------------------------|
| N            | Nitrogen content in the soil             |
| P            | Phosphorous content in the soil          |
| K            | Potassium content in the soil            |
| Temperature  | Temperature in degree Celsius            |
| Humidity     | Relative Humidity (%)                    |
| pH           | pH value of the soil                     |
| Rainfall     | Rainfall in mm                           |

---

## Output

The application returns the **most suitable crop** for the given inputs.  
Example: `Recommended Crop: Rice`

---

## Project Structure

```
crop-recommendation/
├── app.py                  # Streamlit application
├── rf_crop_model.pkl       # Trained ML model (Random Forest)
├── crop_classes.npy        # Crop labels (class names)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---

## Tech Stack

- Python
- Streamlit
- Scikit-learn
- NumPy
- Pandas

---



## License

This project is open-source and available under the [MIT License](LICENSE).
