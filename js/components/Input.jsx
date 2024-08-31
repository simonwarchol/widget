import * as React from "react";
import { useModelState } from "@anywidget/react";

const Input = () => {

    const [maxValue, setMaxValue] = useModelState("max_value");
    return (
        <div >
            <label>Max Value: </label>
            <input type="number" value={maxValue} onChange={(e) => setMaxValue(parseInt(e.target.value))} />
        </div>
    )
};

export default Input;