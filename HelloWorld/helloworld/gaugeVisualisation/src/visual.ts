"use strict";
import powerbi from "powerbi-visuals-api";

import DataView = powerbi.DataView;
import VisualConstructorOptions = powerbi.extensibility.visual.VisualConstructorOptions;
import VisualUpdateOptions = powerbi.extensibility.visual.VisualUpdateOptions;
import IVisual = powerbi.extensibility.visual.IVisual;
import * as React from "react";
import * as ReactDOM from "react-dom";
import { Gauge, updateGauge, updateState } from "./gauge";

const DataChanged:number = 2;

import "./../style/visual.less";
export class Visual implements IVisual {
    private target: HTMLElement;
    private reactRoot: React.ComponentElement<any, any>;
    constructor(options: VisualConstructorOptions) {
        this.reactRoot = Gauge();
        this.target = options.element;
        ReactDOM.render(this.reactRoot, this.target);
    }
    public update(options: VisualUpdateOptions) {
        
        // on data change 
        if (options.type === DataChanged) {
            const dataView: DataView = options.dataViews[0];
            const values = dataView.matrix.rows.root.children.toString();
            try {
                updateState({
                    value: values[0],
                    reference:  values[1],
                    min:  values[2],
                    max:  values[3],
                    test: values
                });
            } catch (error) {
                
            }
            updateGauge();
            
        }
    }
}