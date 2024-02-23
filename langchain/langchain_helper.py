from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

llm = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed", temperature=0.6) #


def generate_restaurant_name_and_menu(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="""I want to open a restaurant for {cuisine} food, suggest the best fancy name for the restaurant."""
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest 10 items in the food menu for {restaurant_name}. Return it as a comma separated list"
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )
    response = chain({
        'cuisine': cuisine,
    })

    print(response)
    return response


# if __name__ == "__main__":
#     print(generate_restaurant_name_and_menu('Italian'))
