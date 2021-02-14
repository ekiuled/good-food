# good-food
Парсер рецептов с сайта [BBC Good Food](https://www.bbcgoodfood.com/recipes) (тестовое задание).

## Установка

Надо установить зависимости, указанные в `requirements.txt`.

```
pip install -r requirements.txt 
```

## Использование

Парсер принимает URL рецепта и выводит структурированный рецепт в формате JSON.

```
python3 goodfood URL
```

## Структура рецепта

- `title` — название рецепта
- `description` — краткое описание рецепта
- `nutrition` — пищевая ценность
- `ingredients` — ингредиенты и их количества
- `method` — список шагов приготовления

## Пример

```
> python3 goodfood https://www.bbcgoodfood.com/recipes/meatball-black-bean-chilli
{
   "title":"Meatball black bean chilli",
   "description":"Double the amounts for this one-pot black bean chilli, then freeze the leftovers for busy days. It tastes just as great reheated as it does freshly cooked",
   "nutrition":{
      "kcal":"423",
      "fat":"16g",
      "saturates":"4g",
      ...
   },
   "ingredients":{
      "olive oil":"2 tbsp",
      "beef meatballs":"12",
      "onion":"1",
      ...
   },
   "method":[
      "Heat the oil in a large flameproof casserole dish over a medium heat. Fry the meatballs for 5 mins until browned, then transfer to a plate with a slotted spoon.",
      "Fry the onion and peppers with a pinch of salt for 7 mins. Add the coriander stalks, garlic, paprika and cumin and fry for 1 min more. Tip in the sugar, tomatoes and beans, and bring to a simmer. Season, return the meatballs to the pan and cook, covered, for 15 mins. To freeze, leave to cool completely and transfer to large freezerproof bags.",
      "Serve the chilli with the rice and the coriander leaves scattered over."
   ]
}
```