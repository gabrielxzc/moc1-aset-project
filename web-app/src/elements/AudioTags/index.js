import React from "react";

import AudioTag from "../AudioTag";

const AudioTags = props => {
  return <div className="tags are-medium">
    {props.tags.map((tag, index) => (
      <AudioTag
        key={index}
        className="is-info"
        tag={tag}
        isWithDeleteIcon={props.isWithDeleteIcon}
        handleClick={(tag) => props.handleTagDelete(tag)}
      />
    ))}
  </div>
};

export default AudioTags;
