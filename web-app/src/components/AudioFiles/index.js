import React, { useEffect, useState } from "react";
import { withRouter } from "react-router-dom";
import queryString from "query-string";

import AudioFile from "../AudioFile";
import Loader from "../../elements/Loader";

import { getAudioFiles } from "../../server-communication/impl/audio-files";

const AudioFiles = props => {
  const [audioFiles, setAudioFiles] = useState();
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    setIsLoading(true);

    const asyncUseEffect = async () => {
      const queryTags = queryString.parse(props.location.search).tags;
      setAudioFiles(await getAudioFiles(queryTags));
    };

    asyncUseEffect().finally(() => setIsLoading(false));
  }, [props.location.search]);

  return (
    <div className="columns is-multiline is-centered is-mobile">
      {isLoading ? (
        <section className="section">
          <Loader />
        </section>
      ) : (
        audioFiles.map((audioFile, index) => (
          <div key={index} className="column is-one-fifth">
            <AudioFile audioFile={audioFile} />
          </div>
        ))
      )}
    </div>
  );
};

export default withRouter(AudioFiles);
