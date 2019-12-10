import React, { useEffect } from "react";
import { withRouter } from "react-router-dom";
import queryString from "query-string";

import AudioFile from "../AudioFile";

const AudioFiles = props => {
  useEffect(() => {
    console.log(queryString.parse(props.location.search));
  }, [props.location.search]);

  return (
    <>
      <div className="columns is-centered">
        <div className="column is-one-fifth">
          <AudioFile />
        </div>
        <div className="column is-one-fifth">
          <AudioFile isPlaying />
        </div>
        <div className="column is-one-fifth">
          <AudioFile />
        </div>
        <div className="column is-one-fifth">
          <AudioFile />
        </div>
      </div>
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
    </>
  );
};

export default withRouter(AudioFiles);
