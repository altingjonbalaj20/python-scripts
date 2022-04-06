import * as React from 'react';

export interface State {
    value: number,
    reference: number,
    min: number,
    max: number,
    barAngle: number,
    referenceAngle: number,
    test: any
};

const state: State = {
    value: 0,
    reference: 0,
    min: 0,
    max: 0,
    barAngle: 0,
    referenceAngle: 0,
    test: ''
};

export function updateState(newState: { value; reference; min; max; test }) {
    state.value = newState.value;
    state.reference = newState.reference;
    state.min = newState.min;
    state.max = newState.max;
    state.barAngle = - newState.value / (newState.max - newState.min) * 180;
    state.referenceAngle = newState.reference / (newState.max - newState.min) * 180;
    state.test = newState.test;
}

export function updateGauge() {
    document.getElementById('value').innerHTML = String(state.value);
    document.getElementById('reference').innerHTML = `${state.value > state.reference ? '▲' : '▼'} ${Math.abs(state.value - state.reference)}`;
    document.getElementById('min').innerHTML = `${state.min}`;
    document.getElementById('max').innerHTML = `${state.max}`;
    document.getElementById('bar').style.transform = `rotate(${state.barAngle}deg);`;
    document.getElementById('threshhold').style.transform = `rotate(${state.reference}deg)`;
    document.getElementById('test').innerHTML = `${state.test}`;
};

export function Gauge() {
    return (
        <div className="main">
            <div className="gauge"></div>
            <div className="bar" id='bar'></div>
            <div className="threshhold" id='threshhold'></div>
            <div className="inner-circle"></div>
            <div className="dashboard" id='dashboard'>
                <div className="values">
                    <p className="value" id='value'>{state.value}</p>
                    <p className="reference" id='reference'>{state.value - state.reference > 0 ? '▲' : '▼'} {Math.abs(state.value - state.reference)}</p>
                    <p id='min'>{state.min}</p>
                    <p id='max'>{state.max}</p>
                    <p id='test'>TEST</p>
                </div>
            </div>
        </div>
    )
};