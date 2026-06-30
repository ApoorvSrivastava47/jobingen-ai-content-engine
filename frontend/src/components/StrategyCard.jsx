import {
FaBullseye,
FaLayerGroup,
FaBook,
FaPalette,
FaFileAlt
} from "react-icons/fa";

import "../styles/Card.css";

function format(text){

return text
.replaceAll("_"," ")
.replace(/\b\w/g,c=>c.toUpperCase());

}

function StrategyCard({strategy}){

if(!strategy) return null;

return(

<section className="card">

<h2>

<FaLayerGroup/>

Strategy Overview

</h2>

<div className="strategy-grid">

<div>

<FaFileAlt/>

<strong>Topic</strong>

<p>{format(strategy.topic)}</p>

</div>

<div>

<FaBullseye/>

<strong>Goal</strong>

<p>{format(strategy.goal)}</p>

</div>

<div>

<FaBook/>

<strong>Pillar</strong>

<p>{format(strategy.pillar)}</p>

</div>

<div>

<FaPalette/>

<strong>Tone</strong>

<p>{format(strategy.tone)}</p>

</div>

<div>

<FaLayerGroup/>

<strong>Template</strong>

<p>{format(strategy.template)}</p>

</div>

</div>

</section>

);

}

export default StrategyCard;