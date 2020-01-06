import React from "react";

import "./_audio-tag.scss";

const AudioTag = props => {
  const getClassNames = () => {
    let classes = "";

    if (props.isWithDeleteIcon) {
      classes += "is-medium is-with-delete-icon";
    } else {
      classes += "is-info";
    }

    return classes;
  };

  return props.isWithDeleteIcon ? (
    <span className={`tag audio-tag ${getClassNames()}`}>
      {props.tag}
      <button
        type="button"
        className="delete is-small"
        onClick={props.handleClick}
      />
    </span>
  ) : (
    <span className={`tag audio-tag ${getClassNames()}`}>{props.tag}</span>
  );
};

export default AudioTag;
