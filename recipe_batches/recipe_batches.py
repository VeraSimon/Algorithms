#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Given a dict denoting a recipe, and another dict denoting ingredients on
    # hand, return how many whole batches of a recipe you can make.
    # Ex. should return 0 since we don't have enough butter!
    # recipe_batches(
    # { 'milk': 100, 'butter': 50, 'flour': 5 },
    # { 'milk': 138, 'butter': 48, 'flour': 51 }
    # )

    # Attempt 1: iterative
    # O(n) for the single for loop
    batch_count = 0
    for k1, v1 in recipe.items():
        if k1 in ingredients and ingredients[k1] // recipe[k1] > 0:
            if ingredients[k1] // recipe[k1] < batch_count or batch_count == 0:
                batch_count = ingredients[k1] // recipe[k1]
        else:
            return 0

    return batch_count


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
