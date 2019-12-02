import React from "react";

import "./_audio-file.scss";

function AudioFile() {
  return (
    <div className="card">
      <div className="card-content">
        <div className="media">
          <div className="media-left">
            <figure className="image is-48x48">
              <span className="icon is-large" style={{ cursor: "pointer" }}>
                <i className="fas fa-2x fa-play-circle"></i>
              </span>
            </figure>
          </div>
          <div className="media-content" style={{ height: "50px" }}>
            {[...Array(40).keys()].map(index => (
              <div key={index} className="bar" />
            ))}
          </div>
        </div>

        <div className="content">
          <div className="tags are-small">
            <span className="tag is-success">
              Chirp
              <button className="delete is-small"></button>
            </span>
            <span className="tag is-success">
              Fill
              <button className="delete is-small"></button>
            </span>
            <span className="tag is-success">
              Chink and clink
              <button className="delete is-small"></button>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AudioFile;
