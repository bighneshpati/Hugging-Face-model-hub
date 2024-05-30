
import requests
import json

def fetch_top_models():
    url = "https://huggingface.co/api/models?sort=downloads"
    response = requests.get(url)
    models = response.json()
    
    # Extract top 10 models
    top_models = models[:10]
    return top_models

def generate_report(models):
    report = "Top 10 Hugging Face Models by Downloads:\n\n"
    for idx, model in enumerate(models):
        report += f"{idx + 1}. {model['modelId']} - {model['downloads']} downloads\n"
    return report

def main():
    top_models = fetch_top_models()
    report = generate_report(top_models)
    print(report)

if __name__ == "__main__":
    main()

