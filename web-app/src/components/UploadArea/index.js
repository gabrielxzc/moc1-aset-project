import React from "react";

function UploadArea() {
  return (
    <div className="field">
      <div className="file is-centered is-boxed is-danger has-name">
        <label className="file-label">
          <input className="file-input" type="file" name="audioFile" />
          <span className="file-cta">
            <span className="file-icon">
              <i className="fas fa-upload"></i>
            </span>
            <span className="file-label">Tag your audio file!</span>
          </span>
          <span className="file-name has-text-centered">fill-and-gasp.wav</span>
        </label>
      </div>
    </div>
  );
}

export default UploadArea;
