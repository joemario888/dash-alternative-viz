# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FusionChart(Component):
    """A FusionChart component.
FusionChart renders FusionCharts.js JSON. Test

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- constructorType (string; optional):
    'chart', 'stockChart', 'mapChart', 'ganttChart'.

- options (dict; optional):
    The FusionCharts chart description."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_alternative_viz'
    _type = 'FusionChart'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, constructorType=Component.UNDEFINED, options=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'constructorType', 'options']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'constructorType', 'options']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FusionChart, self).__init__(**args)
