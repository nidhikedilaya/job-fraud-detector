def preprocess_input(data):
    title = data.get("title", "").lower()
    description = data.get("description", "").lower()
    return title + " " + description
