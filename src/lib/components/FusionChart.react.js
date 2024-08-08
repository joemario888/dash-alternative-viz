import React, {Component} from 'react';
import PropTypes from 'prop-types';
import ReactDOM from 'react-dom';
const ReactFC = require("./react-fusioncharts.js");
const FusionCharts = require('./fusioncharts.js');
const Charts = require('./fusioncharts.charts.js');
const FusionTheme = require('./fusioncharts.theme.fusion.js');

ReactFC.fcRoot(FusionCharts, Charts, FusionTheme);

/**
 * FusionChart renders FusionCharts.js JSON. Test
 */
export default class FusionChart extends Component {
    render() {
        const {constructorType, options} = this.props;
        return (
            <ReactFC
                type={constructorType}
                width="500"
                height="600"
                dataFormat="JSON"
                dataSource={options}
              />
        );
    }
}

ReactDOM.render(
    <FusionChart />,
    document.getElementById('react-entry-point'),
  );

FusionChart.defaultProps = {};
FusionChart.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    /**
     * 'chart', 'stockChart', 'mapChart', 'ganttChart'
     */
    constructorType: PropTypes.string,
    /**
     * The FusionCharts chart description
     */
    options: PropTypes.object,
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
