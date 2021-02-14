import requests
from bs4 import BeautifulSoup
from goodfood.recipe import Recipe
from string import punctuation


def normalize(s):
    return ' '.join(s.split())


def parse_title(soup):
    return soup.find('h1', class_='header__title heading-1').text


def parse_description(soup):
    description = soup.find('div', class_='mb-lg')
    return normalize(description.find('div', class_='editor-content').text)


def parse_nutrition(soup):
    keys = [key.text for key in soup.find_all('td', class_='key-value-blocks__key')]
    values = [val.text for val in soup.find_all('td', class_='key-value-blocks__value')]
    return {key: value for key, value in zip(keys, values)}


def parse_ingredients(soup):
    ingredients = soup.find('section', class_='recipe__ingredients col-12 mt-md col-lg-6')
    ingredients = ingredients.find_all('li', class_='pb-xxs pt-xxs list-item list-item--separator')
    ingredients = [ingredient.get_text(separator='\n') for ingredient in ingredients]

    result = {}
    for ingredient in ingredients:
        amount, item, *_ = ingredient.split('\n')
        result[normalize(item).translate(str.maketrans('', '', punctuation))] = normalize(amount)
    return result


def parse_method(soup):
    method = soup.find('section', class_='recipe__method-steps mb-lg col-12 col-lg-6')
    return [normalize(step.text) for step in method.find_all('div', class_='editor-content')]


def parse(url):
    """Parse a recipe at url and return a JSON."""

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = parse_title(soup)
    description = parse_description(soup)
    nutrition = parse_nutrition(soup)
    ingredients = parse_ingredients(soup)
    method = parse_method(soup)

    recipe = Recipe(title, description, nutrition, ingredients, method)
    return recipe.to_json()
