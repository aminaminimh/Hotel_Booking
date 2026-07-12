# Overview

The project is designed to be deployed as a FastAPI web application.

Deployment allows anyone to access the prediction model through a web browser without installing Python locally.

# Project Structure

```
app.py

  ↓

Load Model

  ↓

FastAPI

  ↓

Web Browser
```

# Local Deployment

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn src.app:app --reload
```

Open:

```
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

# Model Files

The application loads the following files during startup:

```
xgb_model.pkl

encoder.pkl

country_imputer.pkl

children_imputer.pkl

top_countries.pkl
```

These files must always remain synchronized with the preprocessing pipeline used during training.

# Future Improvements

Potential production enhancements:

- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] HTTPS support
- [ ] Logging
- [ ] Monitoring
- [ ] Automatic model versioning
- [ ] Cloud storage for models
- [ ] GPU inference support