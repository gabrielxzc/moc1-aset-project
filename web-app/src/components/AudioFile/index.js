import React from "react";

import "./_audio-file.scss";
import { ALL_AUDIO_TAGS } from "../../commonlib/audio-tags";

const AudioFile = props => {
  const tags = props.tags
    ? props.tags
    : [ALL_AUDIO_TAGS[2], ALL_AUDIO_TAGS[5], ALL_AUDIO_TAGS[8]];

  return (
    <div className="card audio-file">
      <div className="card-content">
        <div className="media">
          <div className="media-left">
            <figure className="image is-48x48">
              <span className="icon is-large" style={{ cursor: "pointer" }}>
                {props.isPlaying ? (
                  <i className="fas fa-2x fa-pause-circle" />
                ) : (
                  <i className="fas fa-2x fa-play-circle" />
                )}
              </span>
            </figure>
          </div>
          <div className="media-content">
            {[...Array(40).keys()].map(index => (
              <div
                key={index}
                className={`bar ${props.isPlaying ? "bar--animated" : ""}`}
              />
            ))}
          </div>
        </div>

        <div className="content audio-file-tags">
          <div className="tags are-small">
            {tags.map((tag, index) => (
              <span key={index} className="tag is-success">
                {tag}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default AudioFile;
