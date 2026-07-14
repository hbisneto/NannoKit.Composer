from .generators import (
    ExtensionGenerator,
    ModuleGenerator
)

def new_extension(name):
    generator = ExtensionGenerator(name)
    return generator.create()

def new_module(name):
    generator = ModuleGenerator(name)
    return generator.create()