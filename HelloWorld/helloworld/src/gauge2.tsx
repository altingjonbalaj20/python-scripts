import * as React from "react";

export interface State {
    value: number
}

export const initialState: State = {
    value: 0
}

export class Gauge extends React.Component<{}, State>{
    constructor(props: State){
        super(props);
        this.state = initialState;
        this.componentDidMount();
    }

    private static updateCallback: (newState: State) => void = null;

    public static update(newState: State) {
        Gauge.updateCallback(newState);
    }

    public componentWillMount() {
        Gauge.updateCallback = (newState: State): void => { 
            this.setState(newState); };
            this.componentDidUpdate();
    }

    public componentWillUnmount() {
        Gauge.updateCallback = null;
    }

    public componentDidUpdate(): void {
        const { value } = this.state;
        document.getElementById('value').innerHTML = ''+value;
        document.getElementById('reference').innerHTML = `${value ? '▲' : '▼'} ${Math.abs(value)}`;
    }

    render(){
        const { value } = this.state;

        return (
            <div className="main">
                <div className="gauge"></div>
                <div className="bar"></div>
                <div className="threshhold"></div>
                <div className="inner-circle"></div>
                <div className="dashboard">
                    <div className="values">
                        <p className="value">{value}</p>
                        <p className="reference">{value ? '▲' : '▼'} {Math.abs(value)}</p>
                        <p>max</p>
                        <p>min</p>
                    </div>
                </div>
            </div>
        )
    }
}