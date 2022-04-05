import * as React from "react";

export interface State {
    value: number,
    reference: number,
    min:number,
    max:number
}

export const initialState: State = {
    value: 0,
    reference: 0,
    min:0,
    max:0
}

export class Gauge extends React.Component<{}, State>{
    constructor(props: any){
        super(props);
        this.state = initialState;
    }

    private static updateCallback: (data: object) => void = null;

    public static update(newState: State) {
        if(typeof Gauge.updateCallback === 'function'){
            Gauge.updateCallback(newState);
        }
    }

    public state: State = initialState;

    public componentWillMount() {
        Gauge.updateCallback = (newState: State): void => { this.setState(newState); };
    }

    public componentWillUnmount() {
        Gauge.updateCallback = null;
    }

    render(){
        const { value, reference } = this.state;

        return (
            <div className="main">
                <div className="gauge"></div>
                <div className="bar"></div>
                <div className="threshhold"></div>
                <div className="inner-circle"></div>
                <div className="dashboard">
                    <div className="values">
                        <p className="value" id='value'>{value}</p>
                        <p className="reference" id='reference'>{value > reference ? '▲' : '▼'} {Math.abs(value - reference)}</p>
                    </div>
                </div>
            </div>
        )
    }
}