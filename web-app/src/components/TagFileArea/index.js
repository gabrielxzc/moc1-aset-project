import React, { useState } from "react";

import TagFileForm from "../TagFileForm";
import Modal from "../../elements/Modal";

function TagFileArea() {
  const [isUploadModalActive, setIsUploadModalActive] = useState(false);

  return (
    <>
      <div className="field">
        <div className="file is-centered is-boxed is-danger has-name">
          <label className="file-label">
          <span className="file-cta" onClick={() => setIsUploadModalActive(true)}>
            <span className="file-icon">
              <i className="fas fa-upload"/>
            </span>
            <span className="file-label">Tag your audio file!</span>
          </span>
          </label>
        </div>
      </div>

      {isUploadModalActive ? <Modal title="Tag your file" isActive onModalClose={() => setIsUploadModalActive(false)}>
        <TagFileForm/>
      </Modal> : null}
    </>
  );
}

export default TagFileArea;
