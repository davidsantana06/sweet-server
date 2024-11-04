from app.database import Product, Products
from app.exception import ProductNotFound
from app.schema import ProductSchema
from app.service import collaborator_service, recipe_service


def create(data: ProductSchema) -> Product:
    collaborator_service.get_one_by_id(data['id_collaborator'])
    recipe_service.get_one_by_id(data['id_recipe'])
    product = Product(**data)
    Product.save(product)
    return product


def get_all() -> Products:
    return Product.find_all()


def get_all_by_name(name: str) -> Products:
    return Product.find_all_by_name(name)


def get_all_unrelated_to_sale(id_sale: int) -> Products:
    realted_ids = []
    return Product.find_all_except(realted_ids)


def get_one_by_id(id: int) -> Product:
    product = Product.find_first_by_id(id)
    if not product: raise ProductNotFound()
    return product


def update(id: int, data: ProductSchema) -> Product:
    collaborator_service.get_one_by_id(data['id_collaborator'])
    recipe_service.get_one_by_id(data['id_recipe'])
    product = get_one_by_id(id)
    product.update(data)
    Product.save(product)
    return product


def delete(id: int) -> None:
    product = get_one_by_id(id)
    Product.delete(product)
