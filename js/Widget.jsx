import * as React from "react";
import { createRender, useModelState } from "@anywidget/react";
import "./Widget.css";
import Graph from "./components/Graph";
import Input from "./components/Input";

const render = createRender(() => {

	return (
		<div className="widget">
			<Graph />
			<Input />
		</div>
	);
});

export default { render };
