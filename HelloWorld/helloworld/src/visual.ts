"use strict";
import powerbi from "powerbi-visuals-api";

import DataView = powerbi.DataView;
import VisualConstructorOptions = powerbi.extensibility.visual.VisualConstructorOptions;
import VisualUpdateOptions = powerbi.extensibility.visual.VisualUpdateOptions;
import IVisual = powerbi.extensibility.visual.IVisual;
import * as React from "react";
import * as ReactDOM from "react-dom";
import { Gauge, updateGauge, updateState } from "./gauge";

const DataType = 2;
let h = 1;
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
        if (options.type === DataType && options.dataViews[0]) {
            const dataView: DataView = options.dataViews[0];
            updateState({
                value: Number(dataView.table.rows[3].toString()),
                reference: Number(dataView.table.rows[2].toString()),
                min: Number(++h),
                max: Number(++h)
            });
            updateGauge();
        }
    }

    private clear() {

    }
}