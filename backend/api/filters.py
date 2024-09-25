from django_filters.rest_framework import (AllValuesMultipleFilter,
                                           BooleanFilter, FilterSet,
                                           ModelMultipleChoiceFilter)
from rest_framework.filters import SearchFilter

from recipes.models import Recipe
from users.models import User


class IngredientFilter(SearchFilter):
    search_param = 'name'


class RecipeFilter(FilterSet):
    """Фильтр для списка рецептов."""
    tags = AllValuesMultipleFilter(
        field_name='tags__slug'
    )
    author = ModelMultipleChoiceFilter(
        field_name='author__id',
        to_field_name='id',
        queryset=User.objects.all()
    )
    is_favorited = BooleanFilter(
        method='filter_is_favorited',
    )
    is_in_shopping_cart = BooleanFilter(
        method='filter_is_in_shopping_cart',
    )

    def filter_is_favorited(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def filter_is_in_shopping_cart(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(shopping_cart__user=self.request.user)
        return queryset

    class Meta:
        model = Recipe
        fields = [
            'author',
            'is_favorited',
            'is_in_shopping_cart',
            'tags'
        ]