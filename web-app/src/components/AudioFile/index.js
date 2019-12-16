import React, { useState, useEffect } from "react";

import "./_audio-file.scss";

const AudioFile = props => {
  const [audio, setAudio] = useState();
  const [tags, setTags] = useState([]);
  const [isPlaying, setIsPlaying] = useState(false);

  useEffect(() => {
    setTags(props.audioFile.tags);
    setAudio(new Audio(props.audioFile.uri));
  }, [props.audioFile]);

  return (
    <div className="card audio-file">
      <div className="card-content">
        <div className="media">
          <div className="media-left">
            <figure className="image is-48x48">
              <span className="icon is-large" style={{ cursor: "pointer" }}>
                <span
                  onClick={() => {
                    if (isPlaying) {
                      audio.pause();
                    } else {
                      audio.play();
                    }

                    setIsPlaying(!isPlaying);
                  }}
                >
                  {isPlaying ? (
                    <i className="fas fa-2x fa-pause-circle"></i>
                  ) : (
                    <i className="fas fa-2x fa-play-circle"></i>
                  )}
                </span>
              </span>
            </figure>
          </div>
          <div className="media-content">
            {[...Array(40).keys()].map(index => (
              <div
                key={index}
                className={`bar ${isPlaying ? "bar--animated" : ""}`}
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
