import React, { useState } from "react";
import tagAudioFile from "../../server-communication/impl/tag-audio-file";
import AudioTags from "../../elements/AudioTags";

function TagFileArea() {
  const [file, setFile] = useState();
  const [errorMsg, setErrorMsg] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const [tags, setTags] = useState();

  const handleFileSelected = (event) => {
    if (event.target.files && event.target.files[0]) {
      const file = event.target.files[0];

      if (!file.name.endsWith('.wav')) {
        setErrorMsg("Only wav files can be tagged");
      } else {
        setErrorMsg(undefined);
        setFile(event.target.files[0]);
      }
    }
  };

  const handleFileUpload = async (event) => {
    event.preventDefault();

    if (!file) {
      setErrorMsg("You must first select a file");
      return;
    }

    setIsLoading(true);
    setTags(await tagAudioFile(file));
    setIsLoading(false);
  }

  return (
    <div className="columns is-centered">
      <section className="section">
        <form noValidate>
          <div className={`file is-centered${file ? " has-name" : ""}`}>
            <label className="file-label">
              <input className="file-input" type="file" onChange={handleFileSelected}/>
              <span className="file-cta">
                <span className="file-icon">
                  <i className="fas fa-upload"/>
                </span>
                <span className="file-label">
                  Choose a file…
                </span>
              </span>

              {file ? <span className="file-name">{file.name}</span> : null}
            </label>
          </div>
          <div className="field">
            <p className=" help" style={{textAlign: "center"}}>You can only upload .wav files</p>
          </div>

          <div className="field buttons is-centered">
            <div className="control">
              <button className={`button is-primary${isLoading ? " is-loading" : ""}`}
                      onClick={handleFileUpload}
                      disabled={isLoading}>
                Submit
              </button>
            </div>
          </div>

          {errorMsg ? <article className="message is-danger">
            <div className="message-body" style={{textAlign: "center"}}>{errorMsg}</div>
          </article> : null}
        </form>

          {tags ? <div className="columns is-centered" style={{paddingTop: "25px"}}>
            <AudioTags tags={tags} isWithDeleteIcon={false}/>
          </div> : null}
      </section>
    </div>
  );
}

export default TagFileArea;
