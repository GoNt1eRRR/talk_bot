import json
from google.cloud import dialogflow
from environs import env


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)

    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[message_texts])
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = client.create_intent(
        request={"parent": parent, "intent": intent}
    )


def main():
    env.read_env()
    project_id = env('PROJECT_ID')
    questions_file = env('QUESTIONS_FILE')

    with open(questions_file, 'r', encoding='utf8') as file:
        questions = json.load(file)

    for topic, data in questions.items():
        create_intent(project_id, topic, data['questions'], data['answer'])


if __name__ == "__main__":
    main()
