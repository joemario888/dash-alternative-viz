# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class BokehJSON(Component):
    """A BokehJSON component.
BokehJSON renders Bokeh JSON.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- json (dict; optional):
    A Bokeh json object."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_alternative_viz'
    _type = 'BokehJSON'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, json=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'json']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'json']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(BokehJSON, self).__init__(**args)
