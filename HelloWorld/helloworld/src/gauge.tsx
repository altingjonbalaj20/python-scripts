import * as React from 'react';

export interface State {
    value: number,
    reference: number,
    min: number,
    max: number
};

const state: State = {
    value: 0,
    reference: 0,
    min: 0,
    max: 0
};

export function updateState(newState: State){
    state.value = newState.value;
    state.reference = newState.reference;
    state.min = newState.min;
    state.max = newState.max;
}

export function updateGauge(){
    document.getElementById('value').innerHTML = String(state.value);
    document.getElementById('reference').innerHTML = `${state.value ? '▲' : '▼'} ${Math.abs(state.value)}`;
    document.getElementById('min').innerHTML = `${state.min}`;
    document.getElementById('max').innerHTML = `${state.max}`;
};

export function Gauge() {
    return (
        <div className="main">
            <div className="gauge"></div>
            <div className="bar"></div>
            <div className="threshhold"></div>
            <div className="inner-circle"></div>
            <div className="dashboard">
                <div className="values">
                    <p className="value" id='value'>{state.value}</p>
                    <p className="reference" id='reference'>{state.value - state.reference > 0 ? '▲' : '▼'} {Math.abs(state.value - state.reference)}</p>
                    <p id='min'>{state.min}</p>
                    <p id='max'>{state.max}</p>
                </div>
            </div>
        </div>
    )
};