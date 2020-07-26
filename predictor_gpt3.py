import openai
from api import GPT, Example

def main():
    gpt = GPT(engine='davinci',
              temperature=0, max_tokens=100)

    # ONE SHOT LEARNING USING x_train_new and y_train_new
    x_train_new = 'The problem is affecting people using the older versions of the PlayStation 3, called the "Fat" model.The problem isn\'t affecting the newer PS3 Slim systems that have been on sale since September last year.Sony have also said they are aiming to have the problem fixed shortly but is advising some users to avoid using their console for the time being."We hope to resolve this problem within the next 24 hours," a statement reads. "In the meantime, if you have a model other than the new slim PS3, we advise that you do not use your PS3 system, as doing so may result in errors in some functionality, such as recording obtained trophies, and not being able to restore certain data."We believe we have identified that this problem is being caused by a bug in the clock functionality incorporated in the system."The PlayStation Network is used by millions of people around the world.It allows users to play their friends at games like Fifa over the internet and also do things like download software or visit online stores.\n'

    y_train_new = 'Sony has told owners of older models of its PlayStation 3 console to stop using the machine because of a problem with the PlayStation Network.\n'

    gpt.add_example(Example(x_train_new, y_train_new))

    #prompt should be the article we want to get summarised
    prompt = """Iran confirmed another 2,333 new Covid-19 cases on Sunday, continuing a surge in infections that began in mid-May.

    The health ministry also reported another 216 deaths over the past 24 hours, bringing the toll to 15,700.

    Iran began relaxing lockdown measures in April following a drop in the number of infections. It reopened mosques, shopping centres and public parks and allowed travel to resume between provinces.

    The initial outbreak was concentrated in Qom and the capital, Tehran, but the latest flare-up is in the south-west, notably in Khuzestan province bordering Iraq.

    President Hassan Rouhani has told Iranians they must wear masks on public transport and in crowded areas.

    Meanwhile, authorities in Tehran have re-imposed restrictions on some businesses and public gatherings."""

    prompt_refined = preprocess_text(prompt)

    output = gpt.submit_request(prompt_refined)
    y_pred = output.choices[0].text
    y_pred_refined = preprocess_output(y_pred)
    print(y_pred_refined)

def preprocess_text(text, text_length = 1300):
    if len(text.split())>text_length:
        text_temp = text.split()[0:text_length]
        text_return = ''
        for word in text_temp:
            text_return += str(' ')+ word
        return text_return
    else:
        return text

def preprocess_output(text):
    text_temp = text.split('.')
    if text_temp[-1] == '.':
        return text
    else:
        return text_temp[0:-2]

if __name__ == "__main__":
    #establishing api connection
    openai.api_key = "sk-Yzto9XmFW1Ad2GPzLHZ9dTbCLlHr0czXZ3B1vMSF"
    main()