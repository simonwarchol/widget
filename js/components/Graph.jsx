import * as React from "react";
import { useModelState } from "@anywidget/react";
import { VegaLite } from 'react-vega'

const Graph = () => {

    const [data, setData] = useModelState("data");
    const spec = {
        width: 400,
        height: 200,
        mark: 'bar',
        encoding: {
            x: { field: 'a', type: 'ordinal' },
            y: { field: 'b', type: 'quantitative' },
        },
        data: { name: 'table' },
        title: 'Test Graph'
    }


    return (
        <div className='widget'>
            <VegaLite spec={{
                ...spec
            }} data={data} />,

        </div>
    )
};

export default Graph;