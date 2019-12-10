import React from "react";

import "./_suggestions.scss";

const Suggestions = props => {
  return (
    <ul className="box suggestions">
      {props.suggestions.map((suggestion, index) => (
        <li
          key={index}
          className="suggestion"
          onClick={() => props.onSelection(suggestion)}
        >
          {suggestion}
        </li>
      ))}
    </ul>
  );
};

export default Suggestions;
