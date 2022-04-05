"use strict";
import powerbi from "powerbi-visuals-api";

import DataView = powerbi.DataView;
import VisualConstructorOptions = powerbi.extensibility.visual.VisualConstructorOptions;
import VisualUpdateOptions = powerbi.extensibility.visual.VisualUpdateOptions;
import IVisual = powerbi.extensibility.visual.IVisual;
import * as React from "react";
import * as ReactDOM from "react-dom"; 
import {Gauge, initialState} from "./gauge2";

import "./../style/visual.less";

export class Visual implements IVisual {
    private target: HTMLElement;
    private reactRoot: React.ComponentElement<any, any>;

    constructor(options: VisualConstructorOptions) {
        this.reactRoot = React.createElement(Gauge, {});
        this.target = options.element;
        ReactDOM.render(this.reactRoot, this.target);
    }
    public update(options: VisualUpdateOptions) {
        if(options.dataViews && options.dataViews[0] && options.dataViews[1]){
            const dataView: DataView = options.dataViews[0];
        
            Gauge.update({
                value: Number(dataView.metadata.columns[0]),
                reference: Number(dataView.metadata.columns[1]),
                min: Number(dataView.metadata.columns[2]),
                max: Number(dataView.metadata.columns[3])
            });
        } else {
            this.clear();
        }
    }

    private clear() {
        Gauge.update(initialState);
    }
}