import * as React from 'react';

export interface State {
    value: number,
    reference: number
};

export const initialState: State = {
    value: 0,
    reference: 0
};

const update = (arg0: { value: number; reference: number; }) => {
    initialState.value = arg0.value;
    initialState.reference = arg0.reference;
};

function Gauge(props) {

    const[value, setValue] = React.useState(props.value);
    const[reference, setReference] = React.useState(props.reference);

    React.useEffect( () => {
        document.getElementById('value').innerHTML = value;
    }, [value]);

    return (
        <div className="main">
            <div className="gauge"></div>
            <div className="bar"></div>
            <div className="threshhold"></div>
            <div className="inner-circle"></div>
            <div className="dashboard">
                <div className="values">
                    <p className="value" id='value'>{props.value}</p>
                    <p className="reference" id='reference'>{props.value > props.reference ? '▲' : '▼'} {Math.abs(props.value - props.reference)}</p>
                </div>
            </div>
        </div>
    )
}

export default Gauge;