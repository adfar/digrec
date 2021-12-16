docker run -it --rm -p 8501:8501 \
-v "$ML_PATH/digits:/models/model" \
-e MODEL_NAME=model \
