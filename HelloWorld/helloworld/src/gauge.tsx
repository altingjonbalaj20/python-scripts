import * as React from 'react';

export interface State {
    value: number,
    reference: number,
    min: number,
    max: number,
    barAngle: number,
    referenceAngle: number
};

const state: State = {
    value: 0,
    reference: 0,
    min: 0,
    max: 0,
    barAngle: 0,
    referenceAngle: 0
};

export function updateState(newState :{value; reference; min; max}){
    state.value = newState.value;
    state.reference = newState.reference;
    state.min = newState.min;
    state.max = newState.max;
    state.barAngle = - newState.value / (newState.max - newState.min) * 180;
    state.referenceAngle = newState.reference / (newState.max - newState.min) * 180;
}

export function updateGauge(){
    document.getElementById('value').innerHTML = String(state.value);
    document.getElementById('reference').innerHTML = `${state.value ? '▲' : '▼'} ${Math.abs(state.value)}`;
    document.getElementById('min').innerHTML = `${state.min}`;
    document.getElementById('max').innerHTML = `${state.max}`;
    document.getElementById('bar').style.transform = `rotate(${state.barAngle}deg);`;
    document.getElementById('threshhold').style.transform = `rotate(${state.reference}deg)`;
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
                </div>
            </div>
        </div>
    )
};