import React from "react";
import AudioFile from "../AudioFile";

function AudioFiles() {
  return (
    <div className="columns is-centered">
      <div className="column is-one-fifth">
        <AudioFile />
      </div>
      <div className="column is-one-fifth">
        <AudioFile />
      </div>
      <div className="column is-one-fifth">
        <AudioFile />
      </div>
      <div className="column is-one-fifth">
        <AudioFile />
      </div>
    </div>
  );
}

export default AudioFiles;
