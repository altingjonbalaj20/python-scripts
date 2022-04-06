"use strict";
import powerbi from "powerbi-visuals-api";

import DataView = powerbi.DataView;
import VisualConstructorOptions = powerbi.extensibility.visual.VisualConstructorOptions;
import VisualUpdateOptions = powerbi.extensibility.visual.VisualUpdateOptions;
import IVisual = powerbi.extensibility.visual.IVisual;
import * as React from "react";
import * as ReactDOM from "react-dom";
import { Gauge, updateGauge, updateState } from "./gauge";

import "./../style/visual.less";
let h = 4;
export class Visual implements IVisual {
    private target: HTMLElement;
    private reactRoot: React.ComponentElement<any, any>;
    constructor(options: VisualConstructorOptions) {
        this.reactRoot = Gauge();
        this.target = options.element;
        ReactDOM.render(this.reactRoot, this.target);
    }
    public update(options: VisualUpdateOptions) {
        const dataView: DataView = options.dataViews[0];

        updateState({
            value: Number(dataView.table.rows[0].pop()),
            reference: Number(dataView.table.rows[1].pop()),
            min: Number(dataView.table.rows[2].pop()),
            max: Number(dataView.table.rows[3].pop())
        });
        h++;
        updateGauge();
    }

    private clear() {

    }
}