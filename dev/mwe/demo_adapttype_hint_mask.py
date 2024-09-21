class MyClass:
    def __init__(self, c: int = 3, c_name=None):
        self.c = c
        self.c_name = c_name


class MySubClass(MyClass):
    def __init__(self, c: int = 3, c_name=None):
        self.c = c
        self.c_name = c_name
        assert False


def main():
    import demo_adapttype_hint_mask
    import geowatch_tpl
    jsonargparse = geowatch_tpl.import_submodule('jsonargparse_fork')
    # import jsonargparse
    parser = jsonargparse.ArgumentParser()
    parser.add_subclass_arguments(demo_adapttype_hint_mask.MyClass, nested_key='myclass', fail_untyped=False, required=True)
    config = parser.parse_args()
    instances = parser.instantiate_classes(config)
    import ubelt as ub
    print(f'instances = {ub.urepr(instances, nl=1)}')
    print(f'{instances.myclass.__dict__=}')


if __name__ == '__main__':
    r"""
    cd ~/code/geowatch/geowatch_tpl/submodules/jsonargparse/dev/mwe
    python demo_adapttype_hint_mask.py \
        --myclass.class_path demo_adapttype_hint_mask.MySubClass \
        --myclass.init_args.c 5
    """
    main()
