from flask import Blueprint, Flask
from importlib import import_module
from os import listdir, path
from types import ModuleType
from typing import Tuple

from ..constants import MODULE_FOLDER, MODULES_FOLDER, MODULE_IMPORT


def _retrieve_module_paths(module_name: str) -> Tuple[str, ...]:
    module_folder = MODULE_FOLDER.format(module_name)
    module_import = MODULE_IMPORT.format(module_name)
    static_folder = path.join(module_folder, 'static')
    static_url_path = f'/{module_import}'
    init_file = path.join(module_folder, '__init__.py')
    routes_import = f'{module_import}.routes'
    routes_file = path.join(module_folder, 'routes.py')
    return (
        module_import, static_folder, static_url_path,
        init_file, routes_file, routes_import
    )


def _retrieve_blueprint(module: ModuleType) -> Blueprint:
    return next(
        (
            value for value in
            module.__dict__.values()
            if isinstance(value, Blueprint)
        ),
        None
    )


def configure_modules(app: Flask) -> None:
    for module_name in listdir(MODULES_FOLDER):
        (
            module_import, static_folder, static_url_path,
            init_file, routes_file, routes_import
        ) = _retrieve_module_paths(module_name)
        if path.exists(init_file):
            module = import_module(module_import)
            blueprint = _retrieve_blueprint(module)
            if blueprint is not None:
                if path.exists(routes_file):
                    import_module(routes_import)
                blueprint.static_folder = static_folder
                blueprint.static_url_path = static_url_path
                app.register_blueprint(blueprint)
