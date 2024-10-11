from werkzeug.exceptions import NotFound
from app.database import (
    Product, Products,
    RelatedIds, SelectChoices
)
from .forms import ProductForm


def create(
    id_recipe: int, id_labor: int, name: str,
    loss_margin: float, contribuition_margin: float
) -> Product:
    product = Product(
        id_recipe, id_labor, name,
        loss_margin, contribuition_margin
    )
    Product.save(product)
    return product


def get_all() -> Products:
    return Product.find_all()


def get_all_by_name(name: str) -> Products:
    return Product.find_all_by_name(name)


def get_all_select_choices(related_ids: RelatedIds) -> SelectChoices:
    return Product.find_all_select_choices_not_related_to_sale(related_ids)


def get_one_by_id(id: int) -> Product:
    product = Product.find_first_by_id(id)
    if not product:
        raise NotFound('The product was not found.')
    return product


def update(product: Product, form: ProductForm) -> Product:
    form.populate_obj(product)
    Product.save(product)
    return product


def delete(product: Product) -> None:
    Product.delete(product)
